import streamlit as st
import pandas as pd
from utils import *

st.set_page_config(page_title="Village project model database", layout="wide")

add_logo()
st.title("Village project model database")


data = load_data()

if not data.empty:
    # Sidebar for Filters
    st.sidebar.header("Filters")
    model_names = data["Model Name"].unique()
    ranked_model_names = data.loc[data["Ranked"] == True]["Model Name"].unique()
    ranked_models = st.sidebar.checkbox("Show only ranked models")

    if not ranked_models:
        selected_model = st.sidebar.selectbox("Model Name", model_names)
    else:
        selected_model = st.sidebar.selectbox("Model Name", ranked_model_names)
    # Improved Filter: Allowing selection of "All" or specific values
    engineering_options = ["All"] + list(
        data["Is it useful in engineering courses?"].unique()
    )
    # selected_engineering_option = st.sidebar.selectbox(
    #     "Useful in Engineering Courses?", engineering_options
    # )

    selected_engineering_option = "All"
    # Apply Filters
    filtered_data = data
    if selected_engineering_option != "All":
        filtered_data = filtered_data[
            filtered_data["Is it useful in engineering courses?"]
            == selected_engineering_option
        ]

    if selected_model != "All":
        filtered_data = filtered_data[filtered_data["Model Name"] == selected_model]

    if not filtered_data.empty:
        # Displaying models in columns
        for i, row in filtered_data.iterrows():
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.markdown(f"### Model: {row['Model Name']}")

            with col2:
                st.markdown("   ")
                st.markdown("###### Integration the VR LAB*: ")
                st.caption("###### *According to the evaluation of 20 experts")

            with col3:
                try:
                    rating_str = "⭐️" * int(
                        row["Number of starts (out of 5)"]
                    ) + "☆" * (5 - int(row["Number of starts (out of 5)"]))
                    st.markdown("   ")
                    st.markdown(
                        f"###### {rating_str} ({row['Number of starts (out of 5)']}/5)"
                    )

                except Exception as e:
                    print("No stars")
            st.markdown(f"**Responsible Partner:** {row['Responsible partner']}")
            st.write(f"**Short Background:** {row['Short Background']}")
            with st.expander("See more details"):
                st.write(f"**Short Description:** {row['Short Description']}")
                st.write(f"**Citing sources:** {row['Sources']}")
                st.write(
                    f"**Useful in Engineering Courses:** {row['Is it useful in engineering courses?']}"
                )
                st.divider()
                loaded_image = find_and_load_image(selected_model)
                if loaded_image:
                    display_image(
                        loaded_image
                    )  # This will display the image if it's successfully loaded
                else:
                    st.error("Failed to find or load the image.")

            # st.markdown("---")  # Divider
    else:
        st.error("No data available for the selected filters.")

file_url = "https://zenodo.org/communities/villageproject/records?q=&l=list&p=1&s=10&sort=newest"
st.sidebar.markdown(f"[Access data in Zenodo]({file_url})", unsafe_allow_html=True)

# download_button = st.sidebar.audiodownload_button(
#     label="Download dataset",
#     data=data,
#     type="secondary",
#     file_name=""file_name"",
# )
# st.sidebar.header("Questionnaire")
# if st.sidebar.button("Start Questionnaire"):
#     show_questionnaire = True
# else:
#     show_questionnaire = False

# # Questionnaire Section
# if show_questionnaire:
#     st.header("Questionnaire")
#     st.write("Please answer the following questions with a rating from 0 to 5.")

#     # Define questions
#     questions = [
#         "How useful do you find the content?",
#         "Is the interface user-friendly?",
#         "How informative is the data?",
#         "How likely are you to recommend this to others?",
#         "Is the data presented in a clear manner?",
#         # Add more questions to match your total of 15
#     ]

#     # Ensuring we have exactly 15 questions
#     questions += ["Question " + str(i) for i in range(len(questions) + 1, 16)]

#     # Initialize a dictionary to store responses
#     responses = {}

#     # Generate a selectbox for each question
#     for i, question in enumerate(questions, start=1):
#         response = st.slider(question, 0, 5, 0, key=f"Q{i}", format="%d")
#         responses[f"Q{i}"] = response

#     # Submit Button for the Questionnaire
#     if st.button("Submit Responses"):
#         st.write("You've submitted the following responses:")
#         for question, response in responses.items():
#             st.write(f"{question}: {response}")
