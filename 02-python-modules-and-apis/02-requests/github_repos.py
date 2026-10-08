import requests

reposta = requests.get("https://api.github.com/users/luciojr-dev/repos")

dados = reposta.json()

for repo in dados:
    print(repo["name"])