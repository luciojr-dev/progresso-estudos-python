# ==========================================
# MINI FINANCEIRO
# ==========================================


# ==========================================
# FUNÇÕES
# ==========================================

# Calcula o total de todos os gastos
def calcular_total_gastos(gastos):
    total_gastos = 0

    for gasto in gastos:
        total_gastos = total_gastos + gasto

    return total_gastos


# Calcula o saldo restante
def calcular_saldo(salario, total_gasto):
    calcular = salario - total_gasto
    return calcular


# ==========================================
# ENTRADA DE DADOS
# ==========================================

# Pega nome, salario do usuario e quantidade de gastos
nome_pessoa = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
quantidade_gastos = int(
    input(f"Quantos gastos deseja cadastrar {nome_pessoa}: ")
)


# ==========================================
# CADASTRO DOS GASTOS
# ==========================================

# Lista para guardar gastos
gastos = []

# Adiciona gastos na lista
for numero in range(quantidade_gastos):
    gasto = float(input(f"Digite o gasto {numero + 1}: "))
    gastos.append(gasto)


# ==========================================
# PROCESSAMENTO
# ==========================================

# Chama a funcao que calcula o total de gastos
resultado = calcular_total_gastos(gastos)

print(f"{nome_pessoa} seu total de gasto seria: {resultado}")


# Calcula o restante que sobra
saldo = calcular_saldo(salario, resultado)


# ==========================================
# RESULTADO
# ==========================================

# Compara se o usuario gasta mais do que ganha
if saldo < 0:
    print(
        f"{nome_pessoa} voce esta no negativo. "
        f"Seu saldo é {saldo}"
    )

elif saldo == 0:
    print(
        f"{nome_pessoa} voce gastou todo o seu salario. "
        f"Seu saldo é {saldo}"
    )

else:
    print(
        f"{nome_pessoa} voce esta gastando menos do que recebe, "
        f"seu saldo é {saldo}"
    )