import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Alex Leonel
Apellido: fernandez
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Numero", "ingrese un número")
        numero = int(numero)
        contador_pares = 0

        for i in range(2, numero, +2):
            print(i)
            contador_pares += 1

        print(f"Los pares encontrador son {contador_pares}")

        


            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()