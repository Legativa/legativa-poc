from langchain_core.vectorstores import VectorStore, VectorStoreRetriever

def build_retriever(vector_store: VectorStore) -> VectorStoreRetriever:
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},
    )