from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    # Preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("D:/canel/Documents/GitHub/POOAURL/tkinterSqlite/DBUsuarios.db")
            print("Conectado BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    # Metodo para Insertar
    def guardarUsuario(self,nom,cor,con):
        # 1. Llamar a la conexion
        conx=self.conexionBD()
        
        # 2. Revisar que los parametros no esten vacios     
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas!!!","Revisa tu formulario")
            conx.close()
        else:
            #3. Preparar los datos y el querySQL
            cursor= conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
            
            #4. Proceder a Insertar y cerramos la conx conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Se guardo el Usuario")
    
    # Encriptar contraseña
    def encriptarCon(self,con):
        conPlana= con
        conPlana= conPlana.encode() # Convierte la contraseña a byte
        sal= bcrypt.gensalt()
        conHa=bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa
                    
        