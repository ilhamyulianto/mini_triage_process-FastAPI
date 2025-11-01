from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    #check
    raise ValueError("api key not found")

app = FastAPI(title="patients triage process (FastAPI + Google LLM Model)")

class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

#prompt
prompt_template = PromptTemplate(
    input_variables=["gender", "age", "symptoms"],
    template=(
        "You are a hospital triage assistant. Based on the patient information below, "
        "recommend the most relevant specialist department.\n\n"
        "Patient gender: {gender}\n"
        "Patient age: {age}\n"
        "Symptoms: {symptoms}\n\n"
        "Return only the department name, such as 'Neurology', 'Cardiology', 'Internal Medicine', 'Radiology', 'Pediatrics', or 'Emergency Department'."
    ),
)

output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

@app.post("/recommend")
async def recommend_department(patient: PatientInfo):
    try:
        result = chain.invoke({
            "gender": patient.gender,
            "age": patient.age,
            "symptoms": ", ".join(patient.symptoms)
        })
        return {"recommended_department": result.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
