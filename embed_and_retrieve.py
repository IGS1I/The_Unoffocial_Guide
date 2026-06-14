import json
import os
import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        # Local persistent database path
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")
        # Load embedding model matching planning.md
        self.model = SentenceTransformer('BAAI/bge-small-en-v1.5')
        
        # Get or create collection
        self.collection = self.chroma_client.get_or_create_collection(name="fiu_research_guide")

    def populate_database(self):
        """ 
        Loads chunks from JSON and updates the Vector Database
        """
        if not os.path.exists("data/chunks.json"):
            print("❌ No processed data found. Run ingest.py first!")
            return
            
        with open("data/chunks.json", "r") as f:
            chunks = json.load(f)
            
        if self.collection.count() > 0:
            print("🔄 Database already populated. Skipping database generation.")
            return

        print("🖥️ Computing embeddings and initializing ChromaDB...")
        
        ids = [c["id"] for c in chunks]
        documents = [c["text"] for c in chunks]
        metadatas = [c["metadata"] for c in chunks]
        
        # Encode chunks in batches
        embeddings = self.model.encode(documents, show_progress_bar=True).tolist()
        
        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"✅ Embedded {self.collection.count()} vectors into vector database.")

    def retrieve(self, query, top_k=5):
        """ 
        Performs vector search matching the Top-k spec
        """
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        formatted_results = []
        if results and results['documents']:
            for i in range(len(results['documents'][0])):
                formatted_results.append({
                    "text": results['documents'][0][i],
                    "url": results['metadatas'][0][i]['url'],
                    "source_id": results['metadatas'][0][i]['source_id']
                })
        return formatted_results

if __name__ == "__main__":
    vector_store = VectorStore()
    vector_store.populate_database()
    
    # Test query
    sample_results = vector_store.retrieve("Undergraduate Research Journal publishing steps", top_k=1)
    print("\n🔍 Test Retrieval Output Preview:")
    for res in sample_results:
        print(f"\n[Source #{res['source_id']}] -> {res['text'][:150]}...")