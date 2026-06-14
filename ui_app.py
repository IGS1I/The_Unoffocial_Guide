import os
from dotenv import load_dotenv
from groq import Groq
from embed_and_retrieve import VectorStore

# Pull API environment keys
load_dotenv()

# Strict System Prompt establishing absolute grounding bounds
SYSTEM_PROMPT = """You are "The Unofficial Guide" conversational assistant for Florida International University undergraduates looking for research labs, clubs, and mentors.

Your responses must be STRICTLY grounded in the provided Text Context chunks.

Follow these rules without variance:
1. ONLY use details explicitly stated in the context blocks below. Do not make up facts, external URLs, names, or general knowledge.
2. If the context does not contain enough concrete information to answer the user query completely, state explicitly: "I do not have enough specific retrieved information to answer that completely based on available documentation."
3. When referencing a fact, attach inline citations using the exact Source number provided in the context format (e.g., [Source #1]).
4. Keep your tone expressive, helpful, and highly clear for an academic environment.
"""

def build_prompt_context(retrieved_chunks):
    """
    Formats retrieved context blocks cleanly for the LLM context window
    """
    context_str = "--- TEXT CONTEXT CHUNKS RECORDED FROM FIU SITES ---\n"
    for chunk in retrieved_chunks:
        context_str += f"\n[Source #{chunk['source_id']}] (URL: {chunk['url']})\n"
        context_str += f"Content: {chunk['text']}\n"
    context_str += "\n--- END OF CONTEXT ---"
    return context_str

def query_rag_pipeline(user_query, v_store, client):
    """
    RAG pipeline
    """
    # 1. Retrieve matching contexts (Top-K set to 5)
    contexts = v_store.retrieve(user_query, top_k=5)
    
    # 2. Build explicit grounding payload
    formatted_context = build_prompt_context(contexts)
    
    # 3. Generate inference via Groq
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"{formatted_context}\n\nUser Question: {user_query}"}
            ],
            temperature=0.1 # Locked down low temperature to restrict creative hallucinations
        )
        
        answer = completion.choices[0].message.content
        
        # 4. Compile dynamic source attribution tracking block
        unique_sources = {c['source_id']: c['url'] for c in contexts}
        
        print("\n========================= ANSWER =========================")
        print(answer)
        print("\n📚 SOURCE ATTRIBUTIONS USED FOR VALIDATION:")
        for source_id, url in sorted(unique_sources.items()):
            print(f" * [Source #{source_id}]: {url}")
        print("==========================================================\n")
        
    except Exception as e:
        print(f"❌ Generation Execution Failed: {str(e)}")

def main():
    """
    Main function for running Unofficial Guide
    """
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY environment variable missing inside your .env configuration.")
        return

    # Wire sub-modules up
    vector_store = VectorStore()
    vector_store.populate_database()
    client = Groq()
    
    print("\n🐾 Welcome to the FIU Unofficial Undergraduate Research Assistant!")
    print("Type 'exit' or 'quit' to terminate the process.\n")
    
    while True:
        user_input = input("🧠 Ask a question about FIU Labs/Clubs: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! Success with your academic milestones.")
            break
        if not user_input.strip():
            continue
            
        query_rag_pipeline(user_input, vector_store, client)

if __name__ == "__main__":
    main()