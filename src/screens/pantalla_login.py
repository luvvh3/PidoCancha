import flet as ft


def pantallaLogin(page: ft.Page, auth, al_autenticar):
    """
    auth: instancia de FirebaseAuth
    al_autenticar: callback que se ejecuta cuando el login es exitoso
    """

    txt_email = ft.TextField(
        label="Correo",
        prefix_icon=ft.Icons.EMAIL,
        keyboard_type=ft.KeyboardType.EMAIL,
        border_radius=10,
        width=320,
    )
    txt_pass = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=10,
        width=320,
    )
    txt_msg = ft.Text("", size=13, color=ft.Colors.RED_400)
    cargando = ft.ProgressRing(visible=False, width=20, height=20)

    def hacer_login(e):
        txt_msg.value = ""
        if not txt_email.value or not txt_pass.value:
            txt_msg.value = "Completa todos los campos."
            page.update()
            return

        cargando.visible = True
        page.update()

        ok, msg = auth.login(txt_email.value.strip(), txt_pass.value)

        cargando.visible = False
        if ok:
            al_autenticar()   # redirige a la app principal
        else:
            txt_msg.value = msg
            page.update()

    def hacer_registro(e):
        txt_msg.value = ""
        if not txt_email.value or not txt_pass.value:
            txt_msg.value = "Completa todos los campos."
            page.update()
            return

        cargando.visible = True
        page.update()

        ok, msg = auth.registrar(txt_email.value.strip(), txt_pass.value)

        cargando.visible = False
        if ok:
            al_autenticar()
        else:
            txt_msg.value = msg
            page.update()

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        spacing=15,
        controls=[
            ft.Icon(ft.Icons.SPORTS_SOCCER, size=80, color="#39891a"),
            ft.Text("Pido Cancha", font_family="Teko", size=42),
            ft.Text("Inicia sesión para continuar", size=14, color=ft.Colors.GREY_600),
            txt_email,
            txt_pass,
            cargando,
            txt_msg,
            ft.Button(
                "Iniciar Sesión",
                icon=ft.Icons.LOGIN,
                width=320,
                style=ft.ButtonStyle(bgcolor="#39891a", color="white"),
                on_click=hacer_login,
            ),
            ft.TextButton(
                "¿No tienes cuenta? Regístrate",
                on_click=hacer_registro,
            ),
        ],
    )