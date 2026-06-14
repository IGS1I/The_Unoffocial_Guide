from embed_and_retrieve import VectorStore

def run_retrieval_evaluation():
    """
    Initialize the vector store manager and ensure db is populated
    """
    vector_store = VectorStore()
    vector_store.populate_database()
    
    # 5 Test Questions directly from your planning.md evaluation plan
    eval_questions = {
        1: "What sorts of labs does FIU have in its engineering college?",
        2: "What research does FIU have in physics?",
        3: "Is there any recent research news at FIU, and where can I find it?",
        4: "Are there any clubs at FIU that have roots in projects and research in science and technology?",
        5: "How can undergraduates at FIU get their research seen and/or published from the university?"
    }
    
    print("🧪 STARTING RETRIEVAL APPROACH EVALUATION\n")
    print("-" * 60)
    
    for query_id, question in eval_questions.items():
        print(f"\n📋 [Question #{query_id}]: \"{question}\"")
        print(f"🔍 Fetching top-k=3 closest chunks using bge-small-en-v1.5...\n")
        
        # Retrieve the top 3 chunks to evaluate quality concisely
        results = vector_store.retrieve(question, top_k=3)
        
        if not results:
            print("  ❌ [RETRIEVAL FAILED]: No chunks returned.")
            continue
            
        for index, result in enumerate(results, start=1):
            # Clean up newlines for cleaner terminal scanning
            snippet = result['text'][:200].replace('\n', ' ').strip()
            print(f"  🔹 Match {index} (Source #{result['source_id']}):")
            print(f"     URL: {result['url']}")
            print(f"     Snippet: {snippet}...\n")
            
        print("-" * 60)

if __name__ == "__main__":
    run_retrieval_evaluation()