import streamlit as st
import pandas as pd
from utils import *

st.title('Literature Model Explorer')

data = load_data()

if not data.empty:
    # Sidebar for Filters
    st.sidebar.header('Filters')
    model_names = data['Model Name'].unique()
    selected_model = st.sidebar.selectbox('Model Name', model_names)

    # Improved Filter: Allowing selection of "All" or specific values
    engineering_options = ['All'] + list(data['Is it useful in engineering courses?'].unique())
    selected_engineering_option = st.sidebar.selectbox('Useful in Engineering Courses?', engineering_options)

    # Apply Filters
    filtered_data = data
    if selected_engineering_option != 'All':
        filtered_data = filtered_data[filtered_data['Is it useful in engineering courses?'] == selected_engineering_option]

    if selected_model != 'All':
        filtered_data = filtered_data[filtered_data['Model Name'] == selected_model]

    if not filtered_data.empty:
        # Displaying models in columns
        for i, row in filtered_data.iterrows():
            st.markdown(f"### {row['Model Name']}")
            st.markdown(f"**Responsible Partner:** {row['Responsible partner']}")
    
            with st.expander("See more details"):
                            st.write(f"**Short Background:** {row['Short Background']}")
                            st.write(f"**Short Description:** {row['Short Description']}")
                            st.write(f"**Citing sources:** {row['Citing sources']}")
                            st.write(f"**Design (Scheme and source):** {row['Design (Scheme and source)']}")
                            st.write(f"**Fields the model can or was used in:** {row['Other - which fields the model can or was used in; website(s) describing the model']}")
                            st.write(f"**Useful in Engineering Courses:** {row['Is it useful in engineering courses?']}")
            # st.markdown("---")  # Divider         
    else:
        st.error("No data available for the selected filters.")

st.sidebar.header("Questionnaire")
if st.sidebar.button('Start Questionnaire'):
    show_questionnaire = True
else:
    show_questionnaire = False

# Questionnaire Section
if show_questionnaire:
    st.header('Questionnaire')
    st.write('Please answer the following questions with a rating from 0 to 5.')

    # Define questions
    questions = [
        "How useful do you find the content?",
        "Is the interface user-friendly?",
        "How informative is the data?",
        "How likely are you to recommend this to others?",
        "Is the data presented in a clear manner?",
        # Add more questions to match your total of 15
    ]
    
    # Ensuring we have exactly 15 questions
    questions += ["Question " + str(i) for i in range(len(questions)+1, 16)]

    # Initialize a dictionary to store responses
    responses = {}

    # Generate a selectbox for each question
    for i, question in enumerate(questions, start=1):
        response = st.slider(question, 0, 5, 0, key=f"Q{i}", format="%d")
        responses[f"Q{i}"] = response

    # Submit Button for the Questionnaire
    if st.button('Submit Responses'):
        st.write("You've submitted the following responses:")
        for question, response in responses.items():
            st.write(f"{question}: {response}")