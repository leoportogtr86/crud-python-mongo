### Guia Completo: Como Realizar um CRUD Básico com Python e MongoDB

#### Introdução

Neste artigo, vamos explorar como realizar operações básicas de CRUD (Create, Read, Update, Delete) usando Python e MongoDB. O MongoDB é um banco de dados NoSQL amplamente utilizado por sua flexibilidade e escalabilidade. Vamos usar a biblioteca `pymongo` para interagir com o MongoDB.

#### Pré-requisitos

- Python instalado (recomendo a versão 3.6 ou superior)
- MongoDB instalado e em execução
- Biblioteca `pymongo` instalada (`pip install pymongo`)

#### Configurando o Ambiente

Antes de começar, certifique-se de que o MongoDB está em execução no seu sistema. Você pode iniciar o MongoDB com o comando:

```bash
mongod
```

Instale a biblioteca `pymongo` usando o pip:

```bash
pip install pymongo
```

#### Conectando ao MongoDB

Vamos começar conectando ao MongoDB. Crie um arquivo Python (por exemplo, `crud_mongodb.py`) e adicione o seguinte código:

```python
from pymongo import MongoClient

# Conectando ao servidor MongoDB (localhost por padrão)
client = MongoClient('localhost', 27017)

# Selecionando o banco de dados
db = client['meu_banco_de_dados']

# Selecionando a coleção
collection = db['minha_colecao']
```

#### Operação de Create (Criar)

Vamos inserir um documento na coleção. Adicione o seguinte código ao seu arquivo:

```python
# Dados do documento a ser inserido
documento = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

# Inserindo o documento
resultado = collection.insert_one(documento)
print(f'Documento inserido com o ID: {resultado.inserted_id}')
```

#### Operação de Read (Ler)

Agora, vamos ler os documentos da coleção. Adicione o seguinte código:

```python
# Lendo um único documento
documento = collection.find_one({'nome': 'João'})
print(f'Documento encontrado: {documento}')

# Lendo todos os documentos
todos_documentos = collection.find()
for doc in todos_documentos:
    print(doc)
```

#### Operação de Update (Atualizar)

Vamos atualizar um documento na coleção. Adicione o seguinte código:

```python
# Critério de busca
criterio = {'nome': 'João'}

# Novos dados
novos_dados = {'$set': {'idade': 31}}

# Atualizando o documento
resultado = collection.update_one(criterio, novos_dados)
print(f'Documentos modificados: {resultado.modified_count}')
```

#### Operação de Delete (Excluir)

Finalmente, vamos excluir um documento da coleção. Adicione o seguinte código:

```python
# Critério de busca para exclusão
criterio = {'nome': 'João'}

# Excluindo o documento
resultado = collection.delete_one(criterio)
print(f'Documentos excluídos: {resultado.deleted_count}')
```

#### Conclusão

Neste artigo, cobrimos como realizar operações básicas de CRUD usando Python e MongoDB. Com estas operações, você pode começar a construir aplicações que interagem com um banco de dados MongoDB de maneira eficiente. Lembre-se de explorar mais sobre as capacidades do `pymongo` e do MongoDB para aproveitar ao máximo essas ferramentas poderosas.

#### Código Completo

Aqui está o código completo para referência:

```python
from pymongo import MongoClient

# Conectando ao servidor MongoDB (localhost por padrão)
client = MongoClient('localhost', 27017)

# Selecionando o banco de dados
db = client['meu_banco_de_dados']

# Selecionando a coleção
collection = db['minha_colecao']

# Create
documento = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}
resultado = collection.insert_one(documento)
print(f'Documento inserido com o ID: {resultado.inserted_id}')

# Read
documento = collection.find_one({'nome': 'João'})
print(f'Documento encontrado: {documento}')

todos_documentos = collection.find()
for doc in todos_documentos:
    print(doc)

# Update
criterio = {'nome': 'João'}
novos_dados = {'$set': {'idade': 31}}
resultado = collection.update_one(criterio, novos_dados)
print(f'Documentos modificados: {resultado.modified_count}')

# Delete
criterio = {'nome': 'João'}
resultado = collection.delete_one(criterio)
print(f'Documentos excluídos: {resultado.deleted_count}')
```

