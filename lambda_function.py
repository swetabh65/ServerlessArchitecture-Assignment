import boto3
import json

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend', region_name='us-west-2')
    
    # Extract user review text from event
    review_text = event.get('review', '')
    print(f" Review received: {review_text}")
    
    if not review_text:
        return {"error": "No review text provided."}
    
    # Call Amazon Comprehend
    response = comprehend.detect_sentiment(Text=review_text, LanguageCode='en')
    
    sentiment = response['Sentiment']
    confidence_scores = response['SentimentScore']
    
    print(f" Sentiment: {sentiment}")
    print(f" Confidence Scores: {json.dumps(confidence_scores, indent=2)}")
    
    return {
        "review": review_text,
        "sentiment": sentiment,
        "confidence": confidence_scores
    }
