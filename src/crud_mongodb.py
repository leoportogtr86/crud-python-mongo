from pymongo import MongoClient

cliente = MongoClient("localhost", 27017)

db = cliente["meu_banco_de_dados"]
collection = db["minha_colecao"]

# ========================= create =========================
doc = {
    "nome": "Anny",
    "idade": 12,
    "profissao": "Estudante"
}

res1 = collection.insert_one(doc)

print(res1)

# ========================= read =========================
# Lendo apenas um doc
doc2 = collection.find_one({"nome": "Anny"})

print(doc2)

# Lendo varios docs
docs = collection.find()

for doc in docs:
    print(doc)

# ========================= update =========================
criterio = {
    "nome": "Leonardo"
}

novos_dados = {
    "$set": {
        "idade": 37
    }
}

doc3 = collection.update_many(criterio, novos_dados)

print(doc3)
# ========================= delete =========================
res2 = collection.delete_many({"nome": "Leonardo"})

print(res2)