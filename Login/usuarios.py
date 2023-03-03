class usuario():
    numUsuarios= 0
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra
        
        self.conectado = False        
        usuario.numUsuarios+=1
    
    def validar (self, Password=None):
        if Password==None:
            Contraseña =input("Ingrese una contraseña: ")
        else:
            Contraseña=Password        
        if Contraseña == self.contra:
            print("Se conecto con exito !!")
            self.conectado =True
            return True
        else:
            print("Datos incorrectos, Revise sus credenciales")
        if Password!=None:
            return False
        else:
         print("Error, no pudo acceder")
                
    def __str__ (self):
        if self.conectado:
            conect ="Conectado"
        else:
            conect ="Desconectado"  
        return f"El usuario es {self.nombre} y está {conect}" 
