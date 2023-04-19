from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

# Crear una instancia de tipo controlador
controlador= controlBD()

# Proceder a Guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarMercancia(varMer.get(),varPa.get())

#-------------------------------------------------------------------------
def BuscarMercancias():
    rsMercancia=controlador.consultarMercancia(varBus.get())
    
    for usu in rsMercancia:
        cadena= str(usu[0])+" "+ usu[1]+" "+ usu[2]      
    
    if (rsMercancia):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showinfo("No encontrado", "Usuario no registrado en la BD")
#-------------------------------------------------------------------------
#def ConsultarRegistros():
 #   Registrados = controlador.consultarUsuarios()
  #  tabla.delete(*tabla.get_children())
   # for user in Registrados:
    #    tabla.insert("", tk.END, text = "", values = user)
#-------------------------------------------------------------------------      
#def ejecutaModificar():
 #   rsUsuario = controlador.consultaUsuario(varid.get())
  #  if(rsUsuario):
   #     controlador.modificarRegistro(varid.get(), varNombre.get(), varCorreo.get(), varContra.get())
    #else:
     #   messagebox.showinfo("No encontrado", "Usuario no registardo en la BD")
#--------------------------------------------------------------------------
#def ejecutaEliminar():
 #   sel = messagebox.askyesno("Elimiar Usuario", "Seguro que desea eliminar el usuario?")
  #  if (sel == True):
        
   #     try:
    #        controlador.eliminarUsuario(ID.get())
     #   except sqlite3.OperationalError:
      #      print("Error Consulta")
#------------------------------------------------------------------------------
#def ejecutaBuscar():
 #   rsUsuario = controlador.consultaUsuario(ID.get())
    
  #  txtusu.delete("1.0", "end")
   # for usu in rsUsuario:
    #    cadena = str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])
    
    #if(rsUsuario):
     #   txtusu.insert("0.0", cadena)
    #else:
     #   messagebox.showinfo("Error!!", "El usuario no esta registrado en la BD")
#-------------------------------------------------------------------------------

Ventana=Tk()
Ventana.title("Importaciones Mercancia")
Ventana.geometry("500x300")


panel=ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)

#Pestaña1: Formulario de Usuarios ------------------------------------------------------------
titulo= Label(pestana1,text="Registro de Mercancia", fg="Blue", font=("Arial",18)).pack()

varMer= tk.StringVar()
iblMer= Label(pestana1, text="Mercancia: ").pack()
txtMer= Entry(pestana1, textvariable=varMer).pack()

varPa= tk.StringVar()
iblPa= Label(pestana1, text="Pais: ").pack()
txtPa= Entry(pestana1, textvariable=varPa).pack()

btnGuardar= Button(pestana1, text="Guardar Mercancia", command=ejecutaInsert).pack()
#Pestaña2: Eliminar Registros -----------------------------------------------------------------
titulo5 = Label(pestana2, text = "Eliminar Mercancia", fg = "red", font = ("Arial", 18)).pack()
 
ID= tk.StringVar()
lblID= Label(pestana2, text = "Pais de Mercancia: ").pack()
txtID= Entry(pestana2, textvariable = ID).pack()

btnBuscar = Button(pestana2, text = "Buscar").pack()

usuarioRe = Label(pestana2, text = "Mercancia Registrada:", fg = "blue", font = ("Arial", 18)).pack()
txtusu = tk.Text(pestana2, height = 2, width = 52)
txtusu.pack()

btnBusqueda = Button(pestana2, text = "Eliminar").pack()

#Pestaña2: Buscar Mercancia---------------------------------------------------------------------

titulo2= Label(pestana3,text="Buscar Mercancia", fg="black", font=("Arial",18)).pack()

varBus= tk.StringVar()
iblid= Label(pestana3, text="Pais de Mercancia: ").pack()
txtid= Entry(pestana3, textvariable=varBus).pack()
btnBusqueda= Button(pestana3, text="Buscar", command=BuscarMercancias).pack()

subBus= Label(pestana3,text="Mercancia Registrada:", fg="Blue",font=("Arial",15)).pack()
textBus=tk.Text(pestana3,height=5, width=52)
textBus.pack()
#----------------------------------------------------------------------------------------------

panel.add(pestana1,text="Insertar Mercancia")
panel.add(pestana2,text="Eliminar Mercancia")
panel.add(pestana3,text="Buscar Mercancia")


Ventana.mainloop()