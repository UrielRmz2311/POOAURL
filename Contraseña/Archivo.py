from tkinter import *
from tkinter import StringVar, IntVar


#Longitud=IntVar()

Interfaz=Tk()
Interfaz.title("Generador de contraseñas")
Interfaz.geometry("400x300")

seccion = Frame(Interfaz,width=400,height=300)
seccion.pack()
seccion.config(bg ="lightblue")
seccion.config(relief="sunken")
seccion.config(bd=25)

seccion2= Frame(Interfaz,bg="lightblue") #bg es opcional
seccion2.pack(expand=True, fill='both')

seccion3= Frame(Interfaz,bg="lightblue") #bg es opcional
seccion3.pack(expand=True, fill='both')

label = Label(seccion, text="Genere su contraseña")
label.pack(anchor=CENTER)
label.config(fg="blue",    
             bg="white",  
             font=("Verdana",24)) 

Longi = Label(seccion2, text="Número de caracteres/default: ")
Longi.config(bg="lightblue")
Longi.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

#Longitud.set("")
Insertarlongi=Entry(seccion2)#textvariable=Longitud)
Insertarlongi.grid(column=2, row=0)

Carac = Label(seccion2, text="Caracter especial SI/NO: ")
Carac.config(bg="lightblue")
Carac.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

#Longitud.set("")
InsertarCarac=Entry(seccion2)#textvariable=Longitud)
InsertarCarac.grid(column=2, row=2)

Generar=Button(seccion2, text="GENERAR", bg="Blue",fg="white")
Generar.grid(column=2, row=4)


Contra = Label(seccion3, text="Su contraseña es: ")
Contra.config(bg="lightblue")
Contra.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

Contraseña=Entry(seccion3)
Contraseña.grid(column=2, row=2)

Interfaz.mainloop()
