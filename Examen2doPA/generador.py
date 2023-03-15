import random
Nombre=str(input("Escriba su nombre: "))
ApellidoP=str(input("Escriba su apellido paterno: "))
ApellidoM=str(input("Escriba su apellido materno: "))
AñoNac=str(input("Escriba el año de nacimiento: "))
Carrera=str(input("Escriba el nombre de su carreara: "))
Añocur=str(input("Escriba el año del curso: "))

nom=Nombre[0:1]
ap=ApellidoP[0:3]
am=ApellidoM[0:3]
an=AñoNac[2:4]
anc=Añocur[2:4]
ca=Carrera[0:3]
Nume=str(random.randint(100,999))

cantidad=ca+anc+an+nom+ap+am+Nume
canti=cantidad.upper()
print(canti)