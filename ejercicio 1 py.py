contrasena_correcta = "admin123"
contrasena_ingresada = input("Ingrese la contraseña: ")

if contrasena_ingresada == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")