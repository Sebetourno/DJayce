import streamlit as st
import requests

# URL of your Pipedream workflow
PIPEDREAM_URL = "https://eomyc5p5pl1x9x0.m.pipedream.net"

# Application title
st.title("DJayce - Your Electro Music Assistant")

# User interface
st.markdown("### Ask a question to DJayce:")
prompt = st.text_input("Question", placeholder="Example: Can you recommend an electro playlist?")

if st.button("Send"):
    if prompt:
        try:
            response = requests.post(PIPEDREAM_URL, json={"prompt": prompt})
            if response.status_code == 200:
                st.text_area("Response from DJayce", response.json().get("response", "No response received."))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a question.")
