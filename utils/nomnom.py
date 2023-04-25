import os
import streamlit as st
from langchain import PromptTemplate
from utils.llm_models import summarise

template = """
    You are an AI assistant that helps users combining and summarizing their meeting notes.

    Combine and summarise the following meeting notes into one:
    {noms}

    Summarize in the following format:
    - Date of the meeting
    - Content of the meeting
    - Key action items
    - Parties that make a lot of effort
"""


def write_nomnom():
    noms = ''
    with st.expander('Insert all of your NOMs here', True):
        noms = st.text_area('Separate by newline', height=200)

    is_generate = st.button(
        'Summarise NOMs', disabled=not noms, type="primary")

    prompt = PromptTemplate(input_variables=["noms"], template=template)
    prompt_str = prompt.format(noms=noms)

    if is_generate:
        with st.spinner('Summarising...'):
            azure_resp = summarise(prompt_str)
            st.subheader('Summarised NOM')
            st.success(azure_resp)