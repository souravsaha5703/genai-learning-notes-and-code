from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Create a small twitter post on this {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Create a small linkedin post on this {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedinPost': RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'Cyber Security'})

print(result['tweet'])
print(result['linkedinPost'])