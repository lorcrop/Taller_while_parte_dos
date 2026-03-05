# INICIO
print("BIENVENIDO:)")

CONTRA= input("INGRESE LA CONTRASEÑA: ")

while CONTRA != "python123":
    print("\033[31mLA CONTRASEÑA ES INCORRECTA\033[0m")
    CONTRA = input("\033[32mIngrese la contraseña: \033[0m")

print("\033[32mLA CONTRASEÑA ES CORRECTA\033[0m")