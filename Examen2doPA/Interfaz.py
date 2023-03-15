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


Label1= Label(seccion2, text="Nombre: ")
Label1.config(bg="lightblue")
Label1.place(x=10,y=40)

Label2= Label(seccion2, text="Apelido Paterno: ")
Label2.config(bg="lightblue")
Label2.place(x=10,y=80)

Label3= Label(seccion2, text="Apelido Materno: ")
Label3.config(bg="lightblue")
Label3.place(x=10,y=120)

Label4= Label(seccion2, text="Año de nacimiento: ")
Label4.config(bg="lightblue")
Label4.place(x=10,y=160)

Label5= Label(seccion2, text="Carrera: ")
Label5.config(bg="lightblue")
Label5.place(x=10,y=200)

Nom=Entry(seccion2)
Nom.place(x=170,y=40) 

AP=Entry(seccion2)
AP.place(x=170,y=80)

AM=Entry(seccion2)
AM.place(x=170,y=120)

AN=Entry(seccion2)
AN.place(x=170,y=160)

CA=Entry(seccion2)
CA.place(x=170,y=200)

Generar=Button(seccion2, text="GENERAR", bg="Blue",fg="white")
Generar.place(x=150,y=240)

Interfaz.mainloop()
