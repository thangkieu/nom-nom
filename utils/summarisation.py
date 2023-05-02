import os
import streamlit as st
from langchain import PromptTemplate
from utils.llm_models import summarise

template = """
    You are an AI assistant that helps users summarise their text.

    Write a concise summary of the following text with a {tone} tone, limit in {length} words:
    {text}
"""


def write_summarisation():
    text = ''
    tone = 'Neutral'
    paragraph_no = 3
    length = 20

    st_input_exp = st.expander('Insert your text here', True)
    text = st_input_exp.text_area('summarisation textarea',
                                  height=200, label_visibility='collapsed')

    # ----- Configuration ----
    st_config_exp = st.expander('Summarisation\'s Configuration', False)
    tone = st_config_exp.radio(
        'Style of Summarisation', ('Professional', 'Neutral', 'Humourous'), index=1, horizontal=True)
    length = st_config_exp.number_input(
        'Length (no. of words)', step=50, min_value=50, format='%d')

    is_summary_clicked = st.button(
        'Summarise Text', disabled=not text, type="primary")

    # ---- Generate prompt ----
    prompt = PromptTemplate(input_variables=["text", "tone", "length"],
                            template=template)
    prompt_str = prompt.format(text=text, tone=tone, length=length)

    # ---- Result ----
    st.subheader('Result')
    st_prompt_exp = st.expander('Prompt Template', False)
    st_prompt_exp.info(template)

    st_resp_exp = st.expander('Response', True)

    if is_summary_clicked:
        with st.spinner('Summarising...'):
            azure_resp = summarise(prompt_str)
            st_resp_exp.success(azure_resp)
