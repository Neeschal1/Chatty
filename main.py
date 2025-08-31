# output in terminal

import google.generativeai as genai
from dotenv import load_dotenv
import os
import pyttsx3
import streamlit as st

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

st.title("Hello, World!")
st.text("Welcome to Chatty :)")

engine = pyttsx3.init()
# terminated_response = "Byebye. Take Care. See you soon :) \n"

def decide():
    decision = int(input('''\nPress 1 to continue, and press 2 to terminate the program: '''))
    func(decision)

def loop():
    # user_input = input("\nEnter anything: ")
    user_input = st.text_input("\nEnter anything: ")
    try: 
       response = model_of_AI.generate_content(user_input)
       engine.say(response.text)
       print(response.text)
       engine.runAndWait()
    except Exception as e:
       print("Error!! ", e)
    
def func(x):
    if(x == 1):
        loop()
        decide()
    else:
        # engine.say(terminated_response)
        # print(terminated_response)
        engine.runAndWait()
        pass
    
genai.configure(api_key=SECRET_KEY)
model_of_AI = genai.GenerativeModel('gemini-2.5-flash')

decide()