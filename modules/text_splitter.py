from langchain_text_splitters import RecursiveCharacterTextSplitter

# Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

# Function to split LangChain documents
def split_documents(documents):
    return text_splitter.split_documents(documents)