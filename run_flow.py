from jina import Flow
from docarray import DocumentArray
from executor import TesseractOCR

docs = DocumentArray.from_files("./data/*.png")

flow = Flow().add(uses=TesseractOCR)

with flow:
    response = flow.index(docs)

for doc in response:
    print(f"== {doc.uri} ==")
    print(doc.text)
