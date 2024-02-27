import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Alex Leonel
Apellido: fernandez
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        contador_positivos = 0
        contador_negativos = 0
        acumulador_positivos = 0
        acumulador_negativos = 0
        acumulador_ceros = 0
        maximo = 0
        minimo = 0
        
        while True:
            numero = prompt("", "Ingrese numeros")
            if numero == None:
                break
            numero = int(numero)

            if numero > 0:
                contador_positivos += numero
                acumulador_positivos += 1

            if numero < 0:
                contador_negativos += numero
                acumulador_negativos += 1

            if numero == 0:
                acumulador_ceros += 1

            if numero > maximo or contador == 0:
                maximo = numero

            if numero < minimo or contador == 0:
                minimo = numero

            contador =+ 1

        Diferencia = acumulador_positivos - acumulador_negativos

        mensaje = f"Suma de positivos: {contador_positivos}. Cantidad de positivos: {acumulador_positivos}. Suma de negativos: {contador_negativos}. Cantidad de negativos: {acumulador_negativos}. Cantidad de ceros: {acumulador_ceros}. Deferencia entre Negarivos y Positivos: {Diferencia}. Numero máximo: {maximo}. Numero mínimo: {minimo}"
                

        alert("Resultados", mensaje)

    #El maximo valor
    #El minimo valor (incluyendo en que interacion se encontro, solo la primera)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
