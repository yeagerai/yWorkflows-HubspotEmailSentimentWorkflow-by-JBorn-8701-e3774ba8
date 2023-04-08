
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow

class HubspotEmailSentimentWorkflowIn(BaseModel):
    EmailId: str
    HubspotApiKey: str
    NegativeTemplate: str
    PositiveTemplate: str

class HubspotEmailSentimentWorkflowOut(BaseModel):
    ResponseEmail: str

class HubspotEmailSentimentWorkflow(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: HubspotEmailSentimentWorkflowIn, callbacks: typing.Any
    ) -> HubspotEmailSentimentWorkflowOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        # Here, add code to process the results_dict and obtain the expected ResponseEmail value
        ResponseEmail = "processed_response_email"
        out = HubspotEmailSentimentWorkflowOut(ResponseEmail=ResponseEmail)
        return out

load_dotenv()
hubspot_email_sentiment_workflow_app = FastAPI()

@hubspot_email_sentiment_workflow_app.post("/transform/")
async def transform(
    args: HubspotEmailSentimentWorkflowIn,
) -> HubspotEmailSentimentWorkflowOut:
    hubspot_email_sentiment_workflow = HubspotEmailSentimentWorkflow()
    return await hubspot_email_sentiment_workflow.transform(args, callbacks=None)
