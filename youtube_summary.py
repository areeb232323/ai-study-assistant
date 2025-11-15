from youtube_transcript_api import YouTubeTranscriptApi
from summarizer import generate_summary, extract_keywords

def get_youtube_id(url: str):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        return None

def fetch_video_transcript(video_url):
    video_id = get_youtube_id(video_url)
    if not video_id:
        return "Invalid YouTube URL."

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t["text"] for t in transcript])
    return text

def summarize_youtube_video(url):
    transcript = fetch_video_transcript(url)
    summary = generate_summary(transcript)
    keywords = extract_keywords(transcript)
    return summary, keywords
