import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Alex Leonel
Apellido: fernandez
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        maximo = 0
        minimo = 0
        acumulador_edad = 0
        contador = 0
        acumulador_votos = 0

        while True:
            Nombre = prompt("Nombre", "Nombre del candidato")

            edad = prompt("Edad", "Su edad")
            edad = int(edad)
            while edad < 25:
                edad = prompt("e ", "La edad no es válida o no existe")
                edad = int(edad)
            acumulador_edad += edad
            
            votos = prompt("Votos", "Cantidad de votos que recibió")
            votos = int(votos)
            while votos < 0:
                votos = prompt("e ", "Los votos deben registrar en numeros positivos")
                votos = int(votos) 
            acumulador_votos += votos

            if votos > maximo:
                maximo = votos
                mensaje1 = f"{Nombre} fue el candidato con más votos"
            
            if votos < minimo:
                minimo = votos
                mensaje2 = f"{Nombre} de {edad} de edad fue el candidato con menos votos"

            contador += 1

            seguir = prompt("Registrado", "Si no hay más candidatos presiona 'cancelar'")
            if seguir == None:
                break
        
        promedio_edad = acumulador_edad / contador
        
        if maximo:
            mensaje1 = f"{Nombre} fue el candidato con más votos"
        
        if minimo:
            mensaje2 = f"{Nombre} de {edad} de edad fue el candidato con menos votos"
        
        alert("Informe", f"{mensaje1}. {mensaje2}. El promedio de edad de los candidatos es {promedio_edad}. El total de votos emitidos es {acumulador_votos}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
