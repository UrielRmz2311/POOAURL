import random
class contraseña():

    def __init__(self,Longitud,Caracter):
        self.Longitud = Longitud
        self.Caracter = Caracter  
        
    def GenerarContra (self,Contraseña,Caracter,Longitud):  
        Longitud==self.Longitud
        Caracter==self.Caracter  
        if Longitud == 0:
            Longitud=8
        else:
            Longitud=Longitud
        if Caracter == 1:
            minus="abcdefghijklmnñopqrstuvwxyz"
            simbolos= "@#$%&[]{()}"
            Mayus= "ABCDEFQHIJKLMNÑOPQRSTUVWXYZ"
            num="1234567890"
            
            base=minus+simbolos+Mayus+num
        else:
            if Caracter ==0:
                minus="abcdefghijklmnñopqrstuvwxyz"
                base=minus
            else:
                print("ERROR!!! Se registro una respuesta invalida")
        Contra=random.sample(base,Longitud)
        Contraseña="".join(Contra)
        self.Contraseña = Contraseña
        