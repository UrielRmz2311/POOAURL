from tkinter import messagebox
import sqlite3
import bcrypt

class controlBD:
    
    def __init__(self):
        pass
    
    # Preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("D:/canel/Documents/GitHub/POOAURL/Examen3erParcial/BDImportaciones.db")
            print("Conectado BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    # Metodo para Insertar
    def guardarMercancia(self,mer,pa):
        # 1. Llamar a la conexion
        conx=self.conexionBD()
        
        # 2. Revisar que los parametros no esten vacios     
        if(mer == "" or pa == ""):
            messagebox.showwarning("Aguas!!!","Ingresa los datos")
            conx.close()
        else:
            #3. Preparar los datos y el querySQL
            cursor= conx.cursor()
            datos=(mer,pa)
            qrInsert="insert into TB_Europa(Mercancia,Pais) values(?,?)"
            
            #4. Proceder a Insertar y cerramos la conx conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Se guardo la Mercancia")
            
    # Metodo para buscar Mercancia ---------------------------------
    def consultarMercancia(self,pa):
            #1. Preparar la conexión
            conx= self.conexionBD()
            
            #2. Verificar el ID no este vació
            if(pa == ""):
                messagebox.showwarning("Error ","Ingresa el Pais")
            else:
            #3. Proceder a buscar
                try:
                    #4. Prepara lo necesario para el select
                    cursor= conx.cursor()
                    sqlSelect= "select IDImpo, Mercancia, Pais from TB_Europa where Pais="+pa
                    
                    #5. Ejecución y guardado de la consulta
                    cursor.execute(sqlSelect)
                    RSusuario= cursor.fetchall()
                    conx.close()
                    
                    return RSusuario
                    
                except sqlite3.OperationalError:
                    print("Error Consulta") 
    #Metodo para eliminar ususario
    def eliminarUsuario(self, id):
        conx = self.conexionBD()
        
        if(id == ""):
            messagebox.showwarning("Cuidado", "Favor de llenar el campo con una ID")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlDelete = "DELETE FROM TB_Europa WHERE IDImpo=?"
                
                cursor.execute(sqlDelete, [id])
                eliminarusu = cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito!!", "La mercancia fue eliminada")
                
                return eliminarusu
            
            except sqlite3.OperationalError:
                print("Error Consulta")
      #
    def consultaUsuario(self,id):
        #1. Preparar la conexión
        conx= self.conexionBD()
        
        #2. Verificar el ID no este vació
        if(id == ""):
            messagebox.showwarning("Error ","Rellena el registro ID")
        else:
        #3. Proceder a buscar
            try:
                #4. Prepara lo necesario para el select
                cursor= conx.cursor()
                sqlSelect= "select * from TB_Europa where IDImpo="+id
                
                #5. Ejecución y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error Consulta") 