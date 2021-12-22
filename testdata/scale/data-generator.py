import os
import json

num=10000
folder = f"./{num}docs"

os.makedirs(folder, exist_ok=True)

for i in range(num):
    doc = {
        "metadata": "foo",
        "namespace": f"{{\"collectionName\":\"collection{(i % 2) + 1}\"}}",
        "fullDocument":f"{{\"foo\": \"I am doc {i}\"}}"
    }
    with open(f"./{folder}/doc_{i}.json", 'w') as f:
        json.dump(doc, f, indent=2)