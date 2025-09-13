from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(docs[0].page_content)

#pypdfloader only suitable for text only pdfs

