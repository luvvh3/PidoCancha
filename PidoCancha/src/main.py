import flet as ft
from screens.pantalla1 import pantalla1Mostrar
from screens.pantalla2 import pantalla2Mostrar
from screens.pantalla3 import pantalla3Mostrar

def main(page: ft.Page):

    header = ft.AppBar(
        title=ft.Text("PidoCancha"),
        center_title=True,
    )
    nav_bar = ft.NavigationBar(
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
            )
        ]
    )
   
    page.add(
       header,
       nav_bar
    )


if __name__ == "__main__":
    ft.run(main)
