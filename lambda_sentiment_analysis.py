import boto3
import csv
import io
import json
from datetime import datetime

# Initialize AWS clients
s3 = boto3.client('s3')
comprehend = boto3.client('comprehend', region_name='eu-west-1')

def lambda_handler(event, context):
    try:
        # Get bucket and file key from the S3 event trigger
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Only proceed if the file is in the 'feedback/' folder
        if not key.startswith('feedback/'):
            return {
                'statusCode': 400,
                'body': f"Skipped file {key} because it's not in the 'feedback/' folder."
            }

        # Fetch and decode CSV content
        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response['Body'].read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file_content))
        
        processed_data = []

        # Loop through each row and detect sentiment
        for row in reader:
            feedback_text = row.get('Feedback')  # Assumes CSV column is named 'Feedback'
            if feedback_text:
                sentiment_result = comprehend.detect_sentiment(Text=feedback_text, LanguageCode='en')
                sentiment = sentiment_result['Sentiment']

                # Add sentiment and timestamp to the row
                row['DetectedSentiment'] = sentiment
                row['ProcessedTimestamp'] = datetime.utcnow().isoformat()
                processed_data.append(row)

        # Save processed data as JSON in a new 'processed/' folder
        result_key = f"processed/feedback_result_{datetime.utcnow().isoformat()}.json"
        s3.put_object(
            Bucket=bucket,
            Key=result_key,
            Body=json.dumps(processed_data, indent=2),
            ContentType='application/json'
        )

        return {
            'statusCode': 200,
            'body': f"✅ Processed {len(processed_data)} entries from '{key}' and saved to '{result_key}'"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
