#Using pydantic for data validation
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel,Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Review(BaseModel):
    key_themes:list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summery:str = Field(description="A breif summary of the review")
    sentiment:str = Field(description="Sentiment of the user")
    pros: Optional[list[str]] = Field(default=None,description="Write down all the pros inside a list")
    cons:Optional[list[str]] = Field(default=None,description="Write down all the cons inside a list")

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

result_dict = dict(result)

print(result_dict)

print("Summary is - ",result_dict['summery'])
print("Sentiment of the product is - ",result_dict['sentiment'])
print("Key themes are - ",result_dict['key_themes'])
print("All the pros are - ",result_dict['pros'])
print("All the cons are - ",result_dict['cons'])