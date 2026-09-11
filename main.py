from fastapi import FastAPI

from models import TranscriptRequest
from llm_service import analyze_transcript


app = FastAPI(
    title="Meeting AI Automation",
    description="Prototype for automated processing of meeting transcripts"
)


@app.get("/")
def root():
    return {
        "message": "Meeting AI Automation API is running"
    }


@app.post("/process-transcript")
def process_transcript(request: TranscriptRequest):

    analysis = analyze_transcript(request.transcript)

    return analysis

