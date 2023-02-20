class Personaje:
    #atributos Personaje
    especie= "Humano"
    nombre= "Mater chief"
    altura= "2.70"
    
    #metodos Personaje
    def correr(self,status):
        if(status):
            print("el personaje" +self.nombre " esta corriendo")
        else:
            print("El personaje"+ self.nombre " se detuvo")
                         
    def lanzarGranadas(self):
         print("El personaje"+ self.nombre " lanzo una granada")
           
    def recargarArma(self,municiones):
        cargador= 10
        cargador= cargador + municiones
        print("El arma tiene"+ cargador "balas")

