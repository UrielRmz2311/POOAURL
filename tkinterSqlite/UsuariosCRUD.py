from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana=Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")


panel=ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#Pestaña1: Formulario de Usuarios
titulo= Label(pestana1,text="Registro Usuarios", fg="Blue", font=("Modern",18)).pack()

varNom= tk.StringVar()
iblNom= Label(pestana1, text="Nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varCor= tk.StringVar()
iblCor= Label(pestana1, text="Correo: ").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()

varCon= tk.StringVar()
iblCon= Label(pestana1, text="Contraseña: ").pack()
txtCon= Entry(pestana1, textvariable=varCon).pack()

btnGuardar= Button(pestana1, text="Guardar Usuario").pack()


panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuario")
panel.add(pestana4,text="Actualizar Usuario")

Ventana.mainloop()