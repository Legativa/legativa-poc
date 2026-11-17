from pathlib import Path
from typing import Iterator

from pypdf import PdfReader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

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