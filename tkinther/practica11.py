from tkinter import Tk, Button ,Frame, messagebox

def mostrarMensajes():
    messagebox.showinfo("showinfo", "Presionaste el Botón Azul")




#1. Instanciamos el objeto ventana

ventana= Tk()
ventana.title("Ejemplo de Frames")
ventana.geometry("600x400")

#2. Agregamos los Frames

seccion1= Frame(ventana,bg="blue") #bg es opcional
seccion1.pack(expand=True, fill='both')

seccion2= Frame(ventana,bg="gray") #bg es opcional
seccion2.pack(expand=True, fill='both')

seccion3= Frame(ventana,bg="pink") #bg es opcional
seccion3.pack(expand=True, fill='both')

#3. Agregamos botones
botonAzul=Button(seccion1,text="Botón Azul",bg="blue",fg="white", command=mostrarMensajes)
botonAzul.place(x=60, y=60)

botonAmarillo=Button(seccion2,text="Botón Amarillo",bg="Yellow")
botonAmarillo.grid(row= 0, column=0)

botonNegro=Button(seccion2,text="Botón Negro",bg="black",fg="white")
botonNegro.grid(row = 1, column=1)

botonVerde=Button(seccion3,text="Botón Verde",bg="green", fg="white")
botonVerde.configure(height=2 , width=10)
botonVerde.pack()

#Llamamos al Main
ventana.mainloop()