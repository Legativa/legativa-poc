from pathlib import Path
from typing import Iterator

from pypdf import PdfReader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

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
    
    print(f"Páginas carregadas: {len(documents)}")
    print(f"Chunks gerados {len(chunks)}")

    for index, chunk in enumerate(chunks[:5], start=1):
        print(f"\n--- Chunk {index} ---")
        print(f"Página: {chunk.metadata['page'] + 1}")
        print(f"Posição inicial: {chunk.metadata.get('start_index')}")
        print(f"Caracteres: {len(chunk.page_content)}")
        print(chunk.page_content)

if __name__ == "__main__":
    main()
