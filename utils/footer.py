
import streamlit as st


def write_footer():
    st.divider()

    # Display feedback message
    st.info(
        "💬 Help us improve the application by sharing your [feedback with us](http://go.gov.sg/launchpad-gpt-feedback).")

    # Hide streamlit footer
    hide_streamlit_style = """
                <style>
                footer {display: none;}
                .stAlert {white-space:pre-wrap;}
                .row-widget.stButton {text-align:right;}
                .st-bk,[kind="primary"],[role="alert"],[data-baseweb="textarea"] {border-radius: 8px;}
                </style>
                """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
