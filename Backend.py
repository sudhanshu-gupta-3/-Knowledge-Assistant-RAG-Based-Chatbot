import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import RetrievalQA
# API key Setup
import os
from dotenv import load_dotenv

load_dotenv("api.env")  # Load variables from .env

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")



# ----- Load and chunk documents -----
def load_documents():
    docs = []
    data_dir = "C:\\Users\\user\\python work\\RAG CHATBOT\\Data"
    for filename in os.listdir(data_dir):
        if filename.startswith('.'):
            continue
        filepath = os.path.join(data_dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return [chunk for doc in docs for chunk in splitter.split_text(doc)]


# ----- FAISS + Embeddings -----
def create_faiss_index():
    docs = load_documents()
    chunks = chunk_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embeddings)

def get_retriever():
    db = create_faiss_index()
    return db.as_retriever()


# ----- Tools -----
def calculator_tool(query):
    try:
        expression = query.lower().split("calculate")[-1].strip()
        return eval(expression)
    except:
        return "Invalid calculation."

def dictionary_tool(query):
    word = query.lower().split("define")[-1].strip()
    return f"'{word}': [Definition not implemented – connect to a dictionary API]"


# ----- LLM Setup -----
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    temperature=0.5,
    provider="hf-inference"
)
retriever = get_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


# ----- Routing -----
def route_query(query):
    if "calculate" in query.lower():
        result = calculator_tool(query)
        route = "Calculator Tool"
    elif "define" in query.lower():
        result = dictionary_tool(query)
        route = "Dictionary Tool"
    else:
        result = qa_chain.run(query)
        route = "RAG → LLM"
    return route, result
