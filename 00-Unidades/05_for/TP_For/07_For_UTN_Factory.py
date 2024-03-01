import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Alex Leonel
Apellido: Fernandez
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero. # 

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_NB_ASP_ssr = 0
        acumulador_M_edad = 0
        acumulador_F_edad = 0
        acumulador_NB_edad = 0
        contador_M = 0
        contador_F = 0
        contador_NB = 0
        contador = 0
        minimo_jr = 0
        contador_PYTHON = 0
        contador_JS = 0
        contador_ASP = 0

        for i in range(0, 10):
            nombre = prompt("Nombre", "Ingrese el nombre")

            edad = prompt("e", "edad")
            edad = int(edad)           
            while edad < 18:
                edad = prompt("Error", "edad")
                edad = int(edad)

            genero = prompt("Género", "Ingrese la inicial del género")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("Error", "Ingrese la SOLO inicial del género")
            
            tecnologia = prompt("Tecnología", "Ingrese la tecnología")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("Error", "Ingrese una tecnología que sea compatible")

            puesto = prompt("Género", "Ingrese la inicial del género")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("Error", "Ingrese la SOLO inicial del género")

            if puesto == "Jr":
                if edad < minimo_jr or contador == 0:
                    minimo_jr = edad

            match tecnologia:
                case "ASP.NET":
                    contador_ASP += 1
                case "JS":
                    contador_JS += 1
                case "PYTHON":
                    contador_PYTHON += 1
                               
            match genero:
                case "M":
                    contador_M += 1
                    acumulador_M_edad += edad
                case "F":
                    contador_F += 1
                    acumulador_F_edad += edad
                case _:
                    contador_NB += 1
                    acumulador_NB_edad += edad
                    if (tecnologia == "ASP.NET" or tecnologia == "JS") and 25 < edad < 40 and puesto == "Ssr":
                        contador_NB_ASP_ssr += 1

            contador += 1

        promedio_M = acumulador_M_edad / contador_M
        promedio_F = acumulador_F_edad / contador_F
        promedio_NB = acumulador_NB_edad / contador_NB

        print(f"Premodio de edad de género masculino es {promedio_M}, de femenino es {promedio_F} y no binario es {promedio_NB}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
