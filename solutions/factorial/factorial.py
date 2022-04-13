"""
Escribir un programa que solicite el ingreso de números, y a medida que se ingresan, calcule e informe el factorial de cada número.
Para saber si el programa debe seguir solicitando ingresos, se le debe preguntar al usuario si desea ingresar otro número.
En caso que no se pueda calcular el factorial del número ingresado, se debe informar que no es posible calcular el factorial para dicho número.
"""

continuar = "s"
print(f"======= CALCULADOR DE FACTORIAL ========= ")
while continuar == "s":
    numero = float(input("Ingresá un numero: "))
    if numero % 1 == 0.0:
        result = 1
        for n in range(int(abs(numero)), 0, -1):
            result = result * n
        result = result * -1 if numero < 0 else result
        print(f"factorial de {numero}! es {result} ")
        result = 1
    else:
        print(f"No es posible calcular el factorial para {numero}")
        print(f"Tip: ingresá un numero entero")
    continuar = str(input("Continuar calculando factorial ? S/n (o cualquier caracter para salir): ")).lower()
