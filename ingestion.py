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

def clean_text(html_content):
    """
    Strips navigation boilerplate, menus, sidebars, and empty elements
    to isolate informative paragraphs.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Broadly decompose known boilerplate and layout containers
    boilerplate_selectors = [
        "script", "style", "header", "footer", "nav", "aside",
        ".navigation", ".menu", ".sidebar", ".footer", ".header",
        "#navigation", "#sidebar", "#footer", "#header",
        ".menu-container", ".nav-menu", ".breadcrumbs", ".search-box",
        ".fiu-footer", ".fiu-header", "#fiu-responsive-menu"
    ]
    
    for selector in boilerplate_selectors:
        # Handle both raw tags and CSS classes/IDs
        for element in soup.select(selector):
            element.decompose()

    # 2. Try to pinpoint the primary content container if it exists
    # Many FIU and university pages wrap main text in these semantic structures
    content_areas = soup.select("main, article, #main-content, .main-content, #content, .content")
    
    if content_areas:
        # If we found a dedicated main content wrapper, prioritize it
        working_soup = BeautifulSoup(" ".join([str(c) for c in content_areas]), 'html.parser')
    else:
        # Fallback to the cleaned body if no clear main wrapper is defined
        working_soup = soup

    # 3. Target informative blocks (paragraphs, list items, headers)
    text_blocks = []
    # Gathering text from elements likely to hold actual academic/club data
    for element in working_soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li', 'td']):
        block_text = element.get_text(separator=' ').strip()
        
        # Clean up internal whitespace anomalies
        block_text = re.sub(r'\s+', ' ', block_text)
        
        # Filter out short text fragments (e.g., "Home", "Apply Now", "Next")
        # An informative phrase usually requires more than 4 words
        if len(block_text.split()) > 4:
            text_blocks.append(block_text)
            
    # Combine the high-quality text blocks with clean paragraph breaks
    cleaned_text = "\n\n".join(text_blocks)
    return cleaned_text

def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """ 
    Split text programatically using sliding character windows
    """
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

def run_ingestion():
    """
    Main function that is ran by the script
    """
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