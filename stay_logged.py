import webbrowser
import time
import requests

# URL de tu curso
URL_CURSO = "https://hdnfmad.grupohedima.com/course/view.php?id=227"  # <-- pon aquí la URL real

# Cada cuántos segundos comprobar (ej: 5 minutos)
INTERVALO = 300

def comprobar_conexion():
    try:
        requests.get("https://hdnfmad.grupohedima.com/course/view.php?id=227", timeout=5)
        return True
    except requests.ConnectionError:
        return False

print("Iniciando script para mantener acceso al curso...")
webbrowser.open(URL_CURSO)

while True:
    if not comprobar_conexion():
        print("⚠ No hay conexión a internet, esperando...")
    else:
        print("✅ Conexión activa, asegurando acceso al curso...")
        # Vuelve a abrir la página (no cierra pestañas previas)
        webbrowser.open(URL_CURSO)
    time.sleep(INTERVALO)
