import os
import streamlit as st
import openai


def ask_gpt(prompt: str = ''):
    openai.api_type = st.secrets['OpenAI']['API_TYPE']
    openai.api_base = st.secrets['OpenAI']['API_BASE']
    openai.api_version = st.secrets['OpenAI']['API_VERSION'] or None
    openai.api_key = st.secrets['OpenAI']['API_KEY']

    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0.0,
                                        max_tokens=300,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0)

    return response["choices"][0]["text"]

def ask_azure_gpt(prompt: str = ''):
    openai.api_type = st.secrets['Azure']['API_TYPE']
    openai.api_base = st.secrets['Azure']['API_BASE']
    openai.api_version = st.secrets['Azure']['API_VERSION']
    openai.api_key = st.secrets['Azure']['API_KEY']

    response = openai.Completion.create(engine=st.secrets['Azure']['API_ENGINE'],
                                        prompt=prompt,
                                        temperature=0.0,
                                        max_tokens=300,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0)

    return response["choices"][0]["text"]