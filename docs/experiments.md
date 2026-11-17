# Legativa — Validação da Prova de Conceito

## 1. Objetivo

Registrar os experimentos realizados para verificar o funcionamento do pipeline RAG, considerando a qualidade da recuperação, a fundamentação das respostas e a rastreabilidade das fontes.

## 2. Perguntas de Teste

| ID | Pergunta | Aspecto avaliado |
|---|---|---|
| Q1 | Quais são os princípios previstos na LGPD para o tratamento de dados pessoais? | Recuperação de disposições específicas |
| Q2 | Em quais hipóteses o tratamento de dados pessoais pode ocorrer? | Recuperação de informações jurídicas |
| Q3 | Quais direitos a LGPD assegura aos titulares de dados? | Recuperação e síntese de informações |
| Q4 | Um sistema pode coletar qualquer dado pessoal desde que o usuário forneça consentimento? | Interpretação fundamentada |

As perguntas devem ser ajustadas e ampliadas conforme os resultados.

## 3. Critérios de Avaliação

| Critério | O que verificar |
|---|---|
| **Recuperação** | Os chunks recuperados contêm informações pertinentes à pergunta? |
| **Fundamentação** | A resposta é compatível com os trechos recuperados? |
| **Rastreabilidade** | É possível identificar os trechos e páginas utilizados? |
| **Limitações** | A resposta apresenta informações incorretas, insuficientes ou sem respaldo nas fontes? |

## 4. Registro dos Experimentos

Para cada consulta, registrar:

- **Pergunta:** identificação do caso de teste.
- **Trechos recuperados:** conteúdo e páginas de origem.
- **Resposta gerada:** resultado produzido pela LLM.
- **Avaliação:** observações sobre recuperação, fundamentação e rastreabilidade.
- **Problemas identificados:** eventuais falhas ou limitações.

Os resultados serão preenchidos durante a execução dos testes, preservando as evidências necessárias para análise posterior.

## 5. Conclusões

*Seção reservada para a consolidação dos resultados.*

Ao final dos experimentos, serão registrados os principais acertos, dificuldades e possíveis melhorias identificadas para orientar a evolução da Legativa.