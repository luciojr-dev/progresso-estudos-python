from transformers import AutoTokenizer, AutoModel 
import torch

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM-135M")

texto = input("Digite alguma coisa: ")

tokens = tokenizer.tokenize(texto)
ids = tokenizer.convert_tokens_to_ids(tokens)

print(tokens)
print(ids)

input_ids = torch.tensor([ids])
print(input_ids)

model = AutoModel.from_pretrained("HuggingFaceTB/SmolLM-135M")

embedding_layer = model.get_input_embeddings()

embedding = embedding_layer(input_ids)
print(embedding)