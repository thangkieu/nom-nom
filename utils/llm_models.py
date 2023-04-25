import streamlit as st

from langchain.chat_models import AzureChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain


def summarise(prompt: str = ''):
    env_var = st.secrets.get('Azure')

    llm = AzureChatOpenAI(deployment_name=env_var.get('API_ENGINE'),
                          openai_api_key=env_var.get('API_KEY'),
                          openai_api_type=env_var.get('API_TYPE'),
                          openai_api_version=env_var.get('API_VERSION'),
                          openai_api_base=env_var.get('API_BASE'))

    text_splitter = CharacterTextSplitter()

    texts = text_splitter.split_text(prompt)
    docs = [Document(page_content=t) for t in texts[:3]]
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    resp = chain.run(docs)

    return resp
