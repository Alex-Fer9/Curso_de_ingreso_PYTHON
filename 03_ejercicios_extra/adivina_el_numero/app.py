import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
 el juego con un mensaje similar a este: 

“Ganaste en X intentos”.
de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.numero_secreto = random.randint(1, 100)
        self.numero_intento = 0


    def btn_mostrar_on_click(self):
        numero = self.txt_numero.get()
        numero = int(numero)
        numero_random = random.randint(1, 100)

        
        if numero < numero_random:
            alert("Aún falta", "Se quedó corto")
        elif numero > numero_random:
            alert("Ups!", "Se pasó del numero")
        else:
            alert("El juego terminó", f"Ganaste en x intentos")

        self.txt_numero.delete(0, "end")

        
        
        

if __name__ == "__main__":
    app = App() 
    app.geometry("300x300")
    app.mainloop()