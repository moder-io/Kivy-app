import os
from cryptography.fernet import Fernet


def cargar_clave():
    claves = []
    for i in range(1, 4):
        with open(f'password/clave{i}.key', 'rb') as clave_archivo:
            claves.append(clave_archivo.read())
    return claves

 
def desencriptar_archivo(archivo_enc3, claves):
    cifrador_3 = Fernet(claves[2])
    try:
        with open(archivo_enc3, 'rb') as archivo_entrada_3:
            datos_enc3 = archivo_entrada_3.read()
        datos_descifrados_3 = cifrador_3.decrypt(datos_enc3)
        with open(f'{archivo_enc3[:-4]}_desencriptado.enc2', 'wb') as archivo_salida_3:
            archivo_salida_3.write(datos_descifrados_3)
    except Exception as e:
        print(f"Error al descifrar el archivo encriptado con la tercera clave: {str(e)}")

    cifrador_2 = Fernet(claves[1])
    try:
        with open(f'{archivo_enc3[:-4]}_desencriptado.enc2', 'rb') as archivo_entrada_2:
            datos_enc2 = archivo_entrada_2.read()
        datos_descifrados_2 = cifrador_2.decrypt(datos_enc2)
        with open(f'{archivo_enc3[:-4]}_desencriptado.enc1', 'wb') as archivo_salida_2:
            archivo_salida_2.write(datos_descifrados_2)
        os.remove(f'{archivo_enc3[:-4]}_desencriptado.enc2')
    except Exception as e:
        print(f"Error al descifrar el archivo encriptado con la segunda clave: {str(e)}")

    cifrador_1 = Fernet(claves[0])
    try:
        with open(f'{archivo_enc3[:-4]}_desencriptado.enc1', 'rb') as archivo_entrada_1:
            datos_enc1 = archivo_entrada_1.read()
        datos_descifrados_1 = cifrador_1.decrypt(datos_enc1)
        with open(f'{archivo_enc3[:-4]}', 'wb') as archivo_salida_1:
            archivo_salida_1.write(datos_descifrados_1)
        os.remove(f'{archivo_enc3[:-4]}_desencriptado.enc1')
        os.remove(archivo_enc3)
    except Exception as e:
        print(f"Error al descifrar el archivo encriptado con la primera clave: {str(e)}")


def desencriptar_carpeta(ruta_carpeta, clave):
    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_archivo) and ruta_archivo.endswith('.enc'):
            desencriptar_archivo(ruta_archivo, clave)
        elif os.path.isdir(ruta_archivo):
            desencriptar_carpeta(ruta_archivo, clave)


if __name__ == "__main__":
    clave = cargar_clave()
    carpeta_a_desencriptar = '' #pon tu carpeta
    desencriptar_carpeta(carpeta_a_desencriptar, clave)
