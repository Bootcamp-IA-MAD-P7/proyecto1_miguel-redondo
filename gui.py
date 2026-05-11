import logging
import time

import customtkinter as ctk
from taximetro import (
    MOVING_RATE,
    STOPPED_RATE,
    Taximeter,
    calculate_fare,
    load_password,
    load_rates,
    save_trip_history,
)

class TaximeterGUI(ctk.CTk):
    """
    Interfaz grafica inicial del taximetro.
    """

    def __init__(self):
        super().__init__()

        self.title("Taximetro Digital F5")
        self.geometry("980x620")
        self.minsize(900, 560)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.stopped_rate, self.moving_rate = load_rates()
        self.expected_password = load_password()
        self.taximeter = Taximeter(self.stopped_rate, self.moving_rate)
        self.refresh_after_id = None
        self.state_buttons = {}
        self.remaining_attempts = 3

        self.configure(fg_color="#f4f6f8")
        logging.info("Interfaz grafica iniciada")
        self._build_login_screen()

    def _build_login_screen(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        login_frame = ctk.CTkFrame(self, fg_color="#ffffff", corner_radius=8, width=420, height=310)
        login_frame.grid(row=0, column=0, sticky="", padx=24, pady=24)
        login_frame.grid_propagate(False)

        title = ctk.CTkLabel(
            login_frame,
            text="Acceso al taximetro",
            font=("Arial", 24, "bold"),
            text_color="#111827",
        )
        title.pack(anchor="w", padx=32, pady=(34, 8))

        description = ctk.CTkLabel(
            login_frame,
            text="Introduce la contrasena configurada para abrir el panel de control.",
            font=("Arial", 13),
            text_color="#64748b",
            wraplength=340,
            justify="left",
        )
        description.pack(anchor="w", padx=32, pady=(0, 22))

        self.password_entry = ctk.CTkEntry(
            login_frame,
            placeholder_text="Contrasena",
            show="*",
            height=42,
            border_width=1,
        )
        self.password_entry.pack(fill="x", padx=32, pady=(0, 12))
        self.password_entry.bind("<Return>", lambda event: self._validate_password())
        self.password_entry.focus()

        self.login_message = ctk.CTkLabel(
            login_frame,
            text="Tienes 3 intentos disponibles.",
            font=("Arial", 12),
            text_color="#64748b",
        )
        self.login_message.pack(anchor="w", padx=32, pady=(0, 18))

        self.login_button = ctk.CTkButton(
            login_frame,
            text="Entrar",
            height=42,
            corner_radius=6,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 14, "bold"),
            command=self._validate_password,
        )
        self.login_button.pack(fill="x", padx=32, pady=(0, 34))

    def _validate_password(self):
        password = self.password_entry.get().strip()

        if password == self.expected_password:
            logging.info("Autenticacion correcta en GUI")
            self._show_taximeter_screen()
            return

        self.remaining_attempts -= 1
        logging.warning("Intento de autenticacion fallido en GUI")

        if self.remaining_attempts == 0:
            logging.warning("Acceso denegado en GUI por agotar intentos")
            self.login_message.configure(
                text="Acceso denegado. Cierra la aplicacion y vuelve a intentarlo.",
                text_color="#b91c1c",
            )
            self.login_button.configure(state="disabled")
            self.password_entry.configure(state="disabled")
            return

        self.login_message.configure(
            text=f"Contrasena incorrecta. Intentos restantes: {self.remaining_attempts}.",
            text_color="#b91c1c",
        )
        self.password_entry.delete(0, "end")

    def _show_taximeter_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self._build_header()
        self._build_main_panel()
        self._build_side_panel()
        self._build_footer()

    def _configure_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(1, weight=1)

    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color="#111827", corner_radius=0)
        header.grid(row=0, column=0, columnspan=2, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Taximetro Digital F5",
            font=("Arial", 24, "bold"),
            text_color="#ffffff",
        )
        title.grid(row=0, column=0, sticky="w", padx=28, pady=(20, 4))

        subtitle = ctk.CTkLabel(
            header,
            text="Panel de control para trayectos, tarifas y estado del servicio",
            font=("Arial", 13),
            text_color="#cbd5e1",
        )
        subtitle.grid(row=1, column=0, sticky="w", padx=28, pady=(0, 18))

    def _build_main_panel(self):
        main = ctk.CTkFrame(self, fg_color="#ffffff", corner_radius=8)
        main.grid(row=1, column=0, sticky="nsew", padx=(24, 12), pady=24)
        main.grid_columnconfigure((0, 1), weight=1)

        status_label = ctk.CTkLabel(
            main,
            text="Estado actual",
            font=("Arial", 13, "bold"),
            text_color="#64748b",
        )
        status_label.grid(row=0, column=0, sticky="w", padx=28, pady=(26, 4))

        self.status_value = ctk.CTkLabel(
            main,
            text="Sin trayecto activo",
            font=("Arial", 28, "bold"),
            text_color="#0f172a",
        )
        self.status_value.grid(row=1, column=0, sticky="w", padx=28, pady=(0, 8))

        fare_label = ctk.CTkLabel(
            main,
            text="Importe actual",
            font=("Arial", 13, "bold"),
            text_color="#64748b",
        )
        fare_label.grid(row=0, column=1, sticky="e", padx=28, pady=(26, 4))

        self.fare_value = ctk.CTkLabel(
            main,
            text="0.00 euros",
            font=("Arial", 34, "bold"),
            text_color="#0f766e",
        )
        self.fare_value.grid(row=1, column=1, sticky="e", padx=28, pady=(0, 8))

        metrics = ctk.CTkFrame(main, fg_color="#f8fafc", corner_radius=8)
        metrics.grid(row=2, column=0, columnspan=2, sticky="ew", padx=28, pady=(18, 18))
        metrics.grid_columnconfigure((0, 1), weight=1)

        self.stopped_time_value = self._metric(metrics, 0, "Tiempo parado", "00:00:00")
        self.moving_time_value = self._metric(metrics, 1, "Tiempo en movimiento", "00:00:00")

        self.final_total_panel = ctk.CTkFrame(main, fg_color="#f8fafc", corner_radius=8)
        self.final_total_panel.grid(row=3, column=0, columnspan=2, sticky="ew", padx=28, pady=(0, 12))

        self.final_total_value = ctk.CTkLabel(
            self.final_total_panel,
            text="Total final pendiente",
            font=("Arial", 18, "bold"),
            text_color="#475569",
        )
        self.final_total_value.pack(anchor="w", padx=18, pady=14)

        actions = ctk.CTkFrame(main, fg_color="#ffffff", corner_radius=8)
        actions.grid(row=4, column=0, columnspan=2, sticky="ew", padx=28, pady=(0, 8))
        actions.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._action_button(actions, 0, "Iniciar", "#2563eb", "#1d4ed8", self.start_trip)
        self.state_buttons["stopped"] = self._action_button(
            actions,
            1,
            "Parado",
            "#475569",
            "#334155",
            self.set_stopped,
        )
        self.state_buttons["moving"] = self._action_button(
            actions,
            2,
            "Movimiento",
            "#0f766e",
            "#115e59",
            self.set_moving,
        )
        self._action_button(actions, 3, "Finalizar", "#b91c1c", "#991b1b", self.finish_trip)

        self.instruction_value = ctk.CTkLabel(
            main,
            text="Pulsa Iniciar para comenzar un nuevo trayecto. El taxi empezara en estado parado.",
            font=("Arial", 13),
            text_color="#475569",
            wraplength=780,
            justify="left",
        )
        self.instruction_value.grid(row=5, column=0, columnspan=2, sticky="w", padx=28, pady=(0, 26))

    def _build_side_panel(self):
        side = ctk.CTkFrame(self, fg_color="#ffffff", corner_radius=8, width=270)
        side.grid(row=1, column=1, sticky="ns", padx=(12, 24), pady=24)
        side.grid_propagate(False)

        title = ctk.CTkLabel(
            side,
            text="Configuracion",
            font=("Arial", 18, "bold"),
            text_color="#0f172a",
        )
        title.pack(anchor="w", padx=22, pady=(24, 14))

        self._build_rate_editor(side)
        self._info_row(side, "Autenticacion", "Activa")
        self._info_row(side, "Tests", "12 pasados")

        separator = ctk.CTkFrame(side, fg_color="#e2e8f0", height=1)
        separator.pack(fill="x", padx=22, pady=18)

        history_title = ctk.CTkLabel(
            side,
            text="Ultimo trayecto",
            font=("Arial", 15, "bold"),
            text_color="#334155",
        )
        history_title.pack(anchor="w", padx=22, pady=(0, 8))

        self.history_text = ctk.CTkLabel(
            side,
            text="Sin trayectos en esta sesion",
            font=("Arial", 13),
            text_color="#64748b",
            justify="left",
        )
        self.history_text.pack(anchor="w", padx=22)

    def _build_footer(self):
        footer = ctk.CTkFrame(self, fg_color="#f4f6f8", corner_radius=0)
        footer.grid(row=2, column=0, columnspan=2, sticky="ew", padx=24, pady=(0, 18))
        footer.grid_columnconfigure(0, weight=1)

        text = ctk.CTkLabel(
            footer,
            text="Version GUI inicial - Nivel avanzado",
            font=("Arial", 12),
            text_color="#64748b",
        )
        text.grid(row=0, column=0, sticky="w")

    def _metric(self, parent, column, label, value):
        frame = ctk.CTkFrame(parent, fg_color="#ffffff", corner_radius=8)
        frame.grid(row=0, column=column, sticky="ew", padx=10, pady=12)

        label_widget = ctk.CTkLabel(
            frame,
            text=label,
            font=("Arial", 12, "bold"),
            text_color="#64748b",
        )
        label_widget.pack(anchor="w", padx=18, pady=(14, 2))

        value_widget = ctk.CTkLabel(
            frame,
            text=value,
            font=("Arial", 24, "bold"),
            text_color="#111827",
        )
        value_widget.pack(anchor="w", padx=18, pady=(0, 14))
        return value_widget

    def _action_button(self, parent, column, text, fg_color, hover_color, command):
        button = ctk.CTkButton(
            parent,
            text=text,
            height=44,
            corner_radius=6,
            fg_color=fg_color,
            hover_color=hover_color,
            font=("Arial", 14, "bold"),
            command=command,
        )
        button.grid(row=0, column=column, sticky="ew", padx=6, pady=8)
        return button

    def _info_row(self, parent, label, value):
        row = ctk.CTkFrame(parent, fg_color="#f8fafc", corner_radius=6)
        row.pack(fill="x", padx=22, pady=5)

        label_widget = ctk.CTkLabel(
            row,
            text=label,
            font=("Arial", 12, "bold"),
            text_color="#64748b",
        )
        label_widget.pack(anchor="w", padx=14, pady=(10, 0))

        value_widget = ctk.CTkLabel(
            row,
            text=value,
            font=("Arial", 15, "bold"),
            text_color="#0f172a",
        )
        value_widget.pack(anchor="w", padx=14, pady=(0, 10))

    def _build_rate_editor(self, parent):
        editor = ctk.CTkFrame(parent, fg_color="#f8fafc", corner_radius=6)
        editor.pack(fill="x", padx=22, pady=5)

        title = ctk.CTkLabel(
            editor,
            text="Tarifas",
            font=("Arial", 12, "bold"),
            text_color="#64748b",
        )
        title.pack(anchor="w", padx=14, pady=(10, 4))

        self.stopped_rate_entry = self._rate_entry(editor, "Parado", self.stopped_rate)
        self.moving_rate_entry = self._rate_entry(editor, "Movimiento", self.moving_rate)

        self.rate_message = ctk.CTkLabel(
            editor,
            text="Si no cambias nada, se usan las tarifas por defecto.",
            font=("Arial", 11),
            text_color="#64748b",
            wraplength=200,
            justify="left",
        )
        self.rate_message.pack(anchor="w", padx=14, pady=(4, 8))

        apply_button = ctk.CTkButton(
            editor,
            text="Aplicar tarifas",
            height=32,
            corner_radius=6,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 12, "bold"),
            command=self.apply_rates,
        )
        apply_button.pack(fill="x", padx=14, pady=(0, 6))

        reset_button = ctk.CTkButton(
            editor,
            text="Restaurar defecto",
            height=32,
            corner_radius=6,
            fg_color="#64748b",
            hover_color="#475569",
            font=("Arial", 12, "bold"),
            command=self.reset_default_rates,
        )
        reset_button.pack(fill="x", padx=14, pady=(0, 12))

    def _rate_entry(self, parent, label, value):
        label_widget = ctk.CTkLabel(
            parent,
            text=f"{label} (euros/s)",
            font=("Arial", 11, "bold"),
            text_color="#334155",
        )
        label_widget.pack(anchor="w", padx=14, pady=(4, 2))

        entry = ctk.CTkEntry(parent, height=32)
        entry.insert(0, str(value))
        entry.pack(fill="x", padx=14)
        return entry

    def apply_rates(self, silent=False):
        if self.taximeter.trip_active:
            self.rate_message.configure(
                text="Finaliza el trayecto activo antes de cambiar tarifas.",
                text_color="#b91c1c",
            )
            return False

        try:
            stopped_rate = float(self.stopped_rate_entry.get().replace(",", "."))
            moving_rate = float(self.moving_rate_entry.get().replace(",", "."))
        except ValueError:
            self.rate_message.configure(
                text="Introduce tarifas numericas validas.",
                text_color="#b91c1c",
            )
            return False

        if stopped_rate < 0 or moving_rate < 0:
            self.rate_message.configure(
                text="Las tarifas no pueden ser negativas.",
                text_color="#b91c1c",
            )
            return False

        self.stopped_rate = stopped_rate
        self.moving_rate = moving_rate
        self.taximeter.stopped_rate = stopped_rate
        self.taximeter.moving_rate = moving_rate

        if not silent:
            self.rate_message.configure(
                text="Tarifas aplicadas para los proximos trayectos.",
                text_color="#166534",
            )
        logging.info(f"Tarifas actualizadas desde GUI: parado={stopped_rate}, movimiento={moving_rate}")
        return True

    def reset_default_rates(self):
        if self.taximeter.trip_active:
            self.rate_message.configure(
                text="Finaliza el trayecto activo antes de restaurar tarifas.",
                text_color="#b91c1c",
            )
            return

        self.stopped_rate_entry.delete(0, "end")
        self.stopped_rate_entry.insert(0, str(STOPPED_RATE))
        self.moving_rate_entry.delete(0, "end")
        self.moving_rate_entry.insert(0, str(MOVING_RATE))
        self.apply_rates()

    def start_trip(self):
        if not self.apply_rates(silent=True):
            return

        if not self.taximeter.start_trip():
            logging.warning("Intento de iniciar un trayecto activo desde GUI")
            self.status_value.configure(text="Ya hay un trayecto activo")
            return

        logging.info("Trayecto iniciado desde GUI")
        self.status_value.configure(text="Trayecto activo")
        self.fare_value.configure(text="0.00 euros")
        self.final_total_panel.configure(fg_color="#f8fafc")
        self.final_total_value.configure(text="Total final pendiente")
        self.final_total_value.configure(text_color="#475569")
        self.instruction_value.configure(
            text="El taxi esta parado. Pulsa Movimiento cuando empiece a circular o Finalizar para cerrar el trayecto."
        )
        self._highlight_state_button("stopped")
        self._refresh_trip_display()

    def set_stopped(self):
        if not self.taximeter.change_state("stopped"):
            logging.warning("Intento de cambiar a parado sin trayecto activo desde GUI")
            self.status_value.configure(text="Inicia un trayecto primero")
            return

        logging.info("Estado actualizado desde GUI: parado")
        self.status_value.configure(text="Taxi parado")
        self.instruction_value.configure(
            text="El taxi esta parado. El importe se calcula a tarifa reducida hasta que pulses Movimiento."
        )
        self._highlight_state_button("stopped")
        self._refresh_trip_display()

    def set_moving(self):
        if not self.taximeter.change_state("moving"):
            logging.warning("Intento de cambiar a movimiento sin trayecto activo desde GUI")
            self.status_value.configure(text="Inicia un trayecto primero")
            return

        logging.info("Estado actualizado desde GUI: en movimiento")
        self.status_value.configure(text="Taxi en movimiento")
        self.instruction_value.configure(
            text="El taxi esta en movimiento. El importe se calcula a tarifa de movimiento hasta que pulses Parado o Finalizar."
        )
        self._highlight_state_button("moving")
        self._refresh_trip_display()

    def finish_trip(self):
        self._cancel_refresh()
        summary = self.taximeter.finish_trip()

        if summary is None:
            logging.warning("Intento de finalizar sin trayecto activo desde GUI")
            self.status_value.configure(text="Inicia un trayecto primero")
            return

        save_trip_history(
            summary["stopped_time"],
            summary["moving_time"],
            summary["total_fare"],
        )
        logging.info(
            f"Trayecto finalizado desde GUI. Tiempo parado: {summary['stopped_time']:.1f}s, "
            f"tiempo en movimiento: {summary['moving_time']:.1f}s, "
            f"total: {summary['total_fare']:.2f} euros"
        )

        self.status_value.configure(text="Trayecto finalizado")
        self.fare_value.configure(text=f"{summary['total_fare']:.2f} euros")
        self.final_total_panel.configure(fg_color="#dcfce7")
        self.final_total_value.configure(text=f"Importe final del trayecto: {summary['total_fare']:.2f} euros")
        self.final_total_value.configure(text_color="#166534")
        self.stopped_time_value.configure(text=self._format_seconds(summary["stopped_time"]))
        self.moving_time_value.configure(text=self._format_seconds(summary["moving_time"]))
        self.instruction_value.configure(
            text="Trayecto finalizado. Pulsa Iniciar para registrar un nuevo trayecto sin cerrar la aplicacion."
        )
        self.history_text.configure(
            text=(
                f"Parado: {summary['stopped_time']:.1f}s\n"
                f"Movimiento: {summary['moving_time']:.1f}s\n"
                f"Total: {summary['total_fare']:.2f} euros"
            )
        )
        self._clear_state_button_highlight()

    def _highlight_state_button(self, active_state):
        self._clear_state_button_highlight()

        button = self.state_buttons.get(active_state)
        if button is None:
            return

        button.configure(border_width=3, border_color="#f59e0b")

    def _clear_state_button_highlight(self):
        for button in self.state_buttons.values():
            button.configure(border_width=0)

    def _get_current_totals(self):
        stopped_time = self.taximeter.stopped_time
        moving_time = self.taximeter.moving_time

        if self.taximeter.trip_active:
            elapsed = time.time() - self.taximeter.state_start_time

            if self.taximeter.state == "stopped":
                stopped_time += elapsed
            elif self.taximeter.state == "moving":
                moving_time += elapsed

        total_fare = calculate_fare(
            stopped_time,
            moving_time,
            self.stopped_rate,
            self.moving_rate,
        )

        return stopped_time, moving_time, total_fare

    def _refresh_trip_display(self):
        self._cancel_refresh()

        stopped_time, moving_time, total_fare = self._get_current_totals()
        self.stopped_time_value.configure(text=self._format_seconds(stopped_time))
        self.moving_time_value.configure(text=self._format_seconds(moving_time))
        self.fare_value.configure(text=f"{total_fare:.2f} euros")

        if self.taximeter.trip_active:
            self.refresh_after_id = self.after(500, self._refresh_trip_display)

    def _cancel_refresh(self):
        if self.refresh_after_id is None:
            return

        try:
            self.after_cancel(self.refresh_after_id)
        except Exception:
            pass

        self.refresh_after_id = None

    def _format_seconds(self, seconds):
        total_seconds = int(seconds)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def main():
    app = TaximeterGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
