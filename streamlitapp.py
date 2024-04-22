import os
import json
import streamlit as st
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain
from src.mcqgenerator import logger
import data
from src.mcqgenerator.utils import *

# Load the JSON file
with open(r"C:\Users\vk\mcqgeneratorproject\data\sample.json", "r") as f:
    json_file = json.load(f)

def main():
    st.title("Generate Multiple Choice Questions")
    st.markdown("---")
    st.subheader("Customize Your Quiz")
    st.markdown("Upload a text file and specify parameters to generate multiple-choice questions.")

    # Create a form
    with st.form("my_form"):
        # File Upload
        uploaded_file = st.file_uploader("Upload a text file (.txt)")
        st.markdown("---")
        # User Inputs
        numquestions = st.number_input("Number of questions", min_value=1, max_value=50, value=5, step=1)
        subject = st.text_input("Subject", "")
        tone = st.radio("Tone", ("Simple", "Complex"))
        st.markdown("---")
        submitted = st.form_submit_button("Generate Questions")
        if submitted and uploaded_file is not None and numquestions and subject and tone:
            with st.spinner("Generating..."):
                try:
                    file = read_file(uploaded_file)
                    answer = generate_evaluate_chain(
                        {
                            "text": file,
                            "number": numquestions,
                            "subject": subject,
                            "tone": tone.lower(),  # Convert to lowercase
                            "response_json": json.dumps(json_file)
                        }
                    )
                    st.markdown("---")
                    st.subheader("Generated Questions")
                    st.markdown("---")
                    st.write(answer['query'])
                except:
                    raise Exception("An error occurred. Please try again.")
        elif submitted:
            st.error("Please fill in all fields and upload a file.")

if __name__ == "__main__":
    main()
