# cria um dicionario
# entendimento: nome -> seria uma chave e o valor seria -> lucio

# exercicio 1
# pessoa = {
#     "nome": "Lucio",
#     "idade": 21,
#     "profissao": "programador",
#     "salario": 8000
# }
# # altera o valor existente
# pessoa["profissao"] = "desenvolvedor"
# pessoa["salario"] = 9000

# # inseri uma nova chave no dicionario
# pessoa["cidade"] = "Sao paulo"

# print(pessoa["profissao"])
# print(pessoa["salario"])

# exercicio 2

# cria o dicionario
# produto = {
#     "nome":"iphone",
#     "preco": 5000,
#     "categoria": "eletronicos"
# }

# produto["preco"] = 8000
# produto["estoque"] = 10

# print(produto["nome"], produto["preco"], produto["estoque"])

# entendimento de dicionarios com for
# for que percorre somente as chaves
# for item in produto:
#     print(item)

# # for pegando somente os valores
# for item in produto.values():
#     print(item)

# # for pegando chave e valor
# for chave, valor in produto.items():
#     print(chave, valor)

# exercicio 3
# for chave, valor in produto.items():
#     print(chave, valor)

# verificando se uma chave existe
# obs: quando fazemos preco in produto -> estamos procurando uma chave, nao valor
# if "preco" in produto:
#     print("produto possui preco cadastrado")
# else:
#     print("preco nao esta cadastrado")

# # verificando em valores
# if 8000 in produto.values():
#     print("valor existe dentro de produtos")
# else:
#     print("valor nao existe")

# # execicio 4
# if "preco" in produto:
#     print("o preco esta cadastrado")
# else:
#     print("preco nao cadastrado")

# if "estoque" in produto:
#     print("o estoque esta cadastrado")
# else:
#     print("estoque nao cadastrado")

# exercicio 5
produto = {
    "nome": "Notebook",
    "preco": 4500,
    "categoria": "eletronicos",
    "estoque": 5
}

for chave, valor in produto.items():
    if chave == "preco":
        print(f"o produto custa {valor}")
    elif chave == "estoque":
        if valor > 0 :
            print("produto disponivel")
        else:
            print("produto indisponivel")