import os
import streamlit as st
from openapi_config import ask_gpt

# Config
st.set_page_config(layout="wide", 
                    page_title="NOM NOM - Summarise NoMs and Highlight Key Actions Items/Parties")
                    
st.header('NOM NOM - Summarise NoMs and Highlight Key Actions Items/Parties')

# Sessions
if 'nom_inputs' not in st.session_state:
    st.session_state['nom_inputs'] = ['NOM']
if 'nom_values' not in st.session_state:
    st.session_state['nom_values'] = ['']

nom_inputs = st.session_state['nom_inputs']
nom_values = st.session_state['nom_values']


col1, col2 = st.columns(2)

with col1:
    clicked = st.button('Add new NOM')
    if clicked:
        nom_inputs.append('NOM')
        nom_values.append('')

    for index, nom in enumerate(nom_inputs):
        val = st.text_area(f'{nom} - {index + 1}')
        nom_values[index] = val

with col2:
    filterd_noms = [nom for nom in nom_values if nom]
    if filterd_noms:
        st.subheader('Preview')
        st.code('\n----------\n'.join(filterd_noms))
    else:
        st.error('Add your NOMs and click Summarise')
    clicked_on_generate = st.button('Summarise', 
                                    disabled=not filterd_noms,
                                    type="primary")

    # Prompt
    prompt = """
    You are an assistant that combining and summarizing meeting notes from multiple person into one.

    Combine and generate a sumany of below meeting notes into one, do mention these info:
    date time, content, key actions items and highlight parties that make a lot of effort.

    Meeting notes:
    {noms}

    Summary:
    """

    filled = prompt.format(noms='\n----------\n'.join(filterd_noms))

    if clicked_on_generate:
        with st.spinner('Summarising...'):
            response: str = ask_gpt(filled)

            st.divider()
            st.subheader('Summarised NOM')
            st.text(response.replace('<|im_end|>', ''))