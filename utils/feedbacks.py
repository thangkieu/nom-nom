import streamlit as st
import requests


def render_feedbacks(name: str,
                     label1: str = None, label2: str = None):

    form = st.form(key=f"{name}_feedback_form")
    feedback = form.radio(
        "How would you rate this response?", ("👍", "👎"), horizontal=True)
    comment = form.text_area("Additional comments (optional)")

    if form.form_submit_button(label='Send feedback'):
        r = requests.post(url=st.secrets.get('LATIOS_API'),
                          json={"application_name":  st.secrets.get('LATIOS_APP_NAME'),
                                "label1":  label1,
                                "label2":  label2,
                                "label3":  feedback,
                                "label4":  comment,
                                "original_url": "https://nomnom.streamlit.app/"},
                          headers={
                              "Content-Type": "application/json",
                              "Authorization": f"Bearer {st.secrets.get('JWT_TOKEN')}"
        })
        resp = r.json()
        print(resp)
        # trigger latios
        latios_url = resp.get('short_url')
        if latios_url:
            with st.spinner('Sending...'):
                r = requests.get(latios_url)
                if r.status_code == 200:
                    st.success('Thank you for your feedback!')
