import os

import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

from marvin import ai_fn

load_dotenv()

# marvin.settings.openai_api_key = os.getenv("OPENAI_API_KEY")


@ai_fn
def summarize_video(text: str) -> str:
    """
    Summarize the transcript of a youtube video provided
    """


st.title("Summarize a YouTube Video")
st.divider()

# Getting input from the user and displaying activity
with st.form("Input_Form", clear_on_submit=True):
    video_url = st.text_input(
        "Enter the URL for the YouTube Video (Note: grab the URL from the browser URL bar, not the YouTube share URL):"
    )
    submitted = st.form_submit_button("Submit")

    if submitted:
        video_id = video_url.split("watch?v=")[-1]

        st.info("Fetching transcript...")

        # Transcribing the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        transcript_text = " ".join([entry["text"] for entry in transcript])

        st.info("Summarizing...")
        summary = summarize_video(transcript_text)

        # Displaying the summary
        st.write("Summary of the video:" + summary)

        video_url = st.empty()
