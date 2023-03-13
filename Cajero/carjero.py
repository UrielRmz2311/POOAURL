import tkinter as tk
from tkinter import messagebox

saldo=800

Login=tk.Tk()
Inicio=tk.Tk()
Consultar=tk.Tk()
Ingresar=tk.Tk()
Retirar = tk.Tk()
Depositar=tk.Tk()
Consultar.iconify()
Ingresar.iconify()
Retirar.iconify()
Depositar.iconify()
Inicio.iconify()

Login.title("Inicio de sesión Cajero popular")
usuario=tk.StringVar()
contraseña=tk.StringVar()
tk.Entry(Login, textvariable=usuario).place(x=130, y=70)
tk.Entry(Login, textvariable= contraseña, show="*").place(x=130,y=110)
tk.Label(Login, text="Iniciar Sesión").place(x=170, y=40)
tk.Label(Login, text="No. Cuenta: ").place(x=50, y=70)
tk.Label(Login, text="Contraseña: ").place(x=50,y=110)
Login.geometry("400x400")
def validar_inicio():
    Usu=usuario.get()
    Con=contraseña.get()
    usuario_def="121040722"
    contraseña_def="12345"
    if(usuario_def==Usu and contraseña_def== Con):
        messagebox.showinfo("Acceso permitido","Bienvenido de vuelta!!!")
        inicio()
    else:
        messagebox.showerror("ERROR!!!","Usuario incorrecto, Revise sus credenciales")
tk.Button(Login, text="Acceder", command=validar_inicio).place(x=170, y=150)
Inicio=tk.Tk()
Inicio.iconify()

#Inicio
def inicio():
    Inicio.deiconify()
    Login.iconify()
    Inicio.title("Cajero Popular")
    Inicio.geometry("400x400")
    tk.Label(Inicio, text="Inicio").place(x=170,y=40)
    tk.Button(Inicio,text="Consultar", command=consultas).place(x=170, y=80)
    tk.Button(Inicio, text="Ingresar").place(x=170,y=120)
    tk.Button(Inicio,text="Retirar", command=retirar).place(x=170,y=160)
    tk.Button(Inicio, text="Depositar",command=depositar).place(x=170,y=200)
    tk.Button(Inicio, text="Cerrar sesión", command=regresar_login).place(x=170, y=240)
    Depositar = tk.Tk()
    Depositar.iconify()
#Consultar
def consultas():
    Consultar.deiconify()
    Inicio.iconify()
    Consultar.title("Consultar")
    Consultar.geometry("400x200")
    tk.Label(Consultar, text="Consultar").place(x=100, y=30)
    def consultar():
        tk.Label(Consultar, text="Su saldo actual es de: "+ " $ " + str(saldo), bg="red",fg="white").place(x=50, y=50)
    tk.Button(Consultar, text="Consultar", command=consultar).place(x=100, y=100)
    tk.Button(Consultar, text="Regresar", command=volver_inicio).place(x=0, y=0)
#Retirar
def retirar():
    Retirar.deiconify()
    Inicio.iconify()
    ingreso= tk.IntVar()
    Retirar.title("Retirar")
    Retirar.geometry("400x400")
    tk.Label(Retirar,text="Retirar").place(x=100,y=30)
    tk.Entry(Retirar, textvariable=ingreso).place(x=50, y=50)
    ingresomo= ((saldo)-(ingreso))
    def mostrar():
        tk.Label(Retirar, text="Ah Retirado Dinero con exito").place(x=100,y=150)
    tk.Label(Retirar, textvariable=ingresomo).place(x=100,y=200)
    tk.Button(Retirar, text="Retirar", command=mostrar).place(x=100,y=100)
    tk.Button(Retirar, text="Regresar",command=volver_inicio).place(x=0, y=0)
    tk.mainloop()
#Depositar
def depositar():
    Depositar.deiconify()
    Inicio.iconify()
    ingresod=tk.IntVar()
    Beneficiario=tk.StringVar()
    cuenta=tk.IntVar()
    edad= tk.IntVar()
    
    Depositar.title("Depositar")
    Depositar.geometry("400x400")
    tk.Label(Retirar, text="Retirar").place(x=100,y=30)
    tk.Label(Depositar, text="Depositar").place(x=100,y=30)
    
    tk.Label(Depositar,text="No.Cuenta: ").place(x=60,y=70)
    tk.Entry(Depositar, textvariable=cuenta).place(x=200, y=70)
    
    tk.Label(Depositar,text="Nombre Beneficiario: ").place(x=50,y=110)
    tk.Entry(Depositar, textvariable=Beneficiario).place(x=200, y=110)
    
    tk.Label(Depositar,text="Edad del Beneficiario: ").place(x=48,y=150)
    tk.Entry(Depositar, textvariable=edad).place(x=200, y=150)
    
    tk.Label(Depositar,text="Cantidad a Depositar: ").place(x=52,y=200)
    tk.Entry(Depositar, textvariable=ingresod).place(x=200,y=200)
    ingresomo=ingresod
    
    def mostrar():
        tk.Label(Depositar, textvariable=ingresomo).place(x=100,y=200)
        if ingresomo==None:
            messagebox.showerror("ERROR!!!","No se registro ninguna cantidad")
        else: 
            tk.Label(Depositar, text="Tu deposito se realizo Correctamente").place(x=100, y=300)
    tk.Button(Depositar,text="Depositar", command=mostrar).place(x=110, y=250)
    tk.Button(Depositar, text="Regresar", command=volver_inicio).place(x=0,y=0)

#Regresar al login
def regresar_login():
    Login.deiconify()
    Inicio.iconify()
    
#Regresar al Inicio
def volver_inicio():
    Depositar.iconify()
    Consultar.iconify()
    Retirar.iconify()
    Inicio.deiconify()
tk.mainloop()