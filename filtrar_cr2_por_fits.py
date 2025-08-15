import os

# Ruta a la carpeta donde están los archivos
carpeta = "./"  # Cambia si lo necesitas

# Modo seguro: True = solo muestra qué haría, False = borra de verdad
modo_seguro = False

# Extrae los nombres base de los .CR2.fits (por ejemplo: IMG_0001.CR2)
nombres_conservados = {
    os.path.splitext(f)[0]  # Elimina solo ".fits"
    for f in os.listdir(carpeta)
    if f.lower().endswith(".fits")
}

# Borrar .CR2 que no tengan un .CR2.fits correspondiente
cr2_borrados = 0
for archivo in os.listdir(carpeta):
    if archivo.lower().endswith(".cr2"):
        nombre_base = archivo  # No quitamos extensión, porque el .fits la tiene
        if nombre_base not in nombres_conservados:
            ruta_completa = os.path.join(carpeta, archivo)
            if modo_seguro:
                print(f"[SIMULACIÓN] Se borraría: {archivo}")
            else:
                os.remove(ruta_completa)
                print(f"🗑️ Borrado: {archivo}")
                cr2_borrados += 1

if modo_seguro:
    print("\n✅ Modo seguro activado. No se ha borrado nada.")
else:
    print(f"\n✅ Proceso terminado. Se borraron {cr2_borrados} archivos .CR2.")
