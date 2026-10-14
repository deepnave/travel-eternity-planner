# Retrival Augmented Generation (only)
# RAG Pipline

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from os import path

from dotenv import load_dotenv
load_dotenv()

class RAG:
    def __init__(self, sources: list[str], DB_Dir: str = "./ChromaDB"):
        self.sources = sources
    def load(self):
        return "Loaded-"+"".join(self.sources)
    

rag = RAG(["H", "i"])
print(rag.load())