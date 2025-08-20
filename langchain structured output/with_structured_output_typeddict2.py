#No data validation in typeddict
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    key_themes:Annotated[list[str],"Write down all the key themes discussed in the review in a list"]
    summery:Annotated[str,"A breif summary of the review"]
    sentiment:str
    pros: Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Sourav Saha""")

print("Summary is - ",result['summery'])
print("Sentiment of the product is - ",result['sentiment'])
print("Key themes are - ",result['key_themes'])
print("All the pros are - ",result['pros'])
print("All the cons are - ",result['cons'])