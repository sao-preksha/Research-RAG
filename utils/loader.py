from langchain_community.document_loaders import PyPDFDirectoryLoader
import re

def clean_text(text):

    text = re.sub(
        r'(?<=[a-z])(?=[A-Z])',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    text = text.replace("ﬁ", "fi")
    text = text.replace("ﬂ", "fl")

    return text.strip()

def load_pdfs():

    loader = PyPDFDirectoryLoader("data")

    documents = loader.load()

    for doc in documents:

        doc.page_content = clean_text(
            doc.page_content
        )

    return documents