from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Write a small summary about following poem \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt',encoding='utf-8')

docs = loader.load()

# print(docs[0])

# print(type(docs[0]))

# print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)