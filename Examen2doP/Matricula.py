from tkinter import *
Interfaz=Tk()
Interfaz.title("Generador de Matricula")
Interfaz.geometry("400x400")



seccion = Frame(Interfaz,width=400,height=300)
seccion.pack()
seccion.config(bg ="lightblue")
seccion.config(relief="sunken")
seccion.config(bd=25)

seccion2= Frame(Interfaz,bg="lightblue") #bg es opcional
seccion2.pack(expand=True, fill='both')

label = Label(seccion, text="Genere su Matricula")
label.pack(anchor=CENTER)
label.config(fg="blue",    
            bg="lightblue",  
            font=("Verdana",24)) 

Interfaz.mainloop()
