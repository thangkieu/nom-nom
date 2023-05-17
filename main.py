import streamlit as st

from utils.header import write_header
from utils.footer import write_footer
from utils.nomnom import write_nomnom
from utils.summarisation import write_summarisation

write_header(heading="Summariser",
             description="A summarizer app is particularly useful for tasks that involve longer texts. It can help users quickly understand the main ideas of a document without having to read the entire thing. Additionally, for tasks that involve multiple scribes, this summarizer apps offer the option to condense multiple notes, which can save time and improve collaboration.")

summarisation, nomnom = st.tabs(
    ["Summarisation", "Multiple Notes Summarisation"])

with summarisation:
    write_summarisation()

with nomnom:
    write_nomnom()

write_footer()
