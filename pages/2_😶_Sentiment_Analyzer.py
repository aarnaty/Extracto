import streamlit as st
#from api_key import apikey
from langchain import OpenAI

def analyze_sentiment(text):
	openai_api_key="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"
	llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
	response=llm(f'This is a sentiment analysis request. Can you tell me the sentiment of the following text? Be elaborate.\n"{text}"\nSentiment: {{sentiment}}')
	return response

st.set_page_config(page_title='Sentiment Analyzer')
st.title('Sentiment Analyzer')

txt_input = st.text_area('Enter text to get the sentiment analysis', '', height=200)

result = []
submitted = st.button('Submit')
if submitted:
	with st.spinner('Analyzing...'):
		response = analyze_sentiment(txt_input)
		result.append(response)

if len(result):
    st.info(response)