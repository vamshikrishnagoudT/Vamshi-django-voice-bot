# from transformers import pipeline

# # Initialize zero-shot classification pipeline
# nlp_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# def classify_intent(text):
#     # Define possible intents
#     candidate_labels = ["greeting", "account_info", "faq"]
    
#     # Perform zero-shot classification
#     result = nlp_pipeline(text, candidate_labels=candidate_labels)
    
#     # Return the label with the highest score
#     return result['labels'][0]
from transformers import pipeline

# Initialize zero-shot classification pipeline
nlp_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Rule-based responses
responses = {
    "greeting": "Hello! How can I assist you today?",
    "account_info": "You can check your account details by logging into your portal.",
    "faq": "Please visit our FAQ page for common questions."
}

def classify_intent(text):
    # Define possible intents
    candidate_labels = ["greeting", "account_info", "faq"]
    
    # Perform zero-shot classification
    result = nlp_pipeline(text, candidate_labels=candidate_labels)
    
    # Get the detected intent
    intent = result['labels'][0]
    
    # Return the response based on the detected intent
    return responses.get(intent, "Sorry, I didn't understand that.")
