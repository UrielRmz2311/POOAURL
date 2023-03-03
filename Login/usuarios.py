class usuario():
    numUsuarios= 0
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra
        
        self.conectado = False
        self.intentos = 3
        
        usuario.numUsuarios+=1
    
    def conectar (self, Password=None):
        if Password==None:
            Contraseña =input("Ingrese una contraseña: ")
        else:
            Contraseña=Password        
        if Contraseña == self.contra:
            print("Se conecto con exito !!")
            self.conectado =True
            return True
        else:
            self.intentos-=1
            if self.intentos > 0:
                print("Contraseña incorrecta, Revise sus credenciales")
                if Password!=None:
                    return False
                print("Intentos restantes",self.intentos)
                self.conectar()
            else:
                print("Error, no pudo acceder")
                
    def __str__ (self):
        if self.conectado:
            conect ="Conectado"
        else:
            conect ="Desconectado"  
        return f"El usuario es {self.nombre} y está {conect}" 
    
#usuario1 =usuario(input("Ingrese un usuario: "), input("Ingrese una contraseña: ")) 
#print(usuario1)
#usuario1.conectar() 
#print(usuario1)