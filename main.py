from pathlib import Path
from typing import Iterator

from pypdf import PdfReader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

PDF_PATH = Path(__file__).resolve().parent / "documents" / "lgpd.pdf"

class PDFLoader(BaseLoader):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def lazy_load(self) -> Iterator[Document]:
        reader = PdfReader(self.file_path)

        for index, page in enumerate(reader.pages):
            yield Document(
                page_content=page.extract_text() or "",
                metadata={
                    "source": str(self.file_path),
                    "page": index,
                },
            )

def main():
    loader = PDFLoader(PDF_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=True
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-small",
        model_kwargs={"device": "cpu"},
        encode_kwargs={
            "normalize_embeddings": True,
            "prompt": "passage: ",
        },
        query_encode_kwargs={
            "normalize_embeddings": True,
            "prompt": "query: ",
        }
    )

    vector_store = InMemoryVectorStore(embedding=embeddings)
    ids = vector_store.add_documents(chunks)

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    question = "Liste apenas os nomes dos dez princípios previstos no art. 6º da LGPD, sem explicar cada um."
    
    retrieved_docs = retriever.invoke(question)

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


    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    llm = ChatOllama(
        model="gemma3:4b",
        temperature=0
    )

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question,
    })

    print("\n--- Resposta da Legativa ---")
    print(response.content)

if __name__ == "__main__":
    main()
