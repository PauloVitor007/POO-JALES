class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura abaixo do zero absoluto não é permitida.")
        self.__celsius = valor
        
temp = Temperatura(25)
print(f"Temperatura em °C: {temp.celsius}°C")
print(f"Temperatura em °F: {temp.fahrenheit}°F")

temp.celsius = 100
print(f"Temperatura em °C: {temp.celsius}°C")
print(f"Temperatura em °F: {temp.fahrenheit}°F")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Erro: {e}")
