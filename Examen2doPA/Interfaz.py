from tkinter import *
from tkinter import messagebox
import random
from generador import*

Interfaz=Tk()
Interfaz.title("Generador de Matricula")
Interfaz.geometry("400x400")

Nombre=StringVar()
ApellidoP=StringVar()
ApellidoM=StringVar()
AñoNac=StringVar()
Carrera=StringVar()
Añocur=StringVar()


def createMatricula():
    def generar():
        Cantida=Matricula(Nombre.get(),ApellidoP.get(),ApellidoM.get(), AñoNac.get(), Carrera.get(),Añocur.get())
        Cantida.GenerarMatricula()
        messagebox.showinfo("Su matricula es: ", Cantida.getMatricula())
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

    Label6= Label(seccion2, text="Año del curso: ")
    Label6.config(bg="lightblue")
    Label6.place(x=10,y=240)

    Nom=Entry(seccion2, textvariable=Nombre)
    Nom.place(x=170,y=40) 

    AP=Entry(seccion2, textvariable=ApellidoP)
    AP.place(x=170,y=80)

    AM=Entry(seccion2, textvariable=ApellidoM)
    AM.place(x=170,y=120)

    AN=Entry(seccion2, textvariable=AñoNac)
    AN.place(x=170,y=160)

    CA=Entry(seccion2,textvariable=Carrera)
    CA.place(x=170,y=200)

    ANC=Entry(seccion2,textvariable=Añocur)
    ANC.place(x=170,y=240)

    Generar=Button(seccion2, text="GENERAR", bg="Blue",fg="white", command=generar)
    Generar.place(x=150,y=280)
    Interfaz.mainloop()
    
    
    
if __name__=="__main__":
    createMatricula()