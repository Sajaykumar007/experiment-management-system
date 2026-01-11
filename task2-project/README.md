## Task 2: LLM-Based Experiment Execution (High Weight)

Integrated an LLM-based processing pipeline that accepts user input and generates intelligent output.

Why this matters:

Demonstrates understanding of LLM workflows

Handles real-world API constraints such as authentication and quota limits

Errors and limitations are explicitly documented rather than hidden

This task emphasizes design thinking over hardcoding responses.

Task 2: LLM-Based Experiment Execution
## Overview

Task 2 implements an API that processes user input using a Large Language Model (LLM).
The task demonstrates LLM integration concepts, request/response handling, and real-world API error management.

## Tech Stack

Python

FastAPI

OpenAI SDK (LLM integration)

REST APIs

Swagger UI

🚀 How to Run
# Navigate to Task 2 project
cd task2-project

# Activate virtual environment
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

🔗 API Implemented

POST /run-task2 – Process user input using an LLM and return generated output

# Sample Request
{
  "input_text": "Artificial Intelligence is transforming software development."
}

# Sample Response
{
  "status": "completed",
  "output": "AI is transforming modern software development."
}

## Error Handling & Limitations

Handles authentication errors (401)

Handles quota limitations (429)

In case of LLM API limits, errors are logged and documented

Note: LLM quota/billing limitations may prevent live responses during testing.


## Task 2 Outcome

LLM integration logic implemented

API request/response structure defined

Real-world API constraints handled and documented