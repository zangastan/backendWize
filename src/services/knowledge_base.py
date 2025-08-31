# src/services/knowledge_base.py
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load hospital knowledge
loader = TextLoader("hospital_knowledge.txt")
documents = loader.load()

# Split documents into smaller chunks for embeddings
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS vector store
vectorstore = FAISS.from_texts([t.page_content for t in texts], embeddings)

# Function to query knowledge base
def answer_question(query: str):
    # Search for most relevant chunks
    results = vectorstore.similarity_search(query, k=3)
    
    # Build answer with recommendations
    answer = ""
    for r in results:
        content = r.page_content
        # Append only if it has department or recommendation keywords
        if any(keyword in content.lower() for keyword in ["department", "emergency", "opd", "ob/gyn", "surgery", "endoscopy", "recommendation"]):
            answer += content + "\n\n"
    
    # If nothing relevant found, give fallback guidance
    if not answer.strip():
        answer = "Please contact Wezi Medical Centre at +265 880 33 39 80 for accurate guidance."
    
    return answer.strip()

# Example usage
if __name__ == "__main__":
    query = "I have stomach pain and nausea. Which department should I visit?"
    print(answer_question(query))
