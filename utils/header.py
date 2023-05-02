import streamlit as st


def write_header(heading: str, description: str):
    # Set Streamlit app theme
    st.set_page_config(page_title=heading,
                       page_icon="images/launchpad-icon.png", layout="centered")

    # Display logo image
    launchpad_icon = "images/launchpad-icon.png"
    st.image(launchpad_icon, width=100)

    # Set up app title
    st.title(heading)

    # Display app information
    st.warning('**This application is in Alpha version**. You should avoid using it for general fact-finding and information retrieval and must never trust the responses completely.')

    # Add information section
    with st.expander(f"{heading}'s Description".upper(), False):
        st.write(description)

    # st.divider()
