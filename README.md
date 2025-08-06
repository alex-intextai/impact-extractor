# Impact Extractor: Prototype NLP Pipeline for Externality Detection

This project is a prototype system that ingests text from ESG reports and academic papers and extracts sentences or phrases that signal potential externalities such as environmental degradation, health impacts, or social consequences.

---

## 🗂 Essential Workflow Checklist

### 1. Text Extraction

- Extract text from PDF documents using **PyMuPDF**
- Location: `pdf_reader/reader.py`

### 2. Preprocessing

- Clean and segment extracted text into sentences
- Apply **spaCy** for:
  - Lemmatization
  - Named Entity Recognition (NER)
  - Part-of-Speech tagging
- Location: `nlp/spacy_pipeline.py`

### 3. Classification

- Load a **pre-trained or fine-tuned Hugging Face transformer model**
- Classify each sentence as either externality-related or not
- Location: `models/classifier.py`

### 4. Extraction

- Identify and extract key phrases within classified sentences that signal externalities
- Examples: mentions of pollution, health risks, labor violations
- Location: `nlp/extractor.py`

### 5. Output

- Display the results in a **Streamlit interface**
- Location: `app/main.py`
- Save the extracted results to disk as JSON or CSV
- Output path: `data/outputs/`

---

## 📦 Tech Stack

- PyMuPDF (PDF parsing)
- spaCy (NLP preprocessing)
- Hugging Face Transformers (sentence classification)
- PyTorch (model backend)
- Streamlit (UI)

---

## Directories Structure

<pre><code>## Directory Structure 
├── app/ # Streamlit interface 
│ └── main.py 

├── config/ # Configuration and constants 
│ └── settings.py 

├── data/ # Input/output data 
│ ├── raw/ 
│ └── outputs/ 

├── models/ # Classifier model 
│ └── classifier.py 

├── nlp/ # NLP utilities 
│ ├── spacy_pipeline.py # Preprocessing: lemmatization, NER, etc. 
│ └── extractor.py # Externality phrase extraction 

├── pdf_reader/ # PDF text extraction 
│ └── reader.py 

├── utils/ # Helper functions 
│ └── io_utils.py 

├── requirements.txt 
├── README.md 
└── run.py # CLI script for batch processing </code></pre>

## 🚀 Getting Started

Coming soon: setup instructions, environment details, and model loading guidelines.

## Set-up Instructions
