# chat/services.py
from transformers import pipeline

def get_language_model(model_name):
    # Create a text generation pipeline for the specified model
    return pipeline("text-generation", model=model_name)
