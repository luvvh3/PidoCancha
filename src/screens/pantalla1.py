import flet as ft


def pantalla1Mostrar():
    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            # 1. Imagen principal de la cancha
            ft.Image(
                src="bg.jpg",
                border_radius=20,
                height=220,
                width=350,
                fit="cover",
            ),
            # 2. Título de la cancha
            ft.Text(
                "Cancha Maracana",
                font_family="Teko",
                size=36,
                weight=ft.FontWeight.BOLD,
            ),
            # 3. Tarjeta de información/detalles
            ft.Card(
                content=ft.Container(
                    padding=15,
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                leading=ft.Icon(
                                    ft.Icons.SPORTS_SOCCER, color="#39891a"
                                ),
                                title=ft.Text("Tipo de superficie"),
                                subtitle=ft.Text("Césped Sintético Fútbol 7"),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(
                                    ft.Icons.LOCATION_ON, color="#39891a"
                                ),
                                title=ft.Text("Ubicación"),
                                subtitle=ft.Text(
                                    "Av. Principal #123, Zona Sur"
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(
                                    ft.Icons.ATTACH_MONEY, color="#39891a"
                                ),
                                title=ft.Text("Precio por Hora"),
                                subtitle=ft.Text("120 Bs / Hora"),
                            ),
                        ]
                    ),
                )
            ),
        ],
    )