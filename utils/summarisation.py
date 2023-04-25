import os
import streamlit as st
from langchain import PromptTemplate
from utils.llm_models import summarise

template = """
    You are an AI assistant that helps users summarise their text.
    
    Write a concise summary of the following text with a {tone} tone:
    {text}
"""

if 'summary' not in st.session_state:
    st.session_state['summary'] = ''


def write_summarisation():
    text = ''
    tone = 'Neutral'
    paragraph_no = 3

    with st.expander('Insert your text here', True):
        text = st.text_area('summarisation textarea',
                            height=200, label_visibility='collapsed')

    with st.expander('Summarising\'s Configuration', False):
        tone = st.radio('Tone', ('Formal', 'Neutral', 'Humour'), index=1)

    st.divider()

    is_generate = st.button(
        'Summarise Text', disabled=not text, type="primary")

    prompt = PromptTemplate(input_variables=["text", "tone"],
                            template=template)
    prompt_str = prompt.format(text=text, tone=tone)

    if is_generate:
        st.session_state['summary'] = ''

        with st.spinner('Summarising...'):
            azure_resp = summarise(prompt_str)
            st.session_state['summary'] = azure_resp

            st.subheader('Summarised')
            st.success(azure_resp)
    elif st.session_state['summary']:
        st.subheader('Summarised')
        st.success(st.session_state['summary'])

    view_prompt = st.button('View Prompt')
    if view_prompt:
        st.info(template)
