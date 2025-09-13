from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

#load for small amount of documents

# docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

#lazy load for large amount of documents

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)