python
import re
import time
import emoji

def clean_text(text):
    text = str(text).lower()
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"@\w+|#\w+", " ", text)
    text = re.sub(r"[_:]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def predict(text, model, vectorizer):
    start = time.time()
    text_clean = clean_text(text)
    vec = vectorizer.transform([text_clean])
    pred = model.predict(vec)
    latency = time.time() - start
    return pred[0], latency
