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

from youtube_summary import summarize_youtube_video

st.header("YouTube Video Summarizer")

yt_url = st.text_input("Enter YouTube URL:")

if st.button("Summarize YouTube Video"):
    summary, keywords = summarize_youtube_video(yt_url)

    st.subheader("Video Summary")
    st.write(summary)

    st.subheader("Key Concepts")
    st.write(keywords)
