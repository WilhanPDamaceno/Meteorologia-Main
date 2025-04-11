# Sistema de Meteorologia

Este é um sistema simples de meteorologia desenvolvido com FastAPI que permite registrar e consultar dados de temperatura de diferentes cidades.

## Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório ou baixe os arquivos do projeto

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- No Windows:
```bash
.\venv\Scripts\activate
```
- No Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

- `main.py`: Arquivo principal da aplicação FastAPI
- `weatherModel.py`: Modelo de dados e configuração do banco de dados
- `requirements.txt`: Lista de dependências do projeto

## Executando o Projeto

1. Certifique-se de que o ambiente virtual está ativado

2. Inicie o servidor:
```bash
uvicorn main:app --reload
```

3. Para acessar localmente:
- Abra seu navegador e acesse: `http://localhost:8000`

4. Para acessar de outros dispositivos na rede local:
- Inicie o servidor com:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
- Descubra o IP do seu computador na rede local
- Acesse de outro dispositivo usando: `http://SEU_IP:8000`

## Endpoints da API

- `GET /`: Página inicial do sistema
- `POST /weather/`: Adiciona dados meteorológicos
  - Parâmetros:
    - city: Nome da cidade
    - temperature: Temperatura registrada
- `GET /weather/`: Retorna todos os registros de cidades e temperaturas

## Documentação da API

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Observações

- Certifique-se de que a porta 8000 está liberada no seu firewall
- Para maior segurança, é recomendado usar apenas em redes locais confiáveis
- O banco de dados SQLite é criado automaticamente na primeira execução 