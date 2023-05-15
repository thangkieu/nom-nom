import os
import streamlit as st
from langchain import PromptTemplate
from utils.llm_models import summarise
from utils.feedbacks import render_feedbacks

template = """
    You are an AI assistant that helps users summarise their text.

    Write a concise summary of the following text with a {tone} tone, limit in {length} words:
    {text}
"""


def write_summarisation():
    if not 'sum_response' in st.session_state:
        st.session_state.sum_response = ""

    text = ''
    tone = 'Neutral'
    paragraph_no = 3
    length = 20

    st_input_exp = st.expander('📝 **INSERT YOUR TEXT HERE**', True)
    text = st_input_exp.text_area('summarisation textarea',
                                  height=200, label_visibility='collapsed')

    # ----- Configuration ----
    st_config_exp = st.expander('⚙️ **CONFIGURATIONS**', False)
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
    st_prompt_exp = st.expander('**ACTUAL PROMPT**', False)
    st_prompt_exp.info(template)
    st_resp_exp = st.expander('**RESPONSE**', True)

    if is_summary_clicked:
        with st.spinner('Summarising...'):
            azure_resp = summarise(prompt_str)
            st.session_state.sum_response = azure_resp

    if st.session_state.sum_response:
        st_resp_exp.success(st.session_state.sum_response)

        render_feedbacks(name="summarisation", label1="Summarisation",
                         label2=st.session_state.sum_response)
