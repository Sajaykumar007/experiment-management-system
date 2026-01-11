from fastapi import FastAPI
import time

app = FastAPI()

@app.post("/run-task4")
def run_task4(data: dict):
    """
    TASK 4:
    - Execution time measure pannum
    - Output evaluate pannum (score, quality)
    """

    # 🔹 STEP 3: Execution time start
    start_time = time.time()

    # 🔹 Dummy processing (LLM maadhiri)
    text = data.get("input_text", "")
    output = text.upper()

    # 🔹 STEP 3: Execution time end
    end_time = time.time()
    execution_time = round(end_time - start_time, 2)

    # 🔹 STEP 4: Evaluation logic
    if not output:
        score = 0
        quality = "Failed"
        status = "failed"

    elif len(output) < 20:
        score = 4
        quality = "Average"
        status = "completed"

    else:
        score = 8
        quality = "Good"
        status = "completed"

    # 🔹 Final response
    return {
        "status": status,
        "output": output,
        "execution_time_sec": execution_time,
        "evaluation": {
            "score": score,
            "quality": quality
        }
    }

