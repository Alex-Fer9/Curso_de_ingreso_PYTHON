import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random 
'''
Nombre: Alex Leonel
Apellido: fernandez
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("El juego ha comenzado!", "Elije un numero del 1 al 100. Máximo 7 intentos...")
        numero = int(numero)
        intento = 7
        numero_random = random.randint(1, 100)

        for i in range(1, intento+1): 
            if numero < numero_random:
                alert("Aún falta", "Se quedó corto")
            elif numero > numero_random:
                alert("Ups!", "Se pasó del numero")                
            else:
                break
            
            numero = prompt("Vamos de nuevo", "Elije un numero del 1 al 100")
            numero = int(numero)
        
        match i:
            case 1:
                mensaje = f"Felicidades, Al {i}° intento! Usted es un psíquico"
            case 2:
                mensaje = f"Felicidades, Al {i}° intento! Excelente percepción"
            case 3:
                mensaje = f"Felicidades, Al {i}° intento! Esto es suerte"
            case 7:
                mensaje = "Perdiste, suerte para la próxima"  
            case _:
                mensaje = f"Felicidades, Al {i}° intento! Excelente técnica"
        
        alert("El juego terminó", mensaje)
            

                

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()