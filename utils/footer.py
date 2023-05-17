
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
                .st-bk,[role="alert"],input[type]:not([type="number"]),
                [data-baseweb="input"]:not(:has([type="number"])),
                [data-baseweb="textarea"],button[kind],
                [data-testid="stForm"], .focused.focused {
                    border-radius: 8px;
                }
                [data-baseweb="input"]:has([type="number"]) {
                    border-top-left-radius: 8px;
                    border-bottom-left-radius: 8px;
                }
                button.step-up.step-up {
                    border-top-right-radius: 8px;
                    border-bottom-right-radius: 8px;
                }
                [role="tab"] {
                    border-radius: 8px;
                    padding: 0 16px;
                    height: 30px;
                    margin-bottom: 4px;
                }
                [role="tab"].st-da,[role="tab"]:focus { background-color: #f1f2ff;  }
                .st-d2 { gap: 0.5rem }
                pre:has(.language-toml) { 
                    background-color: rgba(28, 131, 225, 0.1); 
                    color: rgb(0, 66, 128); 
                }
                .language-toml {white-space: pre-wrap !important;}
                hr {margin: 1em 0}
                </style>
                """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
