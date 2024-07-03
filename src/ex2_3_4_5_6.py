# 2. **Criação de Banco de Dados e Coleção**
# - Crie um banco de dados chamado `biblioteca` e uma coleção chamada `livros`.
# 3. **Inserção Simples**
# - Insira um documento na coleção `livros` com os campos `titulo`, `autor` e `ano`.
# 4. **Inserção Múltipla**
# - Insira múltiplos documentos de uma só vez na coleção `livros`.
# 5. **Leitura Simples**
# - Leia um documento específico da coleção `livros` usando o campo `titulo`.
# 6. **Leitura Múltipla**
# - Leia todos os documentos da coleção `livros` e exiba-os.
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["biblioteca"]
livros = db["livros"]

livro = {
    "titulo": "Como Programar em HTML",
    "autor": "Dev Nutela",
    "ano": 2050
}

lista_livros = [
    {
        "titulo": "Como Programar em Java",
        "autor": "Joe Dev",
        "ano": 2024
    },
    {
        "titulo": "Como Programar em Python",
        "autor": "Python Dev",
        "ano": 2025
    },
    {
        "titulo": "Como Programar em C",
        "autor": "C Dev",
        "ano": 2026
    },
    {
        "titulo": "Como Programar em C++",
        "autor": "C++ Dev",
        "ano": 2027
    },
    {
        "titulo": "Como Programar em C#",
        "autor": "C# Dev",
        "ano": 2028
    }
]

# res = livros.insert_one(livro)

# print(res)

#
# res1 = livros.insert_many(lista_livros)
#
# print(res1)

livro_buscado = livros.find_one({
    "titulo": "Como Programar em C#"
})

# print(livro_buscado)
todos_os_livros = livros.find()

for livro in todos_os_livros:
    print(livro)
