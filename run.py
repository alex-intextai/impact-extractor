from pdf_reader.reader import extract_text, doc, out
import sys, pathlib, pymupdf
from nlp.sentence import process_text
from nlp.model import read_text, classify_text

def main():
    extract_text(doc, out)
    text = read_text("./data/outputs/out.txt")
    process_text(text)

if __name__ == "__main__":
    main()
