import random
class contraseña():

    def __init__(self,Longi,Carac):
        self.Longi = Longi
        self.Carac = Carac  
        
    def GenerarContra (self,Longitud, Caracter):  
          
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
        print(Contraseña)
        