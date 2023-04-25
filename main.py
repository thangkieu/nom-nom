import streamlit as st

from utils.header import write_header
from utils.footer import write_footer
from utils.nomnom import write_nomnom
from utils.summarisation import write_summarisation

write_header()

summarisation, nomnom = st.tabs(["Summarisation", "NOM summarisation"])

with summarisation:
    write_summarisation()

with nomnom:
    write_nomnom()

write_footer()
