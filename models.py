from typing import Optional
from pydantic import BaseModel


class TranscriptRequest(BaseModel):
    transcript: str


class ActionItem(BaseModel):
    task: str
    responsible_person: Optional[str] = None
    deadline: Optional[str] = None


class MeetingAnalysis(BaseModel):
    client: Optional[str] = None
    summary: str
    requirements: list[str]
    decisions: list[str]
    next_steps: list[ActionItem]