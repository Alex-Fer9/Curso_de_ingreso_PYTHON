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
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (MASCULINO - FEMENINO - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género MASCULINO que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero FEMENINO que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.


'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True
        contador_masc_iotIA = 0
        contador_iot = 0
        contador_ia = 0
        contador_rvra = 0
        contador_masc = 0
        contador_fem = 0
        contador_otro = 0 
        contador_iot_edad = 0
        contador_fem_ia = 0
        acumulador_fem_edad_ia = 0
        bandera_edad = False
        minima_edad = 0
        lista = 0

        while seguir == True:
            if seguir == None:
                break
            
            nombre = prompt("n", "nombre")
            edad = prompt("e", "edad")
            edad = int(edad)
            
            while edad < 18:
                edad = prompt("error", "edad")
                edad = int(edad)
            
            genero = prompt("g", "genero")
            while genero != "MASCULINO" and genero != "FEMENINO" and genero != "OTRO":
                genero = prompt("error", "genero")
            
            tecnologia = prompt("t", "tecnologia")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("error", "tecnologia")

            
            match tecnologia:
                case "IOT":
                    contador_iot += 1
                    if 18 < edad < 25 or 33 < edad < 42:
                        contador_iot_edad += 1
                case "IA":
                    contador_ia += 1
                case "RV/RA":
                    contador_rvra += 1
                    if bandera_edad == False or edad < minima_edad:
                        minima_edad = edad
                        bandera_edad = True
            
            match genero:
                case "MASCULINO":
                    contador_masc += 1
                    if tecnologia == "IA" or tecnologia == "IOT" and 25 <= edad <= 50:
                        contador_masc_iotIA += 1
                case "FEMENINO":
                    contador_fem += 1
                    if tecnologia == "IA":
                        contador_fem_ia += 1
                        acumulador_fem_edad_ia += edad
                case _:
                    contador_otro += 1
            
            lista += f"{nombre} - {edad} - {genero} - {tecnologia}\n"
                        
            seguir = question("Datos cargados", "¿Continuar?")

        if contador_ia > contador_iot and contador_ia > contador_rvra:
            mensaje = "El mas votado es IA"
        elif contador_iot > contador_ia and contador_iot > contador_rvra:
            mensaje = "El mas votado es IOT"
        else:
            mensaje = "el mas votado es RV/RA"

        total_empleados = contador_masc + contador_fem + contador_otro
        porciento_masc = (contador_masc / 100) / total_empleados
        porciento_fem = (contador_fem / 100) / total_empleados
        porciento_otro = (contador_otro / 100) / total_empleados

        porciento_iot_edad = (contador_iot_edad * 100) / contador_iot

        if edad > 0:
            promedio_fem_edad_ia = acumulador_fem_edad_ia / contador_fem_ia
        else:
            alert("error", "La edad ingresada no exite")

        print(f"La contidad de empleados masculinos de 25 a 30 años que votaron IA y IOT: {contador_masc_iotIA}")
        print(mensaje)
        print(f"Porcentaje por cada genero: Masculino: {porciento_masc}%. Femenino: {porciento_fem}%. Otro: {porciento_otro}%")
        print(f"El porcentaje de los que votaron IOT entre 18-25 y 33-42 es del {porciento_iot_edad}%")
        print(f"La edad promedio femenina que votaron IA es: {promedio_fem_edad_ia}")
        print(lista)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
