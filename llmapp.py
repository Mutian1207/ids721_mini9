import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline
model = pipeline("text-generation", model="openai-gpt")

def streamInterface():

    st.title('LLM app')
    text = st.text_area("Enter text to ask chatbot:")

     
    if st.button("Generate"):

        if text:
            content = model(text, max_length=100, num_return_sequences=1)[0]['generated_text']
            st.write("Answer:")
            st.write(content)
        else:
            st.warning("Please enter text to ask chatbot.")
            
if __name__ == "__main__":  
    streamInterface()
    