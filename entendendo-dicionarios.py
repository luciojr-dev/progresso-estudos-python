# Entendendo dicionarios
# entendimento: nome -> seria uma chave e o valor seria -> Lucio


# ==========================================
# Exercicio 1
# ==========================================

# cria um dicionario
pessoa = {
    "nome": "Lucio",
    "idade": 21,
    "profissao": "programador",
    "salario": 8000
}

# altera o valor existente
pessoa["profissao"] = "desenvolvedor"
pessoa["salario"] = 9000

# inseri uma nova chave no dicionario
pessoa["cidade"] = "Sao Paulo"

print(pessoa["profissao"])
print(pessoa["salario"])


# ==========================================
# Exercicio 2
# ==========================================

# cria o dicionario
produto = {
    "nome": "iphone",
    "preco": 5000,
    "categoria": "eletronicos"
}

produto["preco"] = 8000
produto["estoque"] = 10

print(produto["nome"], produto["preco"], produto["estoque"])


# ==========================================
# Entendimento de dicionarios com for
# ==========================================

# for que percorre somente as chaves
for item in produto:
    print(item)

# for pegando somente os valores
for item in produto.values():
    print(item)

# for pegando chave e valor
for chave, valor in produto.items():
    print(chave, valor)


# ==========================================
# Exercicio 3
# ==========================================

for chave, valor in produto.items():
    print(chave, valor)


# ==========================================
# Verificando se uma chave existe
# ==========================================

# obs: quando fazemos "preco" in produto
# estamos procurando uma chave, nao um valor

if "preco" in produto:
    print("produto possui preco cadastrado")
else:
    print("preco nao esta cadastrado")


# verificando em valores
if 8000 in produto.values():
    print("valor existe dentro de produtos")
else:
    print("valor nao existe")


# ==========================================
# Exercicio 4
# ==========================================

if "preco" in produto:
    print("o preco esta cadastrado")
else:
    print("preco nao cadastrado")

if "estoque" in produto:
    print("o estoque esta cadastrado")
else:
    print("estoque nao cadastrado")


# ==========================================
# Exercicio 5
# ==========================================

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

        # segunda pergunta:
        # se a chave for estoque, verificamos se o valor
        # do estoque e maior que zero
        if valor > 0:
            print("produto disponivel")
        else:
            print("produto indisponivel")