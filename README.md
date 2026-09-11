The goal is to convert an unstructured meeting transcript into structured data that can later be reviewed and transferred to an internal business system.

Process

The proposed workflow is:

Meeting transcript → FastAPI → LLM analysis → Structured JSON → Validation → Human approval → Internal business system

The LLM extracts:

Client requirements
Meeting summary
Decisions
Next steps / action items
Responsible persons
Deadlines
Project Structure
project/
├── main.py
├── models.py
├── llm_service.py
├── requirements.txt
└── README.md
main.py

Contains the FastAPI application and the endpoint for receiving meeting transcripts.

models.py

Contains Pydantic models that define and validate the expected structure of the extracted meeting information.

llm_service.py

Contains an example implementation of the LLM integration. The transcript is sent to an LLM together with instructions to extract only information supported by the transcript and return structured data matching the defined Pydantic model.

The API key is intentionally not included in this repository. A valid API key would need to be configured locally to execute the LLM request.

Running the Prototype

Install the required dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn main:app --reload

The API documentation is then available at:

http://127.0.0.1:8000/docs

A transcript can be submitted to:

POST /process-transcript

Example request:

{
  "transcript": "Maria: We need SAP integration. I will send the documentation by Friday. Antonio: I will prepare the prototype."
}
Production Considerations

In a production implementation, I would additionally consider:

Human approval before important information is written to the business system
API authentication and secure secret management
Retry mechanisms and exponential backoff for unavailable services
A secondary LLM provider as a fallback if the primary LLM API is unavailable
Background processing with a task queue for longer-running AI requests
Database storage for processing status and results
Logging and monitoring
Docker-based deployment and, if required by scale, container orchestration

This repository is intended as a small technical demonstration of the proposed architecture rather than a production-ready implementation.