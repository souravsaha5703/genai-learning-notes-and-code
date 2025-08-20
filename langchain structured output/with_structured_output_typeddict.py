#No data validation in typeddict
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    summery:Annotated[str,"A breif summary of the review"]
    sentiment:str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated.
There are too many pre-installed apps that i can;t remove. Also, the UI looks outdated
compared to other brands. Hoping for a software update to fix this.""")

print(result)
print("Summary is -",result['summery'])
print("Sentiment of the product is -",result['sentiment'])