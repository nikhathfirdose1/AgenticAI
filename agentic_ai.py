import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Load the document content
with open("sample.txt", "r") as f:
    text_content = f.read()

# Generate embedding using Gemini
embedding_response = genai.embed_content(
    model="models/embedding-001",
    content=text_content,
    task_type="retrieval_document" 
)

# Output (you can store this in a vector DB like FAISS)
embedding = embedding_response["embedding"]
print("\nFirst 10 embedding vector values:\n", embedding[:10])
print(f"\nFull embedding vector length: {len(embedding)}")