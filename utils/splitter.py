from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = text_splitter.split_documents(documents)

    return chunks