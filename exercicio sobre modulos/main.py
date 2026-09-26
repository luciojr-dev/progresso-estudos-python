# FORMA 1: importa o modulo inteiro e precisa indicar de onde vem a funçao
# import calculadora

# resultado = calculadora.multiplicar(10, 2)
# print(resultado)

# FORMA 2: Importa diretamenta a funçao
from calculadora import multiplicar as multi, subtrair as sub

resultado1 = multi(10, 2)
print(resultado1)

resultado2 = sub(50, 20)
print(resultado2)