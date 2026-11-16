# Legativa — Proof of Concept (PoC)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-4B5563?style=for-the-badge)
![PyPDF](https://img.shields.io/badge/PyPDF-3776AB?style=for-the-badge)

**Inteligência Artificial para Conformidade à LGPD**

Prova de conceito da **Legativa**, uma plataforma de inteligência artificial voltada ao apoio à adequação de sistemas à Lei Geral de Proteção de Dados (LGPD).

O objetivo é validar um pipeline de *Retrieval-Augmented Generation* (RAG), capaz de recuperar informações da legislação e gerar respostas fundamentadas com suas respectivas fontes.

---

### Pré-requisitos

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

### Visão Geral

A PoC será desenvolvida em **Python e LangChain**, utilizando exclusivamente o PDF oficial da LGPD como base de conhecimento.

O experimento contempla dois fluxos:

| Fluxo | Descrição |
|---|---|
| **Ingestão e indexação** | Processamento do PDF, geração de embeddings e armazenamento vetorial em memória. |
| **Consulta e geração** | Recuperação de trechos relevantes e geração de respostas fundamentadas por uma LLM. |

### Observações

- **Execução:** via terminal, sem interface gráfica ou banco de dados persistente.
- **Instalação:** instruções de configuração e execução serão disponibilizadas durante a implementação.
- **Escopo:** exclusivamente a legislação da LGPD, sem avaliação automatizada de conformidade.

### Documentação

A documentação complementar estará disponível no diretório [`docs/`](docs/), reunindo o escopo, as decisões técnicas e os resultados de validação da PoC.

### Evolução

Os resultados deste experimento orientarão o desenvolvimento da aplicação principal da **Legativa**, mantida em um repositório independente.

---

*Projeto experimental. As respostas geradas não substituem orientação jurídica especializada.*