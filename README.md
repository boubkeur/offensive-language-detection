# Offensive Language Detection (NLP)

This project implements an NLP pipeline to detect offensive language in text data.

## Features
- Text preprocessing (emoji normalization, URL removal, cleaning)
- TF-IDF vectorization (unigrams + bigrams)
- Models: SVM, Naive Bayes, Random Forest
- Evaluation using stratified splits

## Project Structure
- TP05_Bouchama.ipynb: main notebook
- inference.py: simple inference script with latency measurement

## Usage
Run the notebook:
```bash
jupyter notebook TP05_Bouchama.ipynb
