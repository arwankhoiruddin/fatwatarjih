from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.retrievers import ParentDocumentRetriever

## Text Splitting & Docloader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.storage import InMemoryStore
from langchain.document_loaders import TextLoader

import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''
os.environ['OPENAI_API_KEY'] = ''

# model_name = 'openai/gpt-3.5-turbo'
model_name = "BAAI/bge-small-en-v1.5"
encode_kwargs = {'normalize_embeddings': True} 

bge_embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs={'device': 'cpu'},
    encode_kwargs=encode_kwargs
)
