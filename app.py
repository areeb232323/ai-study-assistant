import streamlit as st
from summarizer import generate_summary, extract_keywords

st.title("AI Study Assistant 🤖📚")

text = st.text_area("Paste your text here:")

if st.button("Summarize"):
    summary = generate_summary(text)
    st.subheader("Summary")
    st.write(summary)

if st.button("Extract Keywords"):
    keywords = extract_keywords(text)
    st.subheader("Keywords")
    st.write(keywords)
