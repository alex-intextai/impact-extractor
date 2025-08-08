from transformers import pipeline
import torch

def initialize_classifier():
    '''
    Initialize the text classification pipeline with a pre-trained model.
    '''
    return pipeline(
        task="text-classification",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        torch_dtype=torch.float16,
        device=0
    )

def classify_text(text):
    '''
    Classify the input text using the pre-trained model.    
    '''
    classifier = initialize_classifier()
    return classifier(text)


def main():
    text = "The impact of climate change on global agriculture is significant."
    result = classify_text(text)
    print(result)

if __name__ == "__main__":
    main()