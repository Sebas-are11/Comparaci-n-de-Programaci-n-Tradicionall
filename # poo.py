# Definir funciones para entrada de datos diarios y cálculo de promedio semanal

def ingresar_temperaturas_diarias():
    temperaturas = []
    for dia in range(7):
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Entrada de datos diarios y cálculo del promedio semanal
temperaturas_semana = ingresar_temperaturas_diarias()
promedio_semanal = calcular_promedio_semanal(temperaturas_semana)

print(f"Las temperaturas de la semana son: {temperaturas_semana}")
print(f"El promedio semanal de temperaturas es: {promedio_semanal}")




class InformacionClimatica:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperatura_diaria(self):
        temp = float(input("Ingrese la temperatura del día: "))
        self.temperaturas_diarias.append(temp)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas_diarias) != 7:
            print("Debe ingresar las temperaturas de los 7 días de la semana.")
            return
        promedio = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio

# Crear instancia de la clase y utilizar métodos para ingresar datos y calcular promedio
informacion_clima = InformacionClimatica()
for _ in range(7):
    informacion_clima.ingresar_temperatura_diaria()

promedio_semanal = informacion_clima.calcular_promedio_semanal()

print(f"Las temperaturas de la semana son: {informacion_clima.temperaturas_diarias}")
print(f"El promedio semanal de temperaturas es: {promedio_semanal}")