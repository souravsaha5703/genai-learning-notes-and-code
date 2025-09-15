from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

text = """
    The world of mycology, the study of fungi, is a fascinating and often misunderstood field. Fungi are not plants, as many people mistakenly believe. They belong to their own separate kingdom, distinct from both plants and animals. Unlike plants, they do not perform photosynthesis; instead, they obtain nutrients by decomposing organic matter. This crucial role makes them the primary recyclers of the planet, breaking down dead trees, leaves, and other organic material and returning vital nutrients to the soil.

    Fungi exhibit an incredible diversity of forms and functions. From the microscopic yeast used to bake bread and brew beer, to the massive, intricate mycelial networks that can span acres underground, their presence is ubiquitous. Some fungi form symbiotic relationships with plants, such as mycorrhizal fungi that connect with plant roots to exchange nutrients. Others are parasitic, causing diseases in plants and animals, while many more are saprophytic, thriving on dead or decaying matter.

    Beyond their ecological significance, fungi have a profound impact on human life. Penicillin, one of the most important antibiotics in history, was derived from the *Penicillium* fungus. Various species are also cultivated for food, from the common button mushroom to the highly prized truffle. However, the world of fungi also holds dangers, as some species are highly poisonous and can be deadly if consumed. This duality of immense benefit and potential harm makes the study of fungi a continuous and compelling journey.
"""

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=0,
    separator=''
)

# result = splitter.split_text(text)

result = splitter.split_documents(docs)

print(result[0].page_content)