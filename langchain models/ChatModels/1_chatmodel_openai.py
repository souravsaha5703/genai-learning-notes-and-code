from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10) #temperature means creative level of the output we expect and max_completion_tokens means max words limit

result = model.invoke("What is the capital of india? ")

print(result)