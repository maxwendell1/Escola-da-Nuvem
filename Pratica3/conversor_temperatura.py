"""
4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32
def celsius_para_kelvin(c):
    return c + 273.15
def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9
def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15
def kelvin_para_celsius(k):
    return k - 273.15
def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temperatura = float(input("Digite a temperatura a ser convertida: "))
unidade_inicial = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_final = input("Digite a unidade para qual deseja converter (C, F, K): ").upper()

if unidade_inicial == unidade_final:
    temp_convertida = temperatura
elif unidade_inicial == 'C' and unidade_final == 'F':
    temp_convertida = celsius_para_fahrenheit(temperatura)
elif unidade_inicial == 'C' and unidade_final == 'K':
    temp_convertida = celsius_para_kelvin(temperatura)
elif unidade_inicial == 'F' and unidade_final == 'C':
    temp_convertida = fahrenheit_para_celsius(temperatura)
elif unidade_inicial == 'F' and unidade_final == 'K':
    temp_convertida = fahrenheit_para_kelvin(temperatura)
elif unidade_inicial == 'K' and unidade_final == 'C':
    temp_convertida = kelvin_para_celsius(temperatura)
elif unidade_inicial == 'K' and unidade_final == 'F':
    temp_convertida = kelvin_para_fahrenheit(temperatura)
else:
    print("Unidade inválida. Use C, F ou K.")
    exit()
    
print(f"{temperatura:.2f} °{unidade_inicial} é igual a {temp_convertida:.2f} °{unidade_final}")
