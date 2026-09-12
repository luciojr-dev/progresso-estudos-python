# pega nome, salario do usuario e quantidade de gastos
nome_pessoa = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
quantidade_gastos = int(input(f"Quantos gastos deseja cadastrar {nome_pessoa}: "))

# lista para guardar gastos
gastos = []

# adiciona gastos na lista
for numero in range(quantidade_gastos):
    gasto = float(input(f"Digite o gasto {numero + 1}: "))
    gastos.append(gasto)

# calcula gastos
def calcular_total_gastos(gastos):
    total_gastos = 0

    for gasto in gastos:
        total_gastos = total_gastos + gasto

    return total_gastos

# Chama funçao
resultado = calcular_total_gastos(gastos)
print(f"{nome_pessoa} seu total de gasto seria: {resultado}")

# calcular o restante que sobra
def calcular_saldo(salario, total_gasto):
    calcular = salario - total_gasto
    return calcular

saldo = calcular_saldo(salario, resultado)

# comparaçao se usuario gasta mais do que ganha
if saldo < 0:
    print(f"{nome_pessoa} voce esta no negativo. Seu saldo é {saldo}")
elif saldo == 0: 
    print(f"{nome_pessoa} voce gastou todo o seu salario. Seu saldo é {saldo}")
else: 
    print(f"{nome_pessoa} Voce esta gastando menos do que recebe, seu saldo é {saldo}")