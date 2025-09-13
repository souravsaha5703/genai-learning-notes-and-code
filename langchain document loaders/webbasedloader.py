from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/iPhone-16-Pro-Max-256/dp/B0DGJ3L6LR/ref=sr_1_1?crid=1HJBOS7PKHSEE&dib=eyJ2IjoiMSJ9.CJe8fSYvhBZ8cav7vNkkwrNhwuJviL6YGVBoXBzwWQidthL8qq7YGqaSgOOivjORr27gExWQz50vxjHiL7V8s6WqTlSaQyQ8wUQR8YkO4P-I_0MtyXOuAwIRC3QsbPB_a7uIggkbuz5WjHySxoSUbatqhsXmTDehczWOe1ur6TsvxGOqxIfTnffJX7pdLs-MEcoTbJlwvD7Rx1bvogs-r4CGIvlDFCKTS7PGvJEdYes.2NRpx5TZfh9VRM_yWOu6c6HsEn_--iWBpMPBLCawFsU&dib_tag=se&keywords=iphone%2B16pro%2Bmax&nsdOptOutParam=true&qid=1757780611&sprefix=iph%2Caps%2C262&sr=8-1&th=1"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)

#Require beautifulsoup for scraping