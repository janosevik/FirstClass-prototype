import requests

from models import MeetingAnalysis


def save_report_for_approval(analysis: MeetingAnalysis):

    payload = analysis.model_dump()
    payload["status"] = "needs_approval"

    # Example endpoint of the company's internal business system
    url = "https://internal-company-system.example.com/api/meeting-reports"

    # Prototype only:
    # This demonstrates how the validated report would be sent.
    response = requests.post(
        url,
        json=payload,
        timeout=10
    )

    return response