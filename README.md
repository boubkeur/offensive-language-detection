# Offensive Language Detection (NLP)

This project implements a machine learning pipeline to detect offensive language in social media text using classical NLP techniques.

## Features
- Text preprocessing (emoji normalization, URL removal, cleaning)
- TF-IDF vectorization (unigrams + bigrams)
- Models: SVM, Naive Bayes, Random Forest
- Evaluation using stratified train/validation split

## Project Structure
- TP05_Bouchama.ipynb: main notebook
- inference.py: inference script with latency measurement
- requirements.txt: dependencies

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook offensive-language-detection.ipynb
