import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

historico = []

while True:
    mensagem = input("\nVocê: ")

    if mensagem.lower() =="sair":
        break

    historico.append({
        "role": "user",
        "content": mensagem
    })

    resposta = client.responses.create(
        model="gpt-5-mini",
        input=historico
    )

    historico.append({
        "role": "assistant",
        "content": resposta.output_text
    })

    print("\nLLM:", resposta.output_text)