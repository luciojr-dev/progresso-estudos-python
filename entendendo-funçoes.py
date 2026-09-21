# Entendendo funçoes
#------------------------

#cria uma lista
gastos = [100, 250, 350]

# define uma funçao
def calcular_gastos(gastos):
    total_gasto = 0

    for gastos in gastos:
        total_gasto = total_gasto + gastos

    return total_gasto
resultado = calcular_gastos(gastos)
print(resultado)