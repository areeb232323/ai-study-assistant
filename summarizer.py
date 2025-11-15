from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
keyword_extractor = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_summary(text):
    return summarizer(text, max_length=200, min_length=50, do_sample=False)[0]["summary_text"]

def extract_keywords(text):
    prompt = f"Extract the 5 most important keywords from this text:\n{text}"
    keywords = keyword_extractor(prompt, max_length=50)[0]["generated_text"]
    return keywords
