# 🗺️ Mapa Colaborativo

## 📌 Sobre o projeto

O **Mapa Colaborativo** é uma aplicação web que permite aos usuários identificar problemas em diferentes locais da comunidade e também propor possíveis soluções.

Por meio de um mapa interativo, o usuário pode selecionar qualquer ponto no mapa, informar o endereço e escrever uma descrição sobre um problema encontrado. Esse problema será registrado e exibido através de um **marcador vermelho**.

Além disso, o usuário pode cadastrar uma ideia de melhoria ou solução para determinado local, que será exibida no mapa através de um **marcador verde**.

A aplicação busca incentivar a participação das pessoas na identificação de dificuldades do ambiente ao seu redor e na criação de propostas de melhoria utilizando geolocalização e colaboração.

---

# 🚀 Funcionalidades

* Visualização de um mapa interativo utilizando Leaflet e OpenStreetMap;
* Seleção de pontos diretamente no mapa;
* Cadastro de problemas encontrados em determinados locais;
* Cadastro de propostas de solução;
* Exibição dos problemas e soluções registrados no mapa;
* Remoção de registros cadastrados;
* Armazenamento das informações em arquivos JSON locais;
* Exibição de locais de interesse personalizados;
* Legenda para facilitar a identificação dos diferentes marcadores.

---

## 🧰 Tecnologias utilizadas

### Backend

* Python;
* Flask;
* JSON como banco de dados simples.

### Frontend

* HTML5;
* CSS3;
* JavaScript;
* Leaflet.js;
* OpenStreetMap.

---

## 📂 Estrutura do projeto

```text
Mapa-Colaborativo/
│
├── static/                 # Arquivos estáticos (CSS, imagens, ícones, etc.)
│
├── templates/
│   └── index.html          # Interface principal da aplicação
│
├── app.py                  # Servidor Flask e rotas da API
├── problemas.json          # Armazena os problemas cadastrados
├── solucoes.json           # Armazena as soluções cadastradas
├── requirements.txt        # Dependências do projeto
├── runtime.txt             # Versão/configuração do ambiente de execução
├── Procfile                # Configuração de execução para deploy
└── LICENSE                 # Licença do projeto
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/rafael-vincensi/trabalho-tecnologia-transformacao
```

### 2. Acesse a pasta do projeto

```bash
cd Mapa-Colaborativo
```

### 3. Instale as dependências

```bash
pip install flask
```

### 4. Execute a aplicação

```bash
python app.py
```

### 5. Acesse no navegador

```
http://localhost:5000
```

---

## 🎨 Legenda do mapa

| Marcador | Significado                    |
| -------- | ------------------------------ |
| 🔵       | Local selecionado pelo usuário |
| 🟣       | Locais de interesse            |
| 🔴       | Problema identificado          |
| 🟢       | Proposta de solução            |

---

## 💾 Armazenamento dos dados

As informações cadastradas são salvas localmente em arquivos JSON:

* `problemas.json`: armazena os problemas registrados;
* `solucoes.json`: armazena as soluções propostas.

Cada registro contém:

* ID único;
* Rua ou endereço;
* Descrição;
* Latitude;
* Longitude.

---

## 🎯 Objetivo

O objetivo do projeto é utilizar a tecnologia como uma ferramenta de participação coletiva, permitindo que usuários possam mapear problemas e compartilhar ideias de melhoria para diferentes locais, promovendo uma maior colaboração entre a comunidade.
