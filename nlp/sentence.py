import spacy
from spacy.pipeline import SentenceRecognizer

nlp = spacy.load("en_core_web_sm")

nlp.add_pipe("sentencizer")

def process_text(text):
    doc = nlp(text)

    for i, sent in enumerate(doc.sents, 1):
        print(sent.text)

def main():
    text = "This is a sentence. This is another one."
    process_text(text)

if __name__ == "__main__":
    main()