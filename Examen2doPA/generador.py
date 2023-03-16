import random

class Matricula():
    def __init__(self,Nombre,ApellidoP, ApellidoM,AñoNac, Carrera, Añocur):
        self.Nomb= Nombre
        self.AP = ApellidoP
        self.AM=ApellidoM
        self.AN=AñoNac
        self.CA= Carrera
        self.ANC=Añocur
        self.Mat=""
    def GenerarMatricula(self):
        nom=self.Nomb[0:1]
        ap=self.AP[0:3]
        am=self.AM[0:3]
        an=self.AN[2:4]
        anc=self.ANC[2:4]
        ca=self.CA[0:3]
        Nume=str(random.randint(100,999))
        

        cantidad=ca+anc+an+nom+ap+am+Nume
        canti=cantidad.upper()
        self.Mat=canti
    def getMatricula(self):
        return self.Mat