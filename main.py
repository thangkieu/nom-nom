import streamlit as st

from utils.header import write_header
from utils.footer import write_footer
from utils.nomnom import write_nomnom
from utils.summarisation import write_summarisation

write_header(heading="Summariser",
             description="The tool would take in a long, complicated documents or statements and use GPT to generate a summary that captures the main points in simple language")

summarisation, nomnom = st.tabs(["Summarisation", "NOM summarisation"])

with summarisation:
    write_summarisation()

with nomnom:
    write_nomnom()

write_footer()
