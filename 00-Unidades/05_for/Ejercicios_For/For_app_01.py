import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Nombre: Alex Leonel
Apellido: Fernandez
---
Ejercicio: for_01
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        limite = 1
        
        for rango in range(limite, 6):
            alert(rango, rango)

        
       
#for rango in list(range(limite, -567000, -10)):            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()