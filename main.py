from pathlib import Path
from typing import Iterator

from pypdf import PdfReader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

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

    question = "O que deve acontecer quando ocorre um incidente de segurança envolvendo dados pessoais?"

    retrieved_docs = retriever.invoke(question)

    print(f"\nPergunta: {question}")
    print(f"Chunks recuperados: {len(retrieved_docs)}")
    
    for index, doc in enumerate(retrieved_docs, start=1):
        print(f"\n--- Resultado {index} ---")
        print(f"Página: {doc.metadata['page'] + 1}")
        print(f"Posição inicial: {doc.metadata.get('start_index')}")
        print(doc.page_content)

if __name__ == "__main__":
    main()
