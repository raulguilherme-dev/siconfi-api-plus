# FastAPI Siconfi Entes

![Status do Projeto](https://img.shields.io/badge/status-active-brightgreen.svg)
![Versão](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Licença](https://img.shields.io/badge/license-MIT-green.svg)

## Descrição

Esta é uma API RESTful construída com [FastAPI](https://fastapi.tiangolo.com/), projetada para coletar dados de um dos endpoints da API da [SICONFI](https://apidatalake.tesouro.gov.br/docs/siconfi/) (Sistema de Informações Contábeis e Fiscais do Setor Público Brasileiro) porém com a possibilidade de realizar operações de filtragem, ordenação e agregação de dados.

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoints](#endpoints)

## Instalação

### Pré-requisitos

- [Python](https://www.python.org/downloads/) 3.7 ou superior
- [pip](https://pip.pypa.io/en/stable/)

### Passos para Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/[nome-de-usuario]/[repositorio].git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd [pasta-raiz]
    ```

3. Crie e ative um ambiente virtual:
    ```sh
    python -m venv env
    ```

4. Ative o ambiente virtual

    ```sh
    env/Scripts/Activate #No Windows
    ```

    ```sh
    source env/bin/activate #No Linux
    ```

5. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```


### Instalação com Docker

#### Pré-requisitos

- [Docker](https://www.docker.com/)

#### Passos da instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/[usuario]/[repositorio].git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd fastapi-book-library
    ```

3. Construa a imagem Docker:
    ```sh
    docker build -t fastapi-book-library .
    ```
    
## Uso

### Iniciando o Servidor Localmente

Para iniciar o servidor de desenvolvimento, na pasta raiz do projeto execute:

```sh
uvicorn app.main:app --reload
```

#### O servidor será iniciado em `http://127.0.0.1:8000`.

### Iniciando o Servidor em Container

    ```sh
    docker run -d -p 8000:8000 fastapi-book-library
    ```

#### O servidor será iniciado em `http://0.0.0.0:8000`.

### Documentação Interativa

A documentação da API estará disponível em:

#### Localmente

- http://127.0.0.1:8000/docs (Swagger UI)
- http://127.0.0.1:8000/redoc (ReDoc)

#### Em Container

- http://0.0.0.0:8000/docs (Swagger UI)
- http://0.0.0.0:8000/redoc (ReDoc)

## Endpoints

### Buscar Entes

- URL: `/get_entes`
- Metodo: `GET`
- Descrição: Lista todos os entes da federação com suporte para filtros, agregação e ordenação.

Ao acessar o endpoint sem passar nenhum parâmetro será retornado os mesmos dados que ao acessar a [API original](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes).

```json
    {
        "cod_ibge": 3516903,
        "ente": "General Salgado",
        "capital": "0  ",
        "regiao": "SE",
        "uf": "SP",
        "esfera": "M",
        "exercicio": 2024,
        "populacao": 10301,
        "cnpj": "45660610000150"
    }
```


### Parâmetros de consulta

- `filters` (Opcional): Recebe um Json com os filtros que devem ser aplicados na consulta. Os filtros disponíveis são:
    - `capital` 
    - `regiao` 
    - `uf` 
    - `esfera`
    - `exercicio`
    - `populacao` 
    
#### Exemplo de `filters`

```json
{
    "uf": "SP",
    "esfera": "M",
    "populacao": {
        "min": 5000,
        "max": 15000
    }
}
```

- `group_by` (Opcional): Deve receber alguma das opções de filtros para agrupar os dados com base nesse filtro.

- `order` (Opcional): Recebe um Json com dois parâmetros:   
    - `order_by` deve receber uma string com uma das opções de filtros para ordenar os dados. 
    - `reverse` recebe um booleano, por padrão `False`, se verdadeiro `True` irá retornar os dados em ordem reversa.

- `count` (Opcional): Recebe um booleano, por padrão falso, se verdadeiro (True) irá retornar a contagem total de dados.

- `show_only` (Opcional): deve receber uma lista de keys seprados por "|". Irá retornar os dados contendo apenas as keys que foram passadas por parâmetro.

#### Exemplo de `show_only`

```http
?show_only=ente|uf|regiao|populacao
```

irá retornar os dados dessa forma:

```json
    {
        "ente": "General Salgado",
        "regiao": "SE",
        "uf": "SP",
        "populacao": 10301,
    }
```

### Importante

Alguns parâmentros não podem ser usados juntos. E caso sejam utilizados essa mensagem será retornada:

```json
{"detail":"Combinação de parâmetros inválida"}
```
#### Lista de paramentros que não podem ser utilizados juntos

- `count` e `group_by`
- `count` e `order`
- `count` e `show_only`
- `group_by` e `show_only`

