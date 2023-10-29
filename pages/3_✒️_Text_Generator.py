import streamlit as st
from langchain import OpenAI

def translate(text):
	openai_api_key="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"
	llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
	response=llm(f'This is a text generation request. Can you generate a few lines for the following prompt: \n"{text}"\nGenerated Text: {{generated}}')
	return response

st.set_page_config(page_title='Text Generator')
st.title('Text Generator')

txt_input = st.text_area('Enter a prompt to generate text', '', height=100)

result = []
submitted = st.button('Submit')
if submitted:
	with st.spinner('Generating text...'):
		response = translate(txt_input)
		result.append(response)

if len(result):
    st.info(response)