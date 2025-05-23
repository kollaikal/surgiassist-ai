from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
import os
from fetch_pubmed import fetch_pubmed_data

# Load API keys
load_dotenv()
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")

# Initialize Cerebras client
client = Cerebras(api_key=CEREBRAS_API_KEY)

# FastAPI app setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data["question"]

    # Fetch abstracts from PubMed based on user query
    pubmed_docs = fetch_pubmed_data(question, num_results=5)
    context = "\n---\n".join(doc["abstract"] for doc in pubmed_docs)

    # Construct multi-turn prompt
    prompt = (
    "You are a compassionate, knowledgeable medical assistant AI. Your job is to provide medically accurate answers based on the given PubMed abstracts. "
    "If the question is not strictly medical, respond politely with empathy and professionalism. "
    "Always prioritize clinical clarity, but feel free to sound human and supportive.\n\n"
    f"User Question:\n{question}\n\n"
    f"Relevant Medical Abstracts:\n{context}\n\n"
    "First, think step-by-step if any of the provided abstracts relate to the question. "
    "Then clearly separate your final answer like this:\n\n"
    "### Thought Process\n<your reasoning>\n\n"
    "### Final Answer\n<your answer to the user>"
)



    try:
        # Call Cerebras model using SDK
        chat_completion = client.chat.completions.create(
            model="qwen-3-32b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        answer = chat_completion.choices[0].message.content

    except Exception as e:
        answer = f" Cerebras API Error: {str(e)}"

    return {
        "answer": answer,
        "sources": [doc["abstract"] for doc in pubmed_docs]
    }
