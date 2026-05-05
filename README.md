# Salesforce AI Customer 360 Architecture

This project demonstrates an enterprise-grade architecture where AWS and Snowflake act as the data foundation, Salesforce Data Cloud provides identity resolution and segmentation, SFMC activates personalized engagement, and Agentforce enables intelligent customer interactions.

## Architecture Flow

1. AWS ingests raw customer, web, and transaction data.
2. Snowflake stores curated customer and engagement datasets.
3. Salesforce Data Cloud ingests harmonized data from Snowflake.
4. Data Cloud performs identity resolution and segmentation.
5. SFMC activates segments through journeys, email, and web personalization.
6. Agentforce uses unified customer context to automate intelligent recommendations and service actions.

## Technologies

- AWS API Gateway
- AWS Lambda
- AWS EventBridge
- Snowflake
- Salesforce Data Cloud
- Salesforce Marketing Cloud
- Agentforce
- REST APIs
- AMPscript
- SQL

## Use Case

A customer clicks a campaign email, visits the website, and submits interest in a product or service.

The system captures the web event, stores and harmonizes it in Snowflake, updates the customer profile in Data Cloud, activates the customer in SFMC, and allows Agentforce to recommend the next best action.

## What This Project Demonstrates

- Enterprise Customer 360 architecture
- Data ingestion and harmonization
- Identity resolution concepts
- SFMC journey activation
- Agentforce use cases
- AWS event-driven integration
- Snowflake data modeling
- Consent and compliance considerations
