from datetime import datetime
import flet as ft

# Registro centralizado de reservas (RF-07)
RESERVAS_GUARDADAS = {
    datetime.now().strftime("%Y-%m-%d"): ["10:00", "16:00", "18:00"]
}


def pantalla2Mostrar(page: ft.Page):
    fecha_seleccionada = [datetime.now()]
    hora_seleccionada = [None]

    horas_jornada = [f"{h:02d}:00" for h in range(8, 23)]
    grid_horarios = ft.Row(wrap=True, spacing=10, run_spacing=10)

    txt_fecha = ft.Text(
        f"Fecha: {fecha_seleccionada[0].strftime('%d/%m/%Y')}",
        size=18,
        weight=ft.FontWeight.BOLD,
    )
    txt_estado_reserva = ft.Text("", size=14, color=ft.Colors.GREEN)

    def actualizar_horarios():
        grid_horarios.controls.clear()
        clave_fecha = fecha_seleccionada[0].strftime("%Y-%m-%d")
        horas_ocupadas = RESERVAS_GUARDADAS.get(clave_fecha, [])

        for hora in horas_jornada:
            esta_ocupada = hora in horas_ocupadas
            esta_seleccionada = hora == hora_seleccionada[0]

            if esta_ocupada:
                color_bg = ft.Colors.RED_900
                color_texto = ft.Colors.WHITE_54
                deshabilitado = True
            elif esta_seleccionada:
                color_bg = "#39891a"
                color_texto = ft.Colors.WHITE
                deshabilitado = False
            else:
                color_bg = ft.Colors.SURFACE_CONTAINER_HIGHEST
                color_texto = ft.Colors.WHITE
                deshabilitado = False

            def seleccionar_hora(e, h=hora):
                hora_seleccionada[0] = h
                txt_estado_reserva.value = f"Hora seleccionada: {h}"
                actualizar_horarios()
                page.update()

            grid_horarios.controls.append(
                ft.Container(
                    content=ft.Text(
                        hora, color=color_texto, weight=ft.FontWeight.BOLD
                    ),
                    bgcolor=color_bg,
                    padding=12,
                    border_radius=8,
                    disabled=deshabilitado,
                    on_click=seleccionar_hora if not esta_ocupada else None,
                )
            )

    def cambiar_fecha(e):
        if e.control.value:
            fecha_seleccionada[0] = e.control.value
            txt_fecha.value = (
                f"Fecha: {fecha_seleccionada[0].strftime('%d/%m/%Y')}"
            )
            hora_seleccionada[0] = None
            txt_estado_reserva.value = ""
            actualizar_horarios()
            page.update()

    # Configuración de DatePicker compatible (RF-04)
    date_picker = ft.DatePicker(
        first_date=datetime.now(),
        on_change=cambiar_fecha,
    )
    page.overlay.append(date_picker)

    def abrir_calendario(e):
        date_picker.open = True
        page.update()

    def confirmar_reserva(e):
        if not hora_seleccionada[0]:
            txt_estado_reserva.value = (
                "⚠️ Por favor, selecciona una hora primero."
            )
            txt_estado_reserva.color = ft.Colors.AMBER
            page.update()
            return

        clave_fecha = fecha_seleccionada[0].strftime("%Y-%m-%d")
        if clave_fecha not in RESERVAS_GUARDADAS:
            RESERVAS_GUARDADAS[clave_fecha] = []

        RESERVAS_GUARDADAS[clave_fecha].append(hora_seleccionada[0])

        txt_estado_reserva.value = f"¡Reserva confirmada para el {fecha_seleccionada[0].strftime('%d/%m/%Y')} a las {hora_seleccionada[0]}!"
        txt_estado_reserva.color = ft.Colors.GREEN_400

        hora_seleccionada[0] = None
        actualizar_horarios()
        page.update()

    actualizar_horarios()

    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            ft.Text("Reservar Cancha", font_family="Teko", size=32),
            ft.Card(
                content=ft.Container(
                    padding=15,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            txt_fecha,
                            ft.Button(
                                "Seleccionar Fecha",
                                icon=ft.Icons.CALENDAR_MONTH,
                                on_click=abrir_calendario,
                            ),
                        ],
                    ),
                )
            ),
            ft.Text("Horarios Disponibles", size=20, font_family="Teko"),
            grid_horarios,
            txt_estado_reserva,
            ft.Button(
                "Confirmar Reserva",
                icon=ft.Icons.CHECK_CIRCLE,
                style=ft.ButtonStyle(
                    bgcolor="#39891a",
                    color=ft.Colors.WHITE,
                ),
                on_click=confirmar_reserva,
            ),
        ],
    )