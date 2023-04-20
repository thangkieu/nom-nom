import os
import streamlit as st
import openai

openai.api_type = st.secrets['API_TYPE']
openai.api_base = st.secrets['API_BASE']
openai.api_version = st.secrets['API_VERSION']
openai.api_key = st.secrets['API_KEY']

def ask_gpt(prompt: str = ''):
    response = openai.Completion.create(engine=st.secrets['API_ENGINE'],
                                        prompt=prompt,
                                        temperature=0.5,
                                        max_tokens=200,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0)

    return response["choices"][0]["text"]