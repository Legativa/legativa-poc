from pathlib import Path
from typing import Iterator

from pypdf import PdfReader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

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
    
    print(f"Páginas carregadas: {len(documents)}")

    for index, document in enumerate(documents[:3], start=1):
        print(f"\n--- Documento {index} ---")
        print(f"Página: {document.metadata['page'] + 1}")
        print(document.page_content[:500])

if __name__ == "__main__":
    main()
