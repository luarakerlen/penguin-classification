# 🐧 Predição de Espécie de Pinguins com Machine Learning

Este projeto foi desenvolvido o **MVP da Sprint de Qualidade de Software** no curso de **Pós-graduação em Engenharia de Software** da **PUC-Rio**.

O objetivo principal é construir um sistema completo de predição de espécies de pinguins, utilizando técnicas de machine learning e boas práticas de desenvolvimento de software.

---

## 📌 Descrição

O sistema permite prever a espécie de um pinguim com base em três características morfológicas:

- Comprimento do bico (em milímetros)
- Profundidade do bico (em milímetros)
- Comprimento da nadadeira (em milímetros)

Foram utilizadas as bibliotecas `scikit-learn`, `joblib`, `Flask`, `pytest` e outras ferramentas do ecossistema Python.

---

## 📁 Estrutura do Projeto

```
├── backend/
│   ├── app.py                # API Flask que carrega o modelo e faz as predições
│   ├── modelo_pinguins.joblib  # Modelo de ML serializado com pipeline
│   ├── label_encoder.joblib    # Codificador de rótulos (LabelEncoder)
│   ├── test_model.py         # Testes automatizados com PyTest
│   └── requirements.txt      # Dependências do projeto
├── frontend/
│   ├── index.html              # Frontend com formulário interativo
│   ├── style.css               # Estilização do frontend
└── README.md                 # Documentação do projeto
```

---

## 🔗 Notebook Colab

O desenvolvimento do modelo de machine learning foi feito no Google Colab:

👉 [Abrir notebook no Colab](https://colab.research.google.com/drive/1Dh6tUTU1aFAmZHxX88JnEopIwh5FMjMP?usp=sharing)

---

## ▶️ Como Executar

### 1. Clone o repositório e entre na pasta do backend:

```bash
git clone <url-do-repositorio>
cd backend
```

### 2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute a API Flask:

```bash
python app.py
```

A API estará disponível em: `http://127.0.0.1:5000`

---

## 🌐 Front-end

Abra o arquivo `index.html` no navegador. Preencha os campos e envie para obter a espécie prevista.  
O front-end se comunica com o back-end via `fetch()` para a rota `/predict`.

---

## ✅ Testes Automatizados

Execute os testes com:

```bash
pytest -s test_model.py
```

Eles verificam se o modelo atende a um limiar mínimo de acurácia.

---

## 🛡️ Segurança e Boas Práticas

Durante o projeto, foram aplicadas práticas como:

- Separação de treino/teste com estratificação
- Validação cruzada
- Padronização com `StandardScaler`
- Pipeline completo serializado
- Testes automatizados com métricas objetivas
- Separação clara entre back-end e front-end

---

## 👩🏽‍💻 Autora

<a href="https://www.linkedin.com/in/luarakerlen/" target="_blank">
 <img title="Luara Kerlen" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/26902816?v=4" width="100px;" alt="Foto da Luara"/>
 </a>

Feito com ❤️ por <a href="https://www.linkedin.com/in/luarakerlen/" target="_blank"><b>Luara Kerlen</b></a> <a href="https://www.linkedin.com/in/luarakerlen/" title="Luara Kerlen"></a>
<br>Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Luara%20Kerlen-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/luarakerlen/)](https://www.linkedin.com/in/luarakerlen/)
[![Gmail Badge](https://img.shields.io/badge/-luarakerlen12@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:luarakerlen12@gmail.com)](mailto:luarakerlen12@gmail.com)
[![Instagram Badge](https://img.shields.io/badge/Luara%20Kerlen-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/luarakerlen)