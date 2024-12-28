from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI() # uvicorn main:app --host 0.0.0.0 --port 8000

# Load the model and tokenizer
model_name = "aqilwahid/RSUD-MA-Fine-Tune-Gemma2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

class Query(BaseModel):
    question: str

@app.post("/chat")
async def chat(query: Query):
    user_input = query.question
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}