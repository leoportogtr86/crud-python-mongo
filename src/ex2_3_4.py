# 2. **Criação de Banco de Dados e Coleção**
# - Crie um banco de dados chamado `biblioteca` e uma coleção chamada `livros`.
# 3. **Inserção Simples**
# - Insira um documento na coleção `livros` com os campos `titulo`, `autor` e `ano`.
# 4. **Inserção Múltipla**
# - Insira múltiplos documentos de uma só vez na coleção `livros`.

from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["biblioteca"]
livros = db["livros"]

livro = {
    "titulo": "Como Programar em HTML",
    "autor": "Dev Nutela",
    "ano": 2050
}

res = livros.insert_one(livro)

print(res)