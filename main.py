from docarray import DocumentArray
from jina import Flow
from pdf_segmenter import PDFSegmenter

# print-to-pdf of https://courses.cs.vt.edu/csonline/AI/Lessons/VisualProcessing/OCRscans_files/bowers.jpg
docs = DocumentArray.from_files(["/Users/aswin/Documents/misc/anu/glm-130b.pdf"],)

print(docs.summary())

print(docs[0].summary())

for doc in docs:
  doc.load_uri_to_blob()

flow = Flow(protocol='http',timeout_ctrl=100000,timeout_ready=100000,timeout_send=100000, prefetch=1)\
    .add(uses=PDFSegmenter, name="segmenter", install_requirements=True,
)

with flow:
    output = flow.index(docs, return_results=True)


# print(output.summary())

# for o in output:
#     print('-----------------')
#     print(o.summary())
#     print(len(o.chunks))