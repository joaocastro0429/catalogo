# Catálogo

## 📌 Visão Geral

Este projeto é uma aplicação web desenvolvida com o framework **Django**, destinada à criação e gerenciamento de um catálogo, possivelmente de cursos ou produtos. A estrutura do projeto sugere funcionalidades como listagem, criação, edição e exclusão de itens no catálogo.

## 🛠️ Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Framework Web:** Django
- **Frontend:** HTML (com templates Django)
- **Gerenciador de Dependências:** pip

## 📁 Estrutura do Projeto

A estrutura do projeto é a seguinte:

catalogo/
│
├── manage.py # Script de gerenciamento do Django
├── requirements.txt # Lista de dependências do projeto
└── cursos/ # Aplicação Django principal
├── models.py # Modelos de dados
├── views.py # Lógica das views
├── urls.py # Rotas da aplicação
└── templates/ # Templates HTML




## ⚙️ Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente:

### 1. Clone o repositório

git clone https://github.com/joaocastro0429/catalogo.git
cd catalogo
## 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

##3. Instale as dependências

pip install -r requirements.txt


##4. Aplique as migrações do banco de dados

python manage.py migrate

 Funcionalidades Principais

Com base na estrutura do projeto, as seguintes funcionalidades são esperadas:

    Listagem de Itens: Visualização de todos os cursos/produtos cadastrados.

    Detalhes do Item: Visualização de informações detalhadas de um curso/produto específico.

    Criação de Itens: Adição de novos cursos/produtos ao catálogo.

    Edição de Itens: Modificação das informações de cursos/produtos existentes.

    Exclusão de Itens: Remoção de cursos/produtos do catálogo.

📝 Considerações Finais

Para uma documentação mais detalhada, seria ideal a inclusão de um arquivo README.md no repositório,
contendo informações sobre o propósito do projeto, instruções de instalação, uso e contribuições. 
Além disso, a adição de comentários no código e a melhoria na organização dos arquivos são práticas recomendadas.
