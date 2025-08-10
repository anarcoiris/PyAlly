from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
    # GUI
import tkinter as tk
from tkinter import simpledialog

def pedir_datos():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    url_login= simpledialog.askstring("Login", "Introduce la url del login:")
    url_curso = simpledialog.askstring("Login", "Introduce la url principal:")
    usuario = simpledialog.askstring("Login", "Introduce tu usuario:")
    contrasena = simpledialog.askstring("Login", "Introduce tu contraseña:", show="*")

    return usuario, contrasena, url_login, url_curso

# Setup.INIT
USUARIO, CONTRASENA, URL_LOGIN, URL_CURSO = pedir_datos()
print("Usuario introducido:", USUARIO)
print("Contraseña introducida:", "*" * len(CONTRASENA))
print("URL de login:", URL_LOGIN)
print("URL del curso:", URL_CURSO)

# Configurar Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)

def comprobar_conexion():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def sesion_activa():
    """
    Devuelve True si en la página del curso NO aparece el formulario de login.
    """
    driver.get(URL_CURSO)
    time.sleep(2)
    # Buscamos si hay un input con name="username"
    try:
        driver.find_element(By.NAME, "username")
        return False  # Encontramos el login → no hay sesión
    except:
        return True   # No hay formulario → sesión activa

def iniciar_sesion():
    driver.get(URL_LOGIN)
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys(USUARIO)
    driver.find_element(By.NAME, "password").send_keys(CONTRASENA)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    print("✅ Sesión iniciada")
    time.sleep(3)
    driver.get(URL_CURSO)
    print("✅ Página del curso abierta")

# Primer login
iniciar_sesion()

# Mantener abierto
while True:
    time.sleep(240)
    if not comprobar_conexion():
        print("⚠ Sin conexión a internet. Reintentando...")
        continue

    if not sesion_activa():
        print("⚠ Sesión expirada. Iniciando de nuevo...")
        iniciar_sesion()
    else:
        print("✅ Sesión activa. Todo correcto.")
