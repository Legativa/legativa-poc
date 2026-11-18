# Legativa — Validação da Prova de Conceito

## 1. Objetivo

Registrar os experimentos realizados com o pipeline RAG da Legativa PoC, observando a recuperação de informações da LGPD, a geração de respostas e a rastreabilidade dos trechos utilizados.

Os testes foram realizados manualmente, por meio de consultas e inspeção dos conteúdos recuperados e das respostas geradas.

## 2. Perguntas de Teste

| ID | Pergunta | Aspecto avaliado |
|---|---|---|
| Q1 | Quais são os princípios previstos na LGPD para o tratamento de dados pessoais? | Recuperação de disposições específicas |
| Q2 | Em quais hipóteses o tratamento de dados pessoais pode ocorrer? | Recuperação de informações jurídicas |
| Q3 | Quais direitos a LGPD assegura aos titulares de dados? | Recuperação e síntese de informações |
| Q4 | Um sistema pode coletar qualquer dado pessoal desde que o usuário forneça consentimento? | Interpretação fundamentada |

As quatro questões foram contempladas, utilizando as formulações originais ou variações durante os experimentos.

## 3. Critérios de Avaliação

| Critério | O que verificar |
|---|---|
| **Recuperação** | Os chunks recuperados contêm informações pertinentes à pergunta? |
| **Fundamentação** | A resposta é compatível com os trechos recuperados? |
| **Rastreabilidade** | É possível identificar os trechos e páginas utilizados? |
| **Limitações** | A resposta apresenta informações incorretas, insuficientes ou sem respaldo nas fontes? |

## 4. Registro dos Experimentos

### E1 — Direitos dos titulares

**Pergunta:** Quais são os direitos dos titulares de dados pessoais?

**Trechos recuperados:** Arts. 17 e 18, incluindo o início e a continuação da lista de direitos, além de definições do art. 5º.

**Resposta gerada:** A LLM apresentou os direitos previstos nos incisos I a VIII do art. 18, mas omitiu o inciso IX, referente à revogação do consentimento.

**Resultado:** Recuperação pertinente, mas com omissão de informação que estava presente nos trechos fornecidos à LLM.

---

### E2 — Bases legais para o tratamento

**Pergunta:** Quais são as bases legais para o tratamento de dados pessoais?

**Trechos recuperados:**

- **Página 6:** art. 10 — legítimo interesse.
- **Página 4:** art. 6º — princípios do tratamento.
- **Página 10:** art. 18 — direitos dos titulares.
- **Página 17:** arts. 46 e 47 — segurança da informação.

**Resposta gerada:** A LLM apresentou os seguintes dispositivos como bases legais:

> - **Art. 18:** Informa o titular sobre o fato do tratamento e os meios para exercer seus direitos.
> - **Art. 10:** Fundamenta o legítimo interesse do controlador, incluindo apoio às suas atividades e proteção dos direitos do titular.
> - **Art. 8º, § 5º:** Permite a revogação do consentimento pelo titular.

**Resultado:** O Retriever não recuperou a lista do art. 7º. A resposta confundiu direitos dos titulares e revogação do consentimento com bases legais para o tratamento.

---

### E3 — Princípios da LGPD

**Pergunta:** Quais são os princípios que devem orientar o tratamento de dados pessoais segundo a LGPD?

**Trechos recuperados:** Chunks referentes ao art. 6º, acompanhados de conteúdos de outros dispositivos jurídicos.

**Resposta gerada:** A enumeração apresentou corretamente os primeiros princípios, mas misturou informações a partir do inciso X.

Trechos da resposta:

> X - responsabilização e prestação de contas: demonstração, pelo agente, da adoção de privacidade, bem como sobre relatórios de impacto à proteção de dados pessoais [...]

> XIV - ouvir os agentes de tratamento e a sociedade em matérias de interesse relevante e prestar contas sobre suas atividades e planejamento [...]

**Resultado:** A LLM misturou princípios do art. 6º com incisos referentes às competências da ANPD.

---

### E4 — Enumeração dos princípios com contexto reduzido

**Pergunta:** Liste apenas os nomes dos dez princípios previstos no art. 6º da LGPD, sem explicar cada um.

**Trechos recuperados:** Foram utilizados somente os dois primeiros chunks. O primeiro continha os incisos I a V do art. 6º, com o inciso V incompleto. O segundo continha disposições relativas ao tratamento de dados pelo poder público.

**Resposta gerada:** A LLM apresentou os cinco primeiros princípios corretamente, mas completou a lista com:

> 6. Informação
> 7. Encargado
> 8. Publicidade
> 9. Transparência
> 10. Proteção

Em outra execução com contexto reduzido, a geração terminou no meio da descrição do inciso V, com `done_reason=stop` e 201 tokens gerados.

**Resultado:** Foram observadas respostas incompletas e complementação da lista com informações incorretas, mesmo quando o contexto não continha os dez princípios.

---

### E5 — Ajuste das instruções do prompt

**Pergunta:** Liste apenas os nomes dos dez princípios previstos no art. 6º da LGPD, sem explicar cada um.

**Trechos recuperados:** Foram enviados os quatro chunks retornados pelo Retriever. O prompt recebeu instruções adicionais para reconhecer contexto insuficiente e evitar a mistura de dispositivos jurídicos.

**Resposta gerada:** A LLM apresentou corretamente os cinco primeiros princípios, mas continuou com:

> 6. Informação
> 7. Consentimento
> 8. Obrigação legal
> 9. Estudos por órgão de pesquisa
> 10. Proteção da vida ou da incolumidade física

**Resultado:** As instruções adicionais não impediram a geração de informações incorretas. O modelo também não indicou insuficiência do contexto.

---

### E6 — Consulta simplificada sobre direitos

**Pergunta:** Quais são os direitos dos titulares?

**Trechos recuperados:**

- **Página 5:** hipóteses legais para o tratamento de dados.
- **Página 10:** continuação do art. 18, incluindo incisos VII a IX e parágrafos.
- **Página 6:** art. 10 — legítimo interesse.
- **Página 3:** art. 5º — definições jurídicas.

**Resposta gerada:** A LLM destacou o art. 18 e seus §§ 1º a 3º, apresentando, entre outras, a seguinte afirmação:

> **Art. 18:** O titular dos dados pessoais tem o direito de ser informado sobre o tratamento de seus dados, incluindo os meios pelos quais poderá exercer seus direitos.

**Resultado:** O início do art. 18 não foi recuperado. A resposta se concentrou nos procedimentos de exercício dos direitos e omitiu sua lista principal.

---

### E7 — Consulta simplificada sobre bases legais

**Pergunta:** Quais são as bases legais?

**Trechos recuperados:**

- **Página 6:** art. 10 — legítimo interesse.
- **Página 4:** art. 6º — princípios do tratamento.
- **Página 17:** arts. 46 e 47 — segurança da informação.
- **Página 24:** competências da ANPD.

**Resposta gerada:**

> De acordo com o contexto fornecido, as bases legais são:
>
> - Art. 18
> - Art. 10
> - Art. 47

**Resultado:** O art. 7º novamente não foi recuperado. A LLM apresentou dispositivos que não constituem bases legais como resposta à consulta.

---

### E8 — Consentimento e coleta de dados pessoais

**Pergunta:** Um sistema pode coletar qualquer dado pessoal desde que o usuário forneça consentimento?

**Trechos recuperados:**

- **Página 3:** art. 5º — definição de consentimento.
- **Página 8:** art. 14 — tratamento de dados de crianças.
- **Página 4:** art. 7º — hipóteses de tratamento.
- **Página 9:** art. 14 — requisitos relacionados ao tratamento de dados de crianças.

**Resposta gerada:** A LLM respondeu negativamente à pergunta.

Trechos da resposta:

> Não, um sistema não pode coletar qualquer dado pessoal desde que o usuário forneça consentimento.

> Portanto, o consentimento deve ser específico, informado e inequívoco, e o controlador deve garantir que o consentimento seja dado pelo responsável pela criança, quando aplicável.

**Resultado:** A conclusão geral foi correta, mas a fundamentação priorizou regras específicas sobre dados de crianças. O princípio da necessidade, previsto no art. 6º, III, não foi recuperado.

---

## 5. Conclusões

Os experimentos confirmaram o funcionamento integrado do pipeline RAG, desde a recuperação de documentos até a geração de respostas.

A recuperação apresentou resultados variados. Algumas consultas localizaram dispositivos pertinentes, enquanto outras retornaram informações relacionadas ao assunto, mas insuficientes para responder adequadamente. A fragmentação dos artigos e a formulação das perguntas influenciaram os resultados observados.

Na geração, ocorreram omissões, respostas incompletas, mistura de dispositivos jurídicos e informações incorretas. O ajuste do prompt não eliminou esses comportamentos, especialmente quando o contexto recuperado era insuficiente.

Também foi observada demora na geração das respostas durante a interação pelo terminal, sem medições quantitativas de latência.

A realização do experimento foi fundamental para sentir, na prática, as dificuldades de contruir um sistema RAG e identificar aspectos que não ficariam evidentes apenas pelo estudo teórico. Além disso, abrimos um leque de preocupações que precisarão sem consideradas para a evolução do projeto. Agora temos uma base mais sólida para as decisões técnicas e arquiteturais que orientarão a V1.