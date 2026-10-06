import requests

API_KEY = "AIzaSyAgmgj1mcDtESx1ycLEBKoSwg0QMzYr7Ds"  # ← ponla aquí
BASE = "https://identitytoolkit.googleapis.com/v1/accounts"


class FirebaseAuth:
    def __init__(self):
        self.id_token = None
        self.email = None

    def registrar(self, email, password):
        url = f"{BASE}:signUp?key={API_KEY}"
        r = requests.post(url, json={
            "email": email,
            "password": password,
            "returnSecureToken": True
        })
        data = r.json()
        if "error" in data:
            return False, self._traducir_error(data["error"]["message"])
        self.id_token = data["idToken"]
        self.email = data["email"]
        return True, "Registro exitoso"

    def login(self, email, password):
        url = f"{BASE}:signInWithPassword?key={API_KEY}"
        r = requests.post(url, json={
            "email": email,
            "password": password,
            "returnSecureToken": True
        })
        data = r.json()
        if "error" in data:
            return False, self._traducir_error(data["error"]["message"])
        self.id_token = data["idToken"]
        self.email = data["email"]
        return True, "Login exitoso"

    def logout(self):
        self.id_token = None
        self.email = None

    @staticmethod
    def _traducir_error(codigo):
        errores = {
            "EMAIL_EXISTS": "Ese correo ya está registrado.",
            "EMAIL_NOT_FOUND": "Correo no registrado.",
            "INVALID_PASSWORD": "Contraseña incorrecta.",
            "INVALID_LOGIN_CREDENTIALS": "Correo o contraseña incorrectos.",
            "WEAK_PASSWORD": "La contraseña debe tener al menos 6 caracteres.",
            "INVALID_EMAIL": "Correo inválido.",
            "TOO_MANY_ATTEMPTS_TRY_LATER": "Demasiados intentos. Intenta más tarde.",
        }
        return errores.get(codigo, f"Error: {codigo}")