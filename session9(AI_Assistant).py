# Step 1: Importing Libraries
from math import e
import streamlit as st
import google.generativeai as genai

# Step 2: Main App Setup
st.title('Studying AI Assistant')
subjects_options = ['Biology', 'Chemistry', 'Physics', 'Mathematics', 'Computer Science', 'English']
details_options = ['Breif', 'Meduim', 'Detailed'] 
tone_options = ['Formal', 'Informal', 'Friendly', 'Professional', 'Academic', 'Casual']
education_level_options = ['Elementary', 'Junior','Middle School', 'Senior', 'High School']

# Step 3: API kep section
API_key = st.text_input('Enter your Gemeni key:', type='password')

if API_key:
    genai.configure(api_key=API_key)
    model = genai.GenerativeModel('gemini-1.5-pro')

    # First row
    col1, col2 = st.columns(2)
    subject = col1.selectbox('Choose a subject:', subjects_options)
    details = col2.selectbox('Choose details level', details_options)

    # Second row
    col3, col4 = st.columns(2)
    tone = col3.selectbox('Choose a tone:', tone_options)
    education_level = col4.selectbox('Choose educational level:', education_level_options)

    # Taking user question
    user_input = st.text_area('Enter your question:', height=150)

    # Generating response
    if st.button('Get Answer'):
        prompt = f'''
        you are an AI studying assistant helping a {education_level}
        level student with {subject}.
        Answer in a {tone} tone and provide a {details}
        explanation
        The question is:
        {user_input}
        '''

        try:
            response = model.generate_content(prompt)
            st.write(response.text) #law mn8eer .text httl3 json
        except:
            st.error('An error occured')
        
        GEMINI_KEY = 'AIzaSyA6VLecXZswze6SEihl8a-HOTzzkS1A78E'



