import streamlit as st
import os
import google.generativeai as genai 
from dotenv import load_dotenv 

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

genai.configure(api_key=SECRET_KEY)
model_of_AI = genai.GenerativeModel('gemini-2.5-flash')

st.title("Hello, World!")
st.text("Welcome to Chatty :)")

def user():
    user_input = st.text_input("Enter anything to ask to Neeschal's AI:")
    return user_input
    
ask_ai = user()
    
if st.button("Send"):
       response = model_of_AI.generate_content(ask_ai)
       st.write(response.text)
     