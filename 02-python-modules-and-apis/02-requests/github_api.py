import requests

resposta = requests.get("https://api.github.com/users/luciojr-dev")
print(resposta.status_code)

dados = resposta.json()
print(f"Meu nome no github é {dados["name"]}")