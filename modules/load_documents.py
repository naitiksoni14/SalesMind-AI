from langchain_community.document_loaders import TextLoader

def load_company_documents():

    loader = TextLoader(
        "knowledge/company_info.txt",
        encoding="utf-8"
    )

    return loader.load()