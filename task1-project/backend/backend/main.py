from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.directus import (
    create_experiment_directus,
    list_experiments_directus,
    get_experiment_by_id_directus
)

app = FastAPI()

class ExperimentCreate(BaseModel):
    name: str
    experiment_type: str = "llm"
    status: str = "created"

# ✅ POST /experiments (ONLY ONCE)
@app.post("/experiments")
def create_experiment(exp: ExperimentCreate):
    try:
        return create_experiment_directus(exp.dict())
    except Exception as e:
        print("Directus Error:", e)   # 🔥 Debug print
        raise HTTPException(status_code=400, detail=str(e))

# ✅ GET /experiments
@app.get("/experiments")
def list_experiments():
    return list_experiments_directus()

# ✅ GET /experiments/{id}
@app.get("/experiments/{id}")
def get_experiment(id: int):
    try:
        return get_experiment_by_id_directus(id)
    except Exception as e:
        print("Fetch Error:", e)
        raise HTTPException(status_code=404, detail="Experiment not found")
