# Customer Feedback Sentiment Analysis

## Overview

This project implements a serverless customer feedback sentiment analysis pipeline using AWS services.

Customer feedback is uploaded as a CSV file to Amazon S3. An AWS Lambda function processes the file and uses Amazon Comprehend to detect the sentiment of each feedback entry. The processed results are then stored as JSON in Amazon S3.

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
Processed JSON → Amazon S3

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
3. Lambda retrieves the CSV file.
4. Customer feedback is extracted from the CSV.
5. Amazon Comprehend analyzes the sentiment.
6. The detected sentiment and processing timestamp are added to each record.
7. The processed data is converted to JSON.
8. The JSON output is stored in Amazon S3.

## Project Structure

- `lambda_sentiment_analysis.py` — AWS Lambda function
- `manifest.json` — Project configuration
- `customer_feedback.csv` — Customer feedback dataset
- `project-report.pdf` — Project report
- `project-documentation.docx` — Project documentation
- `project-presentation.pptx` — Project presentation

## AWS Services

### Amazon S3

Stores the input customer feedback CSV files and processed JSON output.

### AWS Lambda

Provides the serverless processing layer and executes when a relevant file is uploaded to S3.

### Amazon Comprehend

Performs natural language processing and sentiment detection.

## Learning Outcomes

This project demonstrates experience with:

- Serverless cloud computing
- AWS service integration
- Event-driven architecture
- Natural language processing
- Python programming
- Data processing
- Cloud-based application development

## Future Improvements

- Add a web-based dashboard for sentiment visualization
- Support multiple languages
- Add sentiment confidence scores
- Implement automated monitoring and logging
- Add advanced customer feedback analytics
