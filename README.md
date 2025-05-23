# SurgiAssist AI

SurgiAssist AI is a real-time medical assistant powered by **PubMed retrieval** and **Cerebras’ Qwen-3-32b model**.  
It answers clinical questions using evidence-backed, fast, and empathetic AI responses.


## Features

-  Uses real PubMed abstracts for accuracy
-  Fast inference with Cerebras cloud API
-  Shows clear “Thought Process” before “Final Answer”
-  Streamlit UI — demo-ready, simple and clean
-  Displays all abstract sources used
-  Friendly tone with graceful fallback for non-medical queries


## 🧰 Tech Stack

| Layer        | Tech                                |
|--------------|-------------------------------------|
| Inference    | Cerebras Qwen-3-32b                 |
| Retrieval    | PubMed API                          |
| Backend      | FastAPI + httpx                     |
| Frontend     | Streamlit                           |
| Config       | Python + dotenv                     |

---

## ⚙️ Setup Instructions

### 📁 1. Clone the Repository

```bash
git clone https://github.com/your-username/surgiassist-ai.git
cd surgiassist-ai
```
### 2. Create Environment File
Create a file called .env inside the /app folder:
```
# .env
CEREBRAS_API_KEY=your-cerebras-key
PUBMED_API_KEY=your-pubmed-key   # optional, for higher PubMed fetch rate
```

### 3. Install All Dependencies
Install required packages with:
```
pip install -r requirements.txt
```
Or if using a virtual environment:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### 4. Run the Application
Start the Backend:
```
cd app
uvicorn backend:app --reload
```

Start the Frontend (in another terminal)

```
streamlit run frontend.py
```

### Screenshot 
<img width="600" alt="image" src="https://github.com/user-attachments/assets/7804bfb8-7f50-46b0-9c4a-1ab885f11a8b" />

### Project Structure
SurgiAssistAI/
├── app/
│   ├── backend.py
│   ├── frontend.py
│   ├── fetch_pubmed.py
│   ├── .env.template
├── requirements.txt
├── README.md

