# 1. **Conexão Básica**
# - Crie um script Python que se conecte a um banco de dados MongoDB local.
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["meu_banco_2"]
collection = db["outra_colecao"]
