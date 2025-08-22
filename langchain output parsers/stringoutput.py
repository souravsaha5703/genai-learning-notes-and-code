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

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a details report on {topic}",
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n  {text}",
    input_variables=['text']
)

#without parser

# prompt1 = template1.invoke({'topic':"Black hole"})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})

# result2 = model.invoke(prompt2)

# print(result2)

#withparser and using chains

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Black hole'})

print(result)