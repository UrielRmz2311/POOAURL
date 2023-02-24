from Personaje import *

#1. Solicitar datos.
print("")
print("####### Datos Heroe #")
especieH=input("Escribe la especie del Heroe: ")
nombreH=input("Escribe el nombre del Heroe: ")
alturaH= float(input("Escribe la altura del Heroe: "))
recargaH= int(input("Cuantas Balas recargas al Heroe: "))

print("")
print("####### Datos Villano #")
especieV=input("Escribe la especie del Villano: ")
nombreV=input("Escribe el nombre del Villano: ")
alturaV= float(input("Escribe la altura del Villano: "))
recargaV= int(input("Cuantas Balas recargas al Villano: "))


#2. Definimos los objetos
heroe= Personaje(especieH,nombreH,alturaH)
villano=Personaje(especieV,nombreV,alturaV)

#3. Usar atributos y métodos

print("")
print("####### Objeto Heroe #")
print("El personaje se llama: "+ heroe.getNombre())
print("Pertenece a la especie: "+ heroe.getEspecie())
print("Y tiene una altura de: "+ str(heroe.getAltura())) #str por que float es una cadena

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

print("")
print("####### Objeto Villano #")
print("El personaje se llama: "+ villano.getNombre())
print("Pertenece a la especie: "+ villano.getEspecie())
print("Y tiene una altura de: "+ str(villano.getAltura()))

villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)