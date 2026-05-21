from utils.loader import load_pdfs
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model

from langchain_community.vectorstores import Chroma

documents = load_pdfs()

print(f"Loaded {len(documents)} pages")

chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks")

embeddings = get_embedding_model()

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vectordb"
)

db.persist()

print("Vector DB created successfully")
