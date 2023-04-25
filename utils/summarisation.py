import os
import streamlit as st
from langchain import PromptTemplate
from utils.llm_models import summarise

template = """
    You are an AI assistant that helps users summarise their text.
    
    Write a concise summary of the following with a {tone} tone in {paragraph_no} paragraphs:
    {text}
"""


def write_summarisation():
    text = ''
    tone = 'Neutral'
    paragraph_no = 3

    with st.expander('Insert your text here', True):
        text = st.text_area('summarisation textarea',
                            height=200, label_visibility='collapsed')

    with st.expander('Summarising\'s Configuration', False):
        tone = st.radio('Tone', ('Formal', 'Neutral', 'Humor'), index=1)
        paragraph_no = st.slider('No of paragraph', 1, 5, value=paragraph_no)

    is_generate = st.button(
        'Summarise Text', disabled=not text, type="primary")

    prompt = PromptTemplate(input_variables=["text", "tone", "paragraph_no"],
                            template=template)
    prompt_str = prompt.format(text=text, tone=tone, paragraph_no=paragraph_no)

    if is_generate:
        with st.spinner('Summarising...'):
            azure_resp = summarise(prompt_str)
            st.subheader('Summarised')
            st.success(azure_resp)
