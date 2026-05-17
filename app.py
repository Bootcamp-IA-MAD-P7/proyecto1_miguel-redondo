import time

from flask import Flask, redirect, render_template, request, session, url_for

from database import get_recent_trips, init_database, save_trip_to_database
from taximetro import calculate_fare, load_password, load_rates, save_trip_history

app = Flask(__name__)
app.secret_key = "taximetro-dev-secret-key"


def get_trip_state():
    return {
        "trip_active": session.get("trip_active", False),
        "state": session.get("state"),
        "state_start_time": session.get("state_start_time", 0),
        "stopped_time": session.get("stopped_time", 0),
        "moving_time": session.get("moving_time", 0),
        "last_total": session.get("last_total"),
    }


def save_trip_state(trip_state):
    session["trip_active"] = trip_state["trip_active"]
    session["state"] = trip_state["state"]
    session["state_start_time"] = trip_state["state_start_time"]
    session["stopped_time"] = trip_state["stopped_time"]
    session["moving_time"] = trip_state["moving_time"]
    session["last_total"] = trip_state["last_total"]


def accumulate_current_state(trip_state):
    if not trip_state["trip_active"]:
        return

    elapsed = time.time() - trip_state["state_start_time"]

    if trip_state["state"] == "stopped":
        trip_state["stopped_time"] += elapsed
    elif trip_state["state"] == "moving":
        trip_state["moving_time"] += elapsed

    trip_state["state_start_time"] = time.time()


def get_current_totals(trip_state, stopped_rate, moving_rate):
    stopped_time = trip_state["stopped_time"]
    moving_time = trip_state["moving_time"]

    if trip_state["trip_active"]:
        elapsed = time.time() - trip_state["state_start_time"]

        if trip_state["state"] == "stopped":
            stopped_time += elapsed
        elif trip_state["state"] == "moving":
            moving_time += elapsed

    total_fare = calculate_fare(stopped_time, moving_time, stopped_rate, moving_rate)
    return stopped_time, moving_time, total_fare


def get_status_label(trip_state):
    if not trip_state["trip_active"]:
        if trip_state["last_total"] is not None:
            return "Finalizado"
        return "Libre"

    if trip_state["state"] == "stopped":
        return "Parado"

    if trip_state["state"] == "moving":
        return "Ocupado"

    return "Libre"


@app.route("/")
def index():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    stopped_rate, moving_rate = load_rates()
    trip_state = get_trip_state()
    stopped_time, moving_time, total_fare = get_current_totals(
        trip_state,
        stopped_rate,
        moving_rate,
    )
    trips = get_recent_trips(limit=5)

    return render_template(
        "dashboard.html",
        stopped_rate=stopped_rate,
        moving_rate=moving_rate,
        trips=trips,
        trip_state=trip_state,
        stopped_time=stopped_time,
        moving_time=moving_time,
        total_fare=total_fare,
        status_label=get_status_label(trip_state),
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        password = request.form.get("password", "").strip()

        if password == load_password():
            session["authenticated"] = True
            return redirect(url_for("index"))

        error = "Contrasena incorrecta."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/start", methods=["POST"])
def start_trip():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    trip_state = get_trip_state()

    if not trip_state["trip_active"]:
        trip_state["trip_active"] = True
        trip_state["state"] = "stopped"
        trip_state["state_start_time"] = time.time()
        trip_state["stopped_time"] = 0
        trip_state["moving_time"] = 0
        trip_state["last_total"] = None
        save_trip_state(trip_state)

    return redirect(url_for("index"))


@app.route("/stop", methods=["POST"])
def stop_trip():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    trip_state = get_trip_state()

    if trip_state["trip_active"]:
        accumulate_current_state(trip_state)
        trip_state["state"] = "stopped"
        save_trip_state(trip_state)

    return redirect(url_for("index"))


@app.route("/move", methods=["POST"])
def move_trip():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    trip_state = get_trip_state()

    if trip_state["trip_active"]:
        accumulate_current_state(trip_state)
        trip_state["state"] = "moving"
        save_trip_state(trip_state)

    return redirect(url_for("index"))


@app.route("/finish", methods=["POST"])
def finish_trip():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    stopped_rate, moving_rate = load_rates()
    trip_state = get_trip_state()

    if trip_state["trip_active"]:
        accumulate_current_state(trip_state)

        total_fare = calculate_fare(
            trip_state["stopped_time"],
            trip_state["moving_time"],
            stopped_rate,
            moving_rate,
        )

        save_trip_history(
            trip_state["stopped_time"],
            trip_state["moving_time"],
            total_fare,
        )
        save_trip_to_database(
            trip_state["stopped_time"],
            trip_state["moving_time"],
            stopped_rate,
            moving_rate,
            total_fare,
        )

        trip_state["trip_active"] = False
        trip_state["state"] = None
        trip_state["state_start_time"] = 0
        trip_state["last_total"] = total_fare
        save_trip_state(trip_state)

    return redirect(url_for("index"))


if __name__ == "__main__":
    init_database()
    app.run(debug=True)
