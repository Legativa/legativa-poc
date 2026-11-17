from pathlib import Path
from rag.loader import PDFLoader
from rag.indexing import build_vector_store
from rag.retrieval import build_retriever
from rag.generation import build_chain

PDF_PATH = Path(__file__).resolve().parent / "documents" / "lgpd.pdf"

def main():
    loader = PDFLoader(PDF_PATH)
    documents = loader.load()

    vector_store = build_vector_store(documents)
    retriever = build_retriever(vector_store)

    chain = build_chain()

    print("\nLegativa PoC — Consultas à LGPD")
    print("Digite 'sair' para encerrar.")

    while True:
        question = input("\nPergunta: ").strip()

        if question.lower() == "sair":
            break

        if not question:
            continue

        retrieved_docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in retrieved_docs
        )

        response = chain.invoke({
            "context": context,
            "question": question,
        })

        print(f"\nResposta:\n{response.content}")

        print("\n--- Fontes recuperadas ---")
        for index, doc in enumerate(retrieved_docs, start=1):
            print(f"\n[{index}] Página {doc.metadata['page'] + 1}")
            print(doc.page_content)

if __name__ == "__main__":
    main()
