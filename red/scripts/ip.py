import socket

def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)
        return hostname[0]
    except socket.herror:
        return "No se pudo encontrar el nombre de host para la dirección IP proporcionada."

def get_ip_address(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print("La dirección IP para", hostname, "es:", ip)
    except socket.gaierror as e:
        print("Error al obtener la dirección IP:", e)

if __name__ == "__main__":
    print("¿Qué operación desea realizar?")
    print("1. Obtener el hostname dado una dirección IP.")
    print("2. Obtener la dirección IP dado un hostname.")
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "1":
        ip_address = input("Ingrese la dirección IP: ")
        print("El nombre de host para la dirección IP", ip_address, "es:", get_hostname(ip_address))
    elif opcion == "2":
        hostname = input("Ingrese el hostname: ")
        get_ip_address(hostname)
    else:
        print("Opción no válida. Por favor, ingrese 1 o 2 para seleccionar la operación.")
