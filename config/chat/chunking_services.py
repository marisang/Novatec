from langchain_community.document_loaders import Docx2txtLoader
from models import Cliente, Projeto, Contrato, Chunk
from langchain_text_splitters import RecursiveCharacterTextSplitter

def carregar_docx_do_model(instancia):
    caminho = instancia.arquivo.path   # caminho físico completo, ex: /home/projeto/media/documentos/arquivo.docx
    loader = Docx2txtLoader(caminho)
    docs = loader.load()
    return docs

def chunkar_contrato(texto_contrato):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        separators=[
            "\nCLÁUSULA",      
            "\nCláusula",
            "\n\d+\.\d+",     
            "\n\n",
            "\n",
            ". ",
            " "
        ]
    )
    texto_chunks = splitter.split_documents(texto_contrato)
    return texto_chunks