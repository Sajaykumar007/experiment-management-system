from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm import summarize_text

app = FastAPI()

class Task2Input(BaseModel):
    input_text: str

@app.post("/run-task2")
def run_task2(data: Task2Input):
    try:
        output = summarize_text(data.input_text)
        return {
            "status": "completed",
            "input": data.input_text,
            "output": output
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
