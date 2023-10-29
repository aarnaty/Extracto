import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Welcome Page",
        page_icon="👋",
    )

    st.write("# Welcome to Extracto! 👋")

    st.markdown(
        """
Here at Extracto, we believe in the power of words, and we've harnessed the latest in Artificial Intelligence to make your experience with text processing and communication more vibrant and insightful! 

Step into this virtual realm, where innovation meets elegance, and discover a diverse array of modules designed to elevate your text-related tasks to the next level:

#### -Text Summarizer: 
Simplify the complexities of lengthy texts. This feature condenses information while retaining its essense, making research and information consumption a breeze.

#### -Sentiment Analyzer: 
Understand the emotional context of your text with this tool. Gain insights into the feelings, attitudes and opinions expressed in any piece of writing.

#### -Text Generator: 
From creative writing to professional content, let your thoughts flow effortlessly as you watch words form on your screen, driven by the power of prompt engineering.

#### -Document Chatbot: 
Have a conversation with a bot that reads the documents provided by you and answers your questions based on it. This context-based chatbot answers your questions intelligently while protecting your sensitive data.

Unleash your creativity, simplify your work and connect on a deeper level with the text you encounter. Transform the way you engage with language!
    """
    )


if __name__ == "__main__":
    run()