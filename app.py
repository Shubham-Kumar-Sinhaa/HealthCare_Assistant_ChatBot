import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")

def healthCare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for more accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with Doctor?"
    elif "medication" in user_input:
        return "It is important to consume pescribed medicines regularly. If you have concerns, consult your Doctor"
    else:
        response = chatbot(user_input, max_length=350, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("HealthCare Assistant ChatBot")
    user_input = st.text_input("How can I assist you?")
    if st.button("Submit"):
        if user_input:
            st.write("User : ",user_input)
            with st.spinner("Processing, Please wait ...."):
                response = healthCare_chatbot(user_input)
            st.write("Healthcare Assistant : ",response)
        else:
            st.write("Please enter a query to get a response")

if __name__=="__main__":
    main()
