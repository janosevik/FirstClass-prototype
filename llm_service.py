import os

from dotenv import load_dotenv
from openai import OpenAI

from models import MeetingAnalysis

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not configured. "
        "Add your API key to a local .env file to run the LLM integration."
    )

client = OpenAI(api_key=api_key)


def analyze_transcript(transcript: str) -> MeetingAnalysis:

    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=[
            {
                "role": "system",
                "content": (
                    "You analyze meeting transcripts. "
                    "Extract only information supported by the transcript. "
                    "Do not invent missing information. "
                    "If information is unknown, return null."
                )
            },
            {
                "role": "user",
                "content": transcript
            }
        ],
        text_format=MeetingAnalysis
    )

    return response.output_parsed