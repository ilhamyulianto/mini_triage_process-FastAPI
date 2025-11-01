# Mini Triage Process 

A minimal FastAPI service to recommends department based on patient information (gender, age, symptoms). Uses Google Gemini with LangChain (`langchain-google-genai`) to generate the recommendation.

---

## Features
- POST `/recommend` accepts JSON: `{ "gender","age","symptoms" }`
- Returns: `{ "recommended_department": "<DepartmentName>" }`
- Swagger UI at `/docs`
- Google AI Studio (Gemini) as LLM backend

---

## NOTE 
this REPO includes an API key for demonstration/testing context.

---

1. Clone or download the repository

2. Create and activate a virtual environment (If Needed)
   ```
   python -m venv triage_process
   triage_process\Scripts\activate 
   ```
3. Install dependencies 
   ```
   pip install -r requirements.txt
   ```
4. This repo include API KEY for Google AI Platform to interact with gemini models (gemini-2.5-flash), or you can set up own API Key from https://aistudio.google.com/api-keys and use your own Key at .env

5. Run the FastAPI app
   ```
   uvicorn app:app --reload
   ```
   and opens it on Swagger UI : http://127.0.0.1:8000/docs

6. End point test :
   -  Click POST /recommend sections and click **Try it out**
   -  Use JSON Body (accepts) :
   ```
   {
     "gender": "female",
     "age": 62,
     "symptoms": ["pusing", "mual", "sulit berjalan"]
   }
   ```
   -  Execute → see the JSON response (e.g., {"recommended_department":"Neurology"})