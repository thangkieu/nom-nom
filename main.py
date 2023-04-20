import os
import openai
import streamlit as st

# Config
st.set_page_config(layout="wide", 
                    page_title="NOM NOM - Summarise NoMs and Highlight Key Actions Items/Parties"
                    )
st.header('NOM NOM - Summarise NoMs and Highlight Key Actions Items/Parties')

# Sessions
if 'nom_inputs' not in st.session_state:
    st.session_state['nom_inputs'] = []
if 'nom_values' not in st.session_state:
    st.session_state['nom_values'] = []

nom_inputs = st.session_state['nom_inputs']
nom_values = st.session_state['nom_values']


col1, col2 = st.columns(2)

with col1:
    api_key = st.text_input('Enter OpenAI API KEY to start:')
    if not api_key:
        st.stop()
    openai.api_key = api_key

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
        st.code('\n----------\n'.join(filterd_noms))
    else:
        st.error('Add your NOMs and click Summarise')
    clicked_on_generate = st.button('Summarise', 
                                    disabled=not filterd_noms,
                                    type="primary")

    # Prompt
    prompt = """
    Summary the meeting notes below into one note of minutes (NOM):

    {noms}

    Structure of NOM:
    - date time
    - content
    - key action items
    - parties that make a lot of effort
    """

    filled = prompt.format(noms='\n----------\n'.join(filterd_noms))

    if clicked_on_generate:
        with st.spinner('Summarising...'):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=filled,
                temperature=0,
                max_tokens=200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )


            st.divider()
            st.subheader('Summarised NOM')
            st.success(response["choices"][0]["text"])