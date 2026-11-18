# Legativa — Proof of Concept (PoC)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![PyPDF](https://img.shields.io/badge/PyPDF-3776AB?style=for-the-badge)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Ollama](https://img.shields.io/badge/Ollama-111111?style=for-the-badge&logo=ollama&logoColor=white)
![Gemma 3](https://img.shields.io/badge/Gemma%203-4285F4?style=for-the-badge&logo=google&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge&logo=uv&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-4B5563?style=for-the-badge)

**Inteligência Artificial para Conformidade à LGPD**

Prova de conceito da **Legativa**, uma plataforma de inteligência artificial voltada ao apoio à adequação de sistemas à Lei Geral de Proteção de Dados (LGPD).

O experimento explora um pipeline de *Retrieval-Augmented Generation* (RAG), permitindo realizar consultas à legislação e gerar respostas a partir dos trechos recuperados.

---

### Pré-requisitos

[![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/downloads)
[![Python 3.12](https://img.shields.io/badge/Python%203.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat&logo=uv&logoColor=white)](https://docs.astral.sh/uv/getting-started/installation/)
[![Ollama](https://img.shields.io/badge/Ollama-111111?style=flat&logo=ollama&logoColor=white)](https://ollama.com/download)

A aplicação executa os modelos localmente, sem necessidade de chaves de API.

### Instalação e execução

**1. Clone o repositório.**

```bash
git clone https://github.com/Legativa/legativa-poc.git
cd legativa-poc
```

**2. Instale as dependências.**

```bash
uv sync
```

**3. Baixe o modelo Gemma 3 pelo Ollama.**

```bash
ollama pull gemma3:4b
```

**4. Execute a aplicação.**

Com o Ollama em execução:

```bash
uv run python main.py
```

Na primeira execução, o modelo de embeddings `multilingual-e5-small` será baixado automaticamente do Hugging Face.

### Utilização

Após a indexação da LGPD, o terminal ficará disponível para consultas:

```text
Legativa PoC — Consultas à LGPD
Digite 'sair' para encerrar.

Pergunta: Quais são os direitos dos titulares?

Resposta:
...

--- Fontes recuperadas ---
[1] Página 10
...

Pergunta: sair
```

É possível realizar múltiplas consultas sem reiniciar a aplicação. Para encerrar, digite `sair`.

### Documentação

- [Prova de Conceito](docs/poc.md) — escopo, decisões técnicas e funcionamento do pipeline.
- [Experimentos](docs/experiments.md) — consultas realizadas e resultados observados.

---

*Projeto experimental. As respostas geradas podem conter informações incorretas e não substituem orientação jurídica especializada.*