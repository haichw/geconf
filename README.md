# Flask API com Integração Contínua e Docker

Este projeto consiste em uma API simples utilizando Flask, integrada a um pipeline de integração contínua (CI) utilizando GitHub Actions e Docker.

## 🚀 Tecnologias Utilizadas

- Python 3.13.2
- Flask
- GitHub Actions
- Docker

## 📌 Estrutura do Projeto

```
/
├── app.py            # Código principal da aplicação Flask
├── requirements.txt  # Dependências do projeto
├── Dockerfile        # Configuração para criação da imagem Docker
├── .github/workflows/ci.yml  # Pipeline de integração contínua
├── test_app.py   # Testes unitários com pytest
```

## 🛠️ Configuração e Execução

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/haichw/geconf.git
cd seu-repositorio
```

### 2️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Executar a Aplicação
```bash
python app.py
```
A API estará disponível em `http://localhost:5000`.

### 4️⃣ Executar os Testes
```bash
pytest
```

## 🐳 Executando com Docker

### 1️⃣ Construir a Imagem
```bash
docker build -t hello-world-app .
```

### 2️⃣ Rodar o Container
```bash
docker run -d -p 0:5000 --name hello-world-container hello-world-app
```
Acesse o container pelo navegador.

## 🔄 Integração Contínua
Sempre que houver um `push` na branch `main`, o GitHub Actions executará automaticamente os seguintes passos:

1. Verificação do código-fonte
2. Execução dos testes unitários
3. Construção da imagem Docker
4. Execução do container em uma porta aleatória
