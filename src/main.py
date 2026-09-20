import flet as ft
from screens.pantalla1 import pantalla1Mostrar
from screens.pantalla2 import pantalla2Mostrar
from screens.pantalla3 import pantalla3Mostrar

def main(page: ft.Page):

    page.fonts = {
        "Teko": "TekoroDemo-BlackItalic.otf"
    }

    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.LIGHT_GREEN_800,
        navigation_bar_theme=ft.NavigationBarTheme(
            label_text_style={
                ft.ControlState.DEFAULT: ft.TextStyle(color=ft.Colors.WHITE),
                ft.ControlState.SELECTED: ft.TextStyle(color=ft.Colors.WHITE),
            },
        )
    )

    page.update()

    header = ft.AppBar(
        title=ft.Text(
            "Pido Cancha", 
            font_family="Teko",
            size=40
        ),
        center_title=True,
    )

    contenido=ft.Container(
        expand=True,
        padding=20
    )

    contenido.content=pantalla1Mostrar()

    def cambiarPantalla(e):
        id=e.control.selected_index
        if id==0:
            contenido.content=pantalla2Mostrar(page)
        elif id==1:
            contenido.content=pantalla1Mostrar()
        elif id==2:
            contenido.content=pantalla3Mostrar(page)

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
            )
        ],
        bgcolor="#193f0a",
        indicator_color="#141414",
        
    )
   
    page.add(
       header,
       contenido
    )


if __name__ == "__main__":
    ft.run(main)
