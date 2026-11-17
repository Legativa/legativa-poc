from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

def build_chain():
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            Você é um assistente especializado na LGPD.

            Responda utilizando exclusivamente as informações do contexto fornecido.

            Antes de responder, verifique se o contexto contém todas as
            informações necessárias para atender à pergunta.

            Regras:
            - Não invente informações ou dispositivos legais.
            - Não complete lacunas utilizando conhecimento externo.
            - Não misture incisos pertencentes a artigos diferentes.
            - Se o contexto estiver incompleto, apresente somente as
              informações disponíveis e indique explicitamente a limitação.
            - Indique os artigos utilizados quando presentes no contexto.

            Contexto:
            {context}
            """
        ),
        ("human", "{question}")
    ])

    llm = ChatOllama(
        model="gemma3:4b",
        temperature=0,
    )

    return prompt | llm