from tkinter import *
from tkinter import ttk
import tkinter as tk
from contralorBD import * # Le presentamos la clase a la ventana

# Crear una instancia de tipo controlador
controlador= controladorBD()

# Proceder a Guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#-------------------------------------------------------------------------
def Buscarusuario():
    rsUsuario=controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena= str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])      
    
    if (rsUsuario):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showinfo("No encontrado", "Usuario no registrado en la BD")
#-------------------------------------------------------------------------
def ConsultarRegistros():
    Registrados = controlador.consultarUsuarios()
    tabla.delete(*tabla.get_children())
    for user in Registrados:
        tabla.insert("", tk.END, text = "", values = user)
#-------------------------------------------------------------------------      
def ejecutaModificar():
    rsUsuario = controlador.consultaUsuario(varid.get())
    if(rsUsuario):
        controlador.modificarRegistro(varid.get(), varNombre.get(), varCorreo.get(), varContra.get())
    else:
        messagebox.showinfo("No encontrado", "Usuario no registardo en la BD")
#--------------------------------------------------------------------------
def ejecutaEliminar():
    sel = messagebox.askyesno("Elimiar Usuario", "Seguro que desea eliminar el usuario?")
    if (sel == True):
        
        try:
            controlador.eliminarUsuario(ID.get())
        except sqlite3.OperationalError:
            print("Error Consulta")
#------------------------------------------------------------------------------
def ejecutaBuscar():
    rsUsuario = controlador.consultaUsuario(ID.get())
    
    txtusu.delete("1.0", "end")
    for usu in rsUsuario:
        cadena = str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])
    
    if(rsUsuario):
        txtusu.insert("0.0", cadena)
    else:
        messagebox.showinfo("Error!!", "El usuario no esta registrado en la BD")
#-------------------------------------------------------------------------------

Ventana=Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")


panel=ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)

#Pestaña1: Formulario de Usuarios ------------------------------------------------------------
titulo= Label(pestana1,text="Registro Usuarios", fg="Blue", font=("Arial",18)).pack()

varNom= tk.StringVar()
iblNom= Label(pestana1, text="Nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varCor= tk.StringVar()
iblCor= Label(pestana1, text="Correo: ").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()

varCon= tk.StringVar()
iblCon= Label(pestana1, text="Contraseña: ").pack()
txtCon= Entry(pestana1, textvariable=varCon).pack()

btnGuardar= Button(pestana1, text="Guardar Usuario",command=ejecutaInsert).pack()

#Pestaña2: Buscar Usuario ---------------------------------------------------------------------

titulo2= Label(pestana2,text="Buscar Usuario", fg="black", font=("Arial",18)).pack()

varBus= tk.StringVar()
iblid= Label(pestana2, text="Identificador de Usuario: ").pack()
txtid= Entry(pestana2, textvariable=varBus).pack()
btnBusqueda= Button(pestana2, text="Buscar",command=Buscarusuario).pack()

subBus= Label(pestana2,text="Registrado:", fg="Blue",font=("Arial",15)).pack()
textBus=tk.Text(pestana2,height=5, width=52)
textBus.pack()

#Pestaña3: Consultar Usuarios ------------------------------------------------------------------
titulo3 = Label(pestana3, text = "Consultar Usuarios", fg = "red", font = ("Arial", 18)).pack()

columns = ("id", "nombre", "correo", "contra")
tabla = ttk.Treeview(pestana3, columns = columns, show = "headings")

tabla.column("id", anchor=tk.W, width=50)
tabla.column("nombre", anchor=tk.W, width=150)
tabla.column("correo", anchor=tk.W, width=150)
tabla.column("contra", anchor=tk.W, width=200)

tabla.heading("id", text = "ID", )
tabla.heading("nombre", text = "NOMBRE")
tabla.heading("correo", text = "CORREO")
tabla.heading("contra", text = "CONTRASEÑA")

tabla.pack()

btnConsulta = Button(pestana3, text = "Registros", command = ConsultarRegistros).pack()

#Pestaña4: Modificar Usuarios -------------------------------------------------------------------
titulo4 = Label(pestana4, text = "Modificar Usuarios", fg = "green", font = ("Arial", 18)).pack()

varid= tk.StringVar()
lblid = Label(pestana4, text = "ID del usuario: ").pack()
txtid = Entry(pestana4, textvariable = varid).pack()

varNombre= tk.StringVar()
lblNombre = Label(pestana4, text = "Nombre usuario (nuevo): ").pack()
txtNombre = Entry(pestana4, textvariable = varNombre).pack()

varCorreo= tk.StringVar()
lblCorreo= Label(pestana4, text = "Correo electronico (nuevo): ").pack()
txtCorreo = Entry(pestana4, textvariable = varCorreo).pack()

varContra= tk.StringVar()
lblContra = Label(pestana4, text = "Nueva Contraseña: ").pack()
txtContra = Entry(pestana4, textvariable = varContra, show = "*").pack()

btnmodificar= Button(pestana4, text = "Actualizar", command = ejecutaModificar).pack()

#Pestaña5: Eliminar Registros -----------------------------------------------------------------
titulo5 = Label(pestana5, text = "Eliminar Usuarios", fg = "red", font = ("Arial", 18)).pack()
 
ID= tk.StringVar()
lblID= Label(pestana5, text = "Identificador de usuario: ").pack()
txtID= Entry(pestana5, textvariable = ID).pack()

btnBuscar = Button(pestana5, text = "Buscar", command = ejecutaBuscar).pack()

usuarioRe = Label(pestana5, text = "Registrado:", fg = "blue", font = ("Arial", 18)).pack()
txtusu = tk.Text(pestana5, height = 2, width = 52)
txtusu.pack()

btnBusqueda = Button(pestana5, text = "Eliminar", command = ejecutaEliminar).pack()

#----------------------------------------------------------------------------------------------
panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuario")
panel.add(pestana4,text="Modificar Usuario")
panel.add(pestana5,text="Eliminar Usuario")

Ventana.mainloop()