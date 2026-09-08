# Customer Feedback Sentiment Analysis

## Overview

This project implements a serverless customer feedback sentiment analysis pipeline using AWS services.

Customer feedback is uploaded as a CSV file to Amazon S3. An AWS Lambda function is triggered by the upload, reads the feedback data, and uses Amazon Comprehend to detect the sentiment of each feedback entry. The processed results are then stored as a JSON file in Amazon S3.

## Architecture

Customer Feedback CSV
↓
Amazon S3
↓
AWS Lambda
↓
Amazon Comprehend
↓
Sentiment Detection
↓
Processed JSON
↓
Amazon S3

## Technologies Used

- Python
- AWS Lambda
- Amazon S3
- Amazon Comprehend
- Boto3
- CSV
- JSON

## How It Works

1. A customer feedback CSV file is uploaded to the `feedback/` folder in Amazon S3.
2. The S3 event triggers the AWS Lambda function.
3. Lambda retrieves the uploaded CSV file from S3.
4. Customer feedback is extracted from the CSV.
5. Amazon Comprehend analyzes the sentiment of each feedback entry.
6. The detected sentiment and processing timestamp are added to each record.
7. The processed data is converted to JSON.
8. The resulting JSON file is stored in the `processed/` folder in Amazon S3.

## Project Structure

- `lambda_feedback_sentiment.py` — AWS Lambda function
- `manifest.json` — Project configuration
- `customer_feedback_full (3).csv` — Customer feedback dataset
- `A2_2210030485.pdf` — Project documentation
- `cloud(485) (3).docx` — Project documentation
- `sdc-4_2210030485(a2).pptx` — Project presentation

## Lambda Function

The Lambda function uses Boto3 to interact with Amazon S3 and Amazon Comprehend.

The function:

- Processes S3 upload events
- Reads CSV customer feedback
- Performs sentiment detection using Amazon Comprehend
- Adds detected sentiment to each record
- Adds a processing timestamp
- Stores the processed results as JSON in Amazon S3

## Example Output

```json
{
  "Feedback": "Example customer feedback",
  "DetectedSentiment": "POSITIVE",
  "ProcessedTimestamp": "2026-01-01T12:00:00"
}
AWS Services
Amazon S3

Used for storing the input customer feedback CSV files and processed JSON output.

AWS Lambda

Provides the serverless processing layer and automatically executes when a relevant file is uploaded to S3.

Amazon Comprehend

Provides natural language processing and sentiment detection for customer feedback.

Learning Outcomes

This project demonstrates experience with:

Serverless cloud computing
AWS service integration
Event-driven architecture
Natural language processing
Python programming
Data processing
Cloud-based application development
Future Improvements
Add a web-based dashboard for sentiment visualization
Support multiple languages
Add sentiment confidence scores
Implement automated monitoring and logging
Add advanced customer feedback analytics
