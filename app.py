peso = float(input("Ingrese su peso en KG separado por  '.'  :" ))
altura = float(input("Ingrese su altura en M separado por '.' : "))

def calcularImc(peso,altura):
    imc = peso / (altura ** 2)
    print(f"Tu indice de masa corporal es: {imc: .2f}")



calcularImc(peso, altura)