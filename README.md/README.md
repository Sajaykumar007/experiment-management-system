#  Experiment Management System

## Project Overview
This project demonstrates an **end-to-end experiment management system** built using modern backend and automation practices.  
It covers backend API development, LLM-based processing, automation workflows, and evaluation metrics.

The focus of this project is not just functionality, but also **real-world engineering concerns** such as:
- API design
- Automation
- Error handling
- Performance measurement
- Clear documentation

---

##  Project Structure

project-root
│
├── task1-project # Backend setup & experiment APIs
├── task2-project # LLM-based experiment execution
├── task3-project # Automation using n8n (webhooks)
├── task4-project # Evaluation & performance metrics
└── README.md


---

## 🔹 Task 1: Backend Setup & Experiment APIs

### Description
Implemented a FastAPI backend with REST APIs to manage experiments.  
This task establishes the foundation for all subsequent tasks.

### APIs Implemented
- `POST /experiments` – Create a new experiment  
- `GET /experiments` – List all experiments  
- `GET /experiments/{id}` – Get experiment by ID  

### Outcome
- Backend server setup completed
- APIs accessible via Swagger UI
- Clean request/response handling

---

## 🔹 Task 2: LLM-Based Experiment Execution (High Weight)

### Description
Implemented an API that processes user input using a **Large Language Model (LLM)**.  
This task focuses on integrating AI capabilities into the backend.

### Highlights
- Accepts user input and generates intelligent output
- Designed using `experiment_type = "llm"`
- Handles real-world API issues such as authentication and quota limits

### Note
LLM API limitations (401/429 errors) are **handled and documented**, reflecting real production scenarios.

---

## 🔹 Task 3: Automation using n8n (Event-Driven Workflow)

### Description
Implemented an **automation workflow** using n8n, triggered via a webhook whenever an experiment status update occurs.

### Highlights
- Webhook-based trigger
- Event-driven architecture
- Automation tested using Postman

### Outcome
Demonstrates how backend systems can integrate with automation tools in real-world applications.

---

## 🔹 Task 4: Experiment Evaluation & Metrics

### Description
Implemented evaluation logic to measure experiment performance and output quality.

### Metrics Captured
- Execution time (in seconds)
- Output quality (Good / Average / Failed)
- Evaluation score
- Final experiment status

### Outcome
Moves beyond execution to **analysis and monitoring**, reflecting experimentation best practices.

---

## 🚀 How to Run (Quick Start)

```bash
# Clone the repository
git clone <repository-url>
cd project-root

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

# Navigate to any task folder and install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs
