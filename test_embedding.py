from modules.embeddings import embedding_model

vector = embedding_model.embed_query("Hello world")

print(len(vector))
print(vector[:10])