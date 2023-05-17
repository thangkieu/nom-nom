import os
import streamlit as st
from langchain.prompts import PromptTemplate
from utils.llm_models import summarise
from utils.feedbacks import render_feedbacks
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import AzureChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

template = """
You are an AI assistant that helps users summarizing their meeting notes.
Write a concise summary of the following meeting notes of topics that separate by series of equal sign.

{text}

Summarize the meeting notes by topics, each topic should be summarized into one paragraph, ignore any empty topic. Do remove the topic name.
"""
# Summarize in the following format:
# - Date of the meeting
# - Content of the meeting
# - Key action items
# - Parties that make a lot of effort


def init_state():
    if 'row_no' not in st.session_state:
        st.session_state['row_no'] = 1

    """
    [ [1,2,3] ]
    [ [1,2,3] ]
    """
    if 'nom_values' not in st.session_state:
        st.session_state['nom_values'] = [[]]

    if not 'nom_response' in st.session_state:
        st.session_state.nom_response = ""


def increase_row():
    st.session_state.row_no = st.session_state.row_no + 1


def update_text(*args, **kwargs):
    print(f'textarea value: {args}, {kwargs}')


def form_render():
    init_state()

    party_no = st.number_input('No. of Notes', min_value=1, max_value=3)

    values = st.session_state.nom_values
    total_row = st.session_state.row_no
    cols = st.columns(party_no)

    for idx, col in enumerate(cols):
        col.text_input(key=f'party {idx}', label=f'Note from',
                       placeholder='Name')

    st.divider()

    if total_row > len(values):
        for idx in range(total_row - len(values)):
            values.append([[]])

    for rowIdx in range(st.session_state.row_no):
        st.markdown(f'**Topic {rowIdx + 1}**')

        cols = st.columns(party_no)
        # add new row
        for colIdx, col in enumerate(cols):
            val = col.text_area(key=f'nom-{colIdx}-{rowIdx}',
                                label_visibility='collapsed',
                                label=f'Topic {rowIdx + 1}',
                                placeholder=f'Topic {rowIdx + 1}\'s notes')

            if not val:
                pass

            if len(values[rowIdx]) <= colIdx:
                values[rowIdx].append(val)
            else:
                values[rowIdx][colIdx] = val

    st.button('Add New Topic', on_click=increase_row)


def write_nomnom():
    init_state()
    noms = ''

    with st.expander('📝 **INSERT ALL OF YOUR NOTES HERE**', True):
        form_render()

    is_generate = st.button(
        'Summarise Notes', type="primary")

    # ---- Generate prompt ----
    values = st.session_state.nom_values

    topics = []
    for topic_idx in range(len(values)):
        topic_items = []
        note = values[topic_idx]

        for col in range(len(note)):
            topic_items.append(note[col])

        topic = '\n\n'.join(topic_items)
        topics.append(f'Topic {topic_idx + 1}:\n{topic}')

    noms = '\n\n===========\n\n'.join(topics)

    # ---- Result ----
    st.subheader('Result')
    st_prompt_exp = st.expander('**ACTUAL PROMPT**', False)
    st_prompt_exp.code(template, language='toml')

    st_resp_exp = st.expander('**RESPONSE**', True)

    if is_generate:
        with st.spinner('Summarising...'):
            text = noms
            PROMPT = PromptTemplate(
                input_variables=["text"], template=template)
            azure_resp = summarise(input=text, prompt=PROMPT)

            st.session_state.nom_response = azure_resp

    if st.session_state.nom_response:
        st_resp_exp.success(st.session_state.nom_response)

        render_feedbacks(name="nomnom", label1="NOMNOM",
                         label2=st.session_state.nom_response)
