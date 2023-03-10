from tkinter import *
from tkinter import IntVar, messagebox
from contraseña import contraseña

Interfaz=Tk()
Longitud=IntVar()
Caracter=IntVar()
#Passw=StringVar()

contras=contraseña(Longitud,Caracter)
#contra=contraseña(Contraseña)

def createContraseña():
   
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

    Longi = Label(seccion2, text="Número de caracteres (0=default): ")
    Longi.config(bg="lightblue")
    Longi.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    Longitud.set("")
    Insertarlongi=Entry(seccion2,textvariable=Longitud)
    Insertarlongi.grid(column=2, row=0)

    Carac = Label(seccion2, text="Caracter especial (1=SI/0=NO): ")
    Carac.config(bg="lightblue")
    Carac.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

    Caracter.set("")
    InsertarCarac=Entry(seccion2,textvariable=Caracter)
    InsertarCarac.grid(column=2, row=2)

    Generar=Button(seccion2, text="GENERAR", bg="Blue",fg="white",command=generador)
    Generar.grid(column=2, row=4)


    Contra = Label(seccion3, text="Su contraseña es: ")
    Contra.config(bg="lightblue")
    Contra.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

    Password= Entry(seccion3)
    Password.grid(column=2, row=2)

    Interfaz.mainloop()
    
def generador():
    Longi = int(Longitud.get())
    Carac = int(Caracter.get())
    contras.GenerarContra(Longi,Carac)
    if Carac>1:
        messagebox.showerror("ERROR!!!"," Se registro una respuesta invalida")
    else:
        messagebox.showinfo("Exelente","Su contraseña se genero correctamente")
        
        
        
if __name__=="__main__":
    #contra1=contraseña(Caracter,Longitud)
    createContraseña()
