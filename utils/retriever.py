from langchain_community.vectorstores import Chroma
from utils.embeddings import get_embedding_model

def get_retriever():

    embeddings = get_embedding_model()

    db = Chroma(
        persist_directory="vectordb",
        embedding_function=embeddings
    )

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 6,
            "fetch_k": 20
        }
    )

    return retriever