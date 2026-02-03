# Ask AI PET
API que atual como assistente de vendas especializado em produtos de pet.

## Stack utilizada
**Back-end:** FastAPI, LangChai, OpenAI, pydantic, uvicorn.

## Instalação
OBS: É necessario ter o [Docker](https://docs.docker.com/engine/install/) instalado na máquina.

#### 1. Lembre de adiciona o arquivo .env com seus respectivos valores
- OPENAI_API_KEY: API key da [OpenAI](https://platform.openai.com/settings/organization/api-keys).
- OPENAI_MODEL: [Modelo](https://platform.openai.com/docs/pricing) da llm o valor padrão é "gpt-4o-mini"

#### 2. Faça o clone do projeto na sua maquina:
```bash
  git clone git@github.com:joaoparaujocr/ask_ia.git
```

#### 3. Entre dentro da pasta ask_ia e execute:

```bash
  docker compose up
```

#### 4. Aguarde as instalações necessarias e a aplicação estara disponivel no ambiente local http://localhost:8000

#### 4. Para realizar o teste da rota http://localhost:8000/docs