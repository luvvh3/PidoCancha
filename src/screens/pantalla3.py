from datetime import datetime
import flet as ft
from screens.pantalla2 import RESERVAS_GUARDADAS


def pantalla3Mostrar(page: ft.Page):
    lista_reservas = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO)

    def cancelar_reserva(fecha_clave, hora):
        if (
            fecha_clave in RESERVAS_GUARDADAS
            and hora in RESERVAS_GUARDADAS[fecha_clave]
        ):
            # Cancela y libera el horario (RF-09)
            RESERVAS_GUARDADAS[fecha_clave].remove(hora)

            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Reserva de las {hora} cancelada exitosamente."),
                bgcolor=ft.Colors.RED_700,
            )
            page.snack_bar.open = True

            cargar_reservas()
            page.update()

    def cargar_reservas():
        lista_reservas.controls.clear()
        hay_reservas = False

        for fecha, horas in RESERVAS_GUARDADAS.items():
            for hora in horas:
                hay_reservas = True
                fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
                fecha_formateada = fecha_dt.strftime("%d/%m/%Y")

                tarjeta = ft.Card(
                    content=ft.Container(
                        padding=15,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Column(
                                    spacing=5,
                                    controls=[
                                        ft.Text(
                                            f"Fecha: {fecha_formateada}",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(f"Hora: {hora} hrs", size=16),
                                        ft.Container(
                                            content=ft.Text(
                                                "Estado: Activa",
                                                color=ft.Colors.GREEN_400,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                        ),
                                    ],
                                ),
                                ft.Button(
                                    "Cancelar",
                                    icon=ft.Icons.CANCEL,
                                    style=ft.ButtonStyle(
                                        color=ft.Colors.RED_400,
                                    ),
                                    on_click=lambda e,
                                    f=fecha,
                                    h=hora: cancelar_reserva(f, h),
                                ),
                            ],
                        ),
                    )
                )
                lista_reservas.controls.append(tarjeta)

        if not hay_reservas:
            lista_reservas.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    padding=40,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                ft.Icons.EVENT_BUSY,
                                size=60,
                                color=ft.Colors.WHITE_54,
                            ),
                            ft.Text(
                                "No tienes reservas activas en este momento.",
                                size=16,
                                color=ft.Colors.WHITE_70,
                            ),
                        ],
                    ),
                )
            )

    cargar_reservas()

    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            ft.Text("Mis Reservas", font_family="Teko", size=32),
            lista_reservas,
        ],
    )