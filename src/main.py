import flet as ft
from screens.pantalla_login import pantallaLogin
from screens.pantalla1 import pantalla1Mostrar
from screens.pantalla2 import pantalla2Mostrar
from screens.pantalla3 import pantalla3Mostrar
from services.auth import FirebaseAuth


def main(page: ft.Page):
    page.fonts = {"Teko": "TekoroDemo-BlackItalic.otf"}
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.LIGHT_GREEN_800)
    page.padding = 0

    auth = FirebaseAuth()
    contenido = ft.Container(expand=True, padding=20)

    # ---------- APP PRINCIPAL (post-login) ----------
    def mostrar_app():
        header = ft.AppBar(
            title=ft.Text("Pido Cancha", font_family="Teko", size=40),
            center_title=True,
            bgcolor="#193f0a",
            actions=[
                ft.IconButton(
                    icon=ft.Icons.LOGOUT,
                    tooltip="Cerrar sesión",
                    on_click=cerrar_sesion,
                )
            ],
        )

        contenido.content = pantalla1Mostrar()

        def cambiarPantalla(e):
            id = e.control.selected_index
            if id == 0:
                contenido.content = pantalla2Mostrar(page)
            elif id == 1:
                contenido.content = pantalla1Mostrar()
            elif id == 2:
                contenido.content = pantalla3Mostrar(page)
            contenido.update()

        page.bottom_appbar = ft.NavigationBar(
            selected_index=1,
            on_change=cambiarPantalla,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.ACCESS_TIME_OUTLINED,
                    selected_icon=ft.Icons.ACCESS_TIME,
                    label="Reservar",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.SPORTS_SOCCER_OUTLINED,
                    selected_icon=ft.Icons.SPORTS_SOCCER,
                    label="Cancha",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FAVORITE_BORDER,
                    selected_icon=ft.Icons.FAVORITE,
                    label="Mis Reservas",
                ),
            ],
            bgcolor="#193f0a",
            indicator_color="#141414",
        )

        page.controls.clear()
        page.add(header, contenido)
        page.update()

    def cerrar_sesion(e):
        auth.logout()
        mostrar_login()

    # ---------- LOGIN ----------
    def mostrar_login():
        page.bottom_appbar = None
        page.controls.clear()
        page.add(
            ft.Container(
                content=pantallaLogin(page, auth, mostrar_app),
                expand=True,
                padding=20,
            )
        )
        page.update()

    mostrar_login()


if __name__ == "__main__":
    ft.run(main)