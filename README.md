# Meeting AI Automation Prototype

This project is a small prototype demonstrating how AI could automate the processing of client meeting transcripts in a consulting company.

The goal is to transform an unstructured meeting transcript into structured business information and prepare it for transfer into the company's internal business system.

## Workflow

The proposed process is:

**Meeting transcript → FastAPI → LLM analysis → Structured data → Validation → Internal business API → Human approval**

1. A meeting transcript is sent to the FastAPI backend.
2. The transcript is passed to an LLM for analysis.
3. The LLM extracts the relevant information into a predefined structured format.
4. Pydantic validates the structure of the returned data.
5. The validated report is prepared for transfer to the company's internal business system through its API.
6. The report is stored with the status `needs_approval`.
7. An employee can then review, correct and approve the report inside the company's existing business system.

This keeps a human in the loop without requiring a separate approval interface.

## Extracted Information

The LLM is instructed to extract:

* Client
* Meeting summary
* Client requirements
* Decisions
* Next steps / action items
* Responsible persons
* Deadlines

If information such as a responsible person or deadline cannot be determined from the transcript, the model should return `null` instead of inventing a value.

## Project Structure

```text
meeting-ai-automation/
├── main.py
├── models.py
├── llm_service.py
├── business_api.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Contains the FastAPI application and the endpoint used to receive meeting transcripts and start the processing workflow.

### `models.py`

Contains the Pydantic models defining the expected structure of the AI-generated meeting report.

These models are also used to validate the structure and data types returned by the LLM.

### `llm_service.py`

Contains an example implementation of the LLM integration.

The transcript is sent to the model together with instructions to extract only information supported by the transcript and return the result according to the predefined structure.

The API key is intentionally not included in the repository. A valid API key would need to be configured locally to execute the LLM request.

### `business_api.py`

Demonstrates how the validated report could be transferred to the company's internal business system using an HTTP POST request.

Before sending, the report receives the status:

```text
needs_approval
```

This indicates that the AI-generated information must be reviewed by an employee before it is treated as final.

The URL used in the prototype is only an example and does not represent a real business system.

## Example Structured Output

```json
{
  "client": "ABC d.o.o.",
  "summary": "The client wants to automate invoice processing and integrate the solution with SAP.",
  "requirements": [
    "Automated invoice processing",
    "SAP integration"
  ],
  "decisions": [
    "Prepare an initial prototype"
  ],
  "next_steps": [
    {
      "task": "Send sample invoices",
      "responsible_person": "Maria",
      "deadline": "2026-09-15"
    },
    {
      "task": "Prepare the prototype",
      "responsible_person": "Antonio",
      "deadline": null
    }
  ]
}
```

## Running the Prototype

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

FastAPI's interactive API documentation is then available at:

```text
http://127.0.0.1:8000/docs
```

A transcript can be submitted using:

```text
POST /process-transcript
```

Example request:

```json
{
  "transcript": "Maria: We need SAP integration. I will send the documentation by Friday. Antonio: I will prepare the prototype."
}
```

## Production Considerations

For a production implementation, I would additionally consider authentication and secure secret management, retry mechanisms with exponential backoff, database storage, logging and monitoring, background task processing and a fallback LLM provider.

For larger workloads, technologies such as Redis/Celery, Docker and container orchestration could also be introduced depending on the required scale.

This repository is intentionally kept small and focuses on demonstrating the main architecture and technical approach rather than providing a production-ready system.
