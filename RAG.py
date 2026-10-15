# Retrival Augmented Generation (only)
# RAG Pipline

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from os import path

from dotenv import load_dotenv
load_dotenv()

class RAG:
    def __init__(self, source_path: str, DB_Dir: str = "./ChromaDB"):
        self.__source_path = source_path
    def load(self):
        text_loader = DirectoryLoader(
            path=self.__source_path,
            glob="./*.txt",
            loader_cls=TextLoader,
            loader_kwargs={"autodetect_encoding": True},
        )

        pdf_loader = DirectoryLoader(
            path=self.__source_path,
            glob="./*.pdf",
            loader_cls=PyPDFLoader,
        )

        text_documents = text_loader.load()
        pdf_documents = pdf_loader.load()

        return text_documents, pdf_documents

        # self.__text_documents = text_documents
        # self.__pdf_documents = pdf_documents

    def chunk(self, chunking_func = RecursiveCharacterTextSplitter, size = 500, overlap = 75):
        text_documents, pdf_documents = self.load()
        splitter = chunking_func(chunk_size=size, chunk_overlap=overlap)
        # chunks = []
        if len(text_documents) >= 1:
            chunks += splitter.split_documents(text_documents)
        if len(pdf_documents) >= 1:
            chunks = splitter.split_documents(pdf_documents)
        print(chunks)
        
        

    

if __name__ == "__main__":
    my_RAG = RAG("./documents/")
    my_RAG.chunk()