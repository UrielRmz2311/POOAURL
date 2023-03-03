from tkinter import Tk, Label, Frame, StringVar, Entry, Button, messagebox
from usuarios import usuario

login = Tk()
Usuario= StringVar()
Contraseña =StringVar()

def createGUI():

    #ventanapricipal
    #login = Tk()
    login.title("Login Usuario Practica No.12")
    login.geometry("600x400")

    #mainFrame
    seccion1= Frame(login,bg="white") #bg es opcional
    seccion1.pack(expand=True, fill='both')

    PedirUsu= Label(seccion1, text="Acceder a Cuenta")
    PedirUsu.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    Usu=Label(seccion1, text="Usuario: ")
    Usu.grid(column=0,row=1)
    Pass= Label(seccion1,text="Contraseña: ")
    Pass.grid(column=0, row=2)

    #Pedir entradas de datos
    
    Usuario.set("")
    InsertarUsu=Entry(seccion1,textvariable=Usuario)
    InsertarUsu.grid(column=1, row=1)

    
    Contraseña.set("")
    InsertarPass=Entry(seccion1, textvariable=Contraseña, show="*")
    InsertarPass.grid(column=1,row=2)

    #Botón
    Acceder=Button(seccion1, text="ACCEDER", bg="Blue",fg="white", command=acceder)
    Acceder.grid(column=2, row=3)
    
    login.mainloop()
    
def acceder():
    test= usuario1.conectar(Contraseña.get())
    if test:
        messagebox.showinfo("Conectado","Se accedio con exito")
    else:
        messagebox.showerror("Error","Datos incorrectos")

if __name__=="__main__":
    #usuario1= usuario(input("Ingrese un usuario: "), input("Ingrese una contraseña: ")) 
    usuario1= usuario("Alan","12345")
    createGUI()
        
