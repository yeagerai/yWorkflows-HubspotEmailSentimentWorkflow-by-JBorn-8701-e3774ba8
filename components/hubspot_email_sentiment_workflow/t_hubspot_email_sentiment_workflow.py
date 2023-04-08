
import pytest
from fastapi.testclient import TestClient
from typing import Tuple
from pydantic import BaseModel

from your_module_path import (
    hubspot_email_sentiment_workflow_app,
    HubspotEmailSentimentWorkflowIn,
    HubspotEmailSentimentWorkflowOut
)

client = TestClient(hubspot_email_sentiment_workflow_app)


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        (
            HubspotEmailSentimentWorkflowIn(
                EmailId="mock_email_id",
                HubspotApiKey="mock_api_key",
                NegativeTemplate="mock_negative_template",
                PositiveTemplate="mock_positive_template"
            ),
            HubspotEmailSentimentWorkflowOut(ResponseEmail="processed_response_email")
        ),
        # Add more test cases here
    ],
)
def test_transform(input_data: BaseModel, expected_output: BaseModel) -> None:
    response = client.post("/transform/", data=input_data.json())
    assert response.status_code == 200
    assert response.json() == expected_output.dict()


@pytest.mark.parametrize(
    "invalid_input",
    [
        # Test cases with invalid or missing input data, for example:
        {
            "HubspotApiKey": "mock_api_key",
            "NegativeTemplate": "mock_negative_template",
            "PositiveTemplate": "mock_positive_template",
            # Missing EmailId
        },
        {
            "EmailId": "mock_email_id",
            "NegativeTemplate": "mock_negative_template",
            "PositiveTemplate": "mock_positive_template",
            # Missing HubspotApiKey
        },
        # Add more test cases with invalid input data here
    ],
)
def test_transform_invalid_input(invalid_input: dict) -> None:
    response = client.post("/transform/", data=invalid_input)
    assert response.status_code == 422  # Validation error

# Add any additional tests for edge cases or error handling here
