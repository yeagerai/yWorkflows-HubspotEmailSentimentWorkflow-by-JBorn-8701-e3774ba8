
# HubspotEmailSentimentWorkflow

This workflow takes an email ID, reads and processes the email, analyzing its sentiment. Based on the analyzed sentiment, it selects a pre-determined negative or positive response email template, and creates a complete response email in 'draft' state.

## Initial generation prompt
description: "IOs - inputs:\n  EmailId: The email ID of the email to read and process.\n\
  \  HubspotApiKey: The API key for the Hubspot account.\n  NegativeTemplate: The\
  \ path to the pre-determined negative response email template.\n  PositiveTemplate:\
  \ The path to the pre-determined positive response email template.\noutputs:\n \
  \ ResponseEmail: The complete response email in 'draft' state, based on the analyzed\n\
  \    sentiment and selected template.\n"
name: HubspotEmailSentimentWorkflow


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        