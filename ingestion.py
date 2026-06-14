import os
import re
import json
import requests
from bs4 import BeautifulSoup

# Configutation from planning.md (characters)
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

# Target sources
SOURCES = {
    1: "https://cec.fiu.edu/about/schools-departments/mechanical-materials-engineering/research-industry/centers-labs/index.html",
    3: "https://www.cis.fiu.edu/research/",
    4: "https://solid.cs.fiu.edu/",
    5: "https://case.fiu.edu/physics/research/index.html",
    6: "https://case.fiu.edu/mathstat/",
    7: "https://news.fiu.edu/science-and-technology/",
    8: "https://fiuurj.fiu.edu/",
    12: "https://news.fiu.edu/medicine-and-health-sciences/",
    13: "https://cec.fiu.edu/students/student-organizations/index.html",
    14: "https://www.fiu.edu/research/index.html",
    15: "https://cdssec.fiu.edu/",
    16: "https://lai-afm.fiu.edu/",
    17: "https://faculty.fiu.edu/~jinhe/",
    18: "https://news.fiu.edu/research-magazine/",
    19: "https://fiuurj.fiu.edu/publishing-process/"
}

def clean_text (html_context):
    # Strips HTML boilerplate, leaving clean , contiguous text blocks
    soup = BeautifulSoup(html_context, 'html.parser')

    for element in soup(["script", "style", "header", "footer", "nav"]):
        element.decompose()
    
    text = soup.get_text(separator=' ')

    # Collapse multiple whitespaces/newlines into clean spacing
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    # Split text programatically using sliding character windows
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunk = text[start:end]
        chunks.append(chunk)
        start += (size - overlap)
        if end >= len(text):
            break
    return chunks

# Main function that is ran by the script
def run_ingestion():
    all_document_chunks = []
    print("🍔 Starting Web Ingestion and Scraping... 🍽️")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for doc_id, url in SOURCES.items():
        try:
            print(f"Scraping Source #{doc_id}: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                cleaned = clean_text(response.text)
                chunks = chunk_text(cleaned)

                for index, chunk in enumerate(chunks):
                    all_document_chunks.append({
                        "id": f"doc_{doc_id}_chunk_{index}",
                        "text": chunk,
                        "metadata": {
                            "source_id": doc_id,
                            "url": url
                        }
                    })
            else:
                print(f"⚠️ Failed to fetch source {doc_id}: Status {response.status_code}")
        except Exception as error:
            print(f"❌ Error indexing source {doc_id}: {str(error)}")
    
    # Save processed chunks locally to avoid hammering FIU servers during debugging
    os.makedirs("data", exist_ok=True)
    with open("data/chunks.json", "w") as f:
        json.dump(all_document_chunks, f, indent=4)
    print(f"✅ Ingestion complete!! Total chunks created: {len(all_document_chunks)}")

if __name__ == "__main__":
    run_ingestion()