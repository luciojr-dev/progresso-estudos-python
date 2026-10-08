from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Carregando o tokenizer e o modelo
model_name = "Qwen/Qwen3-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

model.eval()

texto = "A inteligência artificial está"

# Transformando o texto em tokens/IDs
inputs = tokenizer(texto, return_tensors="pt")

temperature = 1.0
top_k = 5

with torch.inference_mode():

    # Passando os tokens pelo Transformer
    outputs = model(**inputs)

    # Pegando os logits do último token
    ultimo_logits = outputs.logits[:, -1, :]

    # Aplicando temperature
    logits_ajustados = ultimo_logits / temperature

    # Pegando apenas os K tokens mais prováveis
    valores, indices = torch.topk(
        logits_ajustados,
        top_k
    )

    # Transformando os Top-K logits em probabilidades
    probabilidades = torch.softmax(valores, dim=-1)

    print(f"\nTop-{top_k} tokens:")

    for valor, indice in zip(probabilidades[0], indices[0]):
        token = tokenizer.decode([indice])
        print(token, "→", valor.item())

    # Sampling somente entre os Top-K
    escolhido = torch.multinomial(
        probabilidades,
        num_samples=1
    )

    proximo_token_id = indices.gather(
        1,
        escolhido
    )

    print("\nToken escolhido:")
    print(tokenizer.decode([proximo_token_id.item()]))

    # Começando a geração
    input_ids = inputs["input_ids"].clone()
    attention_mask = inputs["attention_mask"].clone()

    max_new_tokens = 20

    for _ in range(max_new_tokens):

        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        ultimo_logits = outputs.logits[:, -1, :]

        logits_ajustados = ultimo_logits / temperature

        # Mantendo somente os Top-K
        valores, indices = torch.topk(
            logits_ajustados,
            top_k
        )

        probabilidades = torch.softmax(
            valores,
            dim=-1
        )

        # Sampling entre os Top-K
        escolhido = torch.multinomial(
            probabilidades,
            num_samples=1
        )

        proximo_token_id = indices.gather(
            1,
            escolhido
        )

        # Adicionando o token à sequência
        input_ids = torch.cat(
            [input_ids, proximo_token_id],
            dim=1
        )

        nova_atencao = torch.ones(
            (attention_mask.shape[0], 1),
            dtype=attention_mask.dtype
        )

        attention_mask = torch.cat(
            [attention_mask, nova_atencao],
            dim=1
        )

        if (
            tokenizer.eos_token_id is not None
            and proximo_token_id.item() == tokenizer.eos_token_id
        ):
            break

texto_gerado = tokenizer.decode(
    input_ids[0],
    skip_special_tokens=True
)

print("\nTexto gerado:")
print(texto_gerado)