class usuario():
    numUsuarios= 0
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra
        
        self.conectado = False        
        usuario.numUsuarios+=1
    
    def validar (self, Password=None, nombreusu=None):
        if (Password==None)and(nombreusu==None):
            Usuario=input("Ingrese un usuario: ")
            Contraseña =input("Ingrese una contraseña: ")
        else:
            Usuario=nombreusu
            Contraseña=Password        
        if (Contraseña == self.contra)and(Usuario == self.nombre):
            print("Se conecto con exito !!")
            self.conectado =True
            return True
        else:
            print("Datos incorrectos, Revise sus credenciales")
        if (Password!=None)and(nombreusu!=None):
            return False
        else:
         print("Error, no pudo acceder")
                
    def __str__ (self):
        if self.conectado:
            conect ="Conectado"
        else:
            conect ="Desconectado"  
        return f"El usuario es {self.nombre} y está {conect}" 
