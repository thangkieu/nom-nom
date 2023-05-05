import os
import streamlit as st
from langchain import PromptTemplate
from utils.llm_models import summarise
from utils.feedbacks import render_feedbacks

template = """
    You are an AI assistant that helps users combining and summarizing their meeting notes.

    Combine and write a concise summary of the following meeting notes:
    {noms}

    Summarize in the following format:
    - Date of the meeting
    - Content of the meeting
    - Key action items
    - Parties that make a lot of effort
"""


def write_nomnom():
    if not 'nom_response' in st.session_state:
        st.session_state.nom_response = ""

    noms = ''
    with st.expander('Insert all of your NOMs here', True):
        noms = st.text_area('Separate by newline', height=200)

    is_generate = st.button(
        'Summarise NOMs', disabled=not noms, type="primary")

    # ---- Generate prompt ----
    prompt = PromptTemplate(input_variables=["noms"], template=template)
    prompt_str = prompt.format(noms=noms)

    # ---- Result ----
    st.subheader('Result')
    st_prompt_exp = st.expander('**ACTUAL PROMPT**', False)
    st_prompt_exp.info(template)

    st_resp_exp = st.expander('**RESPONSE**', True)

    if is_generate:
        with st.spinner('Summarising...'):
            azure_resp = summarise(prompt_str)
            st.session_state.nom_response = azure_resp

    if st.session_state.nom_response:
        st_resp_exp.success(st.session_state.nom_response)

        render_feedbacks(name="nomnom", label1="NOMNOM",
                         label2=st.session_state.nom_response)
