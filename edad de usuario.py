
edad = int(input("Ingresa la edad:"))
permiso_padres = input("¿Tienes permiso de tus padres?")
if edad>=18:
    print("Ingreso permitido")
elif edad>16 and edad < 18 and permiso_padres.casefold() == "si":
    print("Ingreso permitido")
else:
    print("Ingreso denegado")