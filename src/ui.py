import streamlit as st
import requests
import pandas as pd
from questions import QUESTIONS
from main import start_model


def process_input_with_button(button_label, user_input_prompt, question):
    if st.button(button_label):
        with st.spinner("Processing..."):
            url = "http://127.0.0.1:8000/generate_answer"
            data_to_send = {
                "user_input_prompt": user_input_prompt,
                "question": question,
            }
            try:
                response = requests.post(url, json=data_to_send)
                response.raise_for_status()  # Raise an exception for HTTP errors
                result = response.json().get("answer", "Error: No answer received")
                st.markdown(f"### Answer: {result}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error during request: {e}")


def main():
    df = pd.read_csv("./data/imdb_movie_data_2023.csv", index_col=0)
    # Set page title and configure layout
    st.set_page_config(
        page_title="PromptCraft - Prompt Engineering Training",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Title and introduction
    st.title("PromptCraft")
    st.markdown(
        """
        ### Welcome to PromptCraft, an educational app for prompt engineering training. :smile:
        
        Your task is to write prompts that help the model respond effectively to pre-recorded questions. Follow the instructions below to optimize prompt formulation and obtain accurate model responses.
        """
    )

    # Objective section
    st.markdown("## :question: Objective")
    st.markdown(
        "Enhance the model's ability to answer pre-recorded questions through prompt engineering techniques."
    )

    # Procedure section
    st.markdown("## :gear: Procedure")
    st.markdown(
        "1. **Access the Dataset:** Utilize the provided dataset for prompt engineering training."
    )
    st.markdown(
        "2. **Formulate Prompts:** Create prompts that encourage the model to generate informative and accurate responses to pre-recorded questions."
    )
    st.markdown(
        "3. **Experimentation:** Explore different prompt styles, structures, and strategies to observe variations in the model's output."
    )

    # Dataset section
    st.markdown("## :book: Dataset")
    st.markdown(
        "[Link](https://www.kaggle.com/datasets/kianindeed/imdb-movie-dataset-dec-2023) to the Kaggle dataset."
    )

    # Display a sample of the dataset
    st.markdown("### Sample of the Dataset:")
    st.table(df.head(3))
    # gidelines
    st.markdown("## 📝 Guidelines")
    st.markdown(
        "- Be clear and concise in your prompts to ensure the model understands the context of the questions."
    )
    st.markdown(
        "- Experiment with keywords, context setting, or specific instructions to guide the model's responses."
    )
    st.markdown(
        "- Test multiple prompt iterations to observe how slight modifications influence the quality of generated answers."
    )
    # Example of usage
    st.markdown("## :question: How it works")
    template = """<s>[INST] 
    Your prompt here
    Context: {context} 
    Question: {question}[/INST]
    """
    st.code(template)
    st.markdown(
        "### Your Task: Copy this template, insert a prompt in the designated position, and verify if your **output** matches the actual values from the table."
    )
    st.markdown("## :dart: Example")
    st.markdown(
        "#### Here just tap **process input** and check result - no need to modify."
    )
    # Default text
    default_text = "This is the default text."
    example_prompt = """<s>[INST]
You have been assigned to answer a user's question using information from a context table that includes film data from IMDB. 
Follow the specified format instructions provided in the context table, if any.
Context: {context}
Question: {question}
[/INST]
"""
    example_question = (
        "Name me a single film from table with Leonardo DiCaprio in cast."
    )
    st.markdown(f"### :pushpin: Question: {example_question}")
    user_input_prompt = st.text_area("Enter prompt:", example_prompt, height=200)
    process_input_with_button("Process Input", user_input_prompt, example_question)
    st.markdown("### Actual value (you will see one of theese):")
    st.table(df[df["Cast"].str.contains("Leonardo DiCaprio")])
    st.markdown(
        "## 📝 Important: Please note that your single prompt is everything \
        the language model has to work with. \
            Make sure to include all relevant details and questions within that one prompt \
                for the best experience with this task. \
                Providing a comprehensive and clear prompt ensures a more accurate and \
                    meaningful response. When you entering new prompt dont forget to tap `CTRL+ENTER`.Good luck! :smile: "
    )

    question_0 = QUESTIONS[0]
    st.markdown(f"### :pushpin: Question: {question_0}")
    user_input_prompt_0 = st.text_area("Enter prompt 0:", default_text, height=200)
    process_input_with_button("Process Input 0", user_input_prompt_0, question_0)
    st.markdown("### Actual value:")
    st.table(
        df[
            df["Cast"].str.contains(
                "Natalie Portman, Chris Tenzis, Charles Melton, Julianne Moore"
            )
        ]
    )

    question_1 = QUESTIONS[1]
    st.markdown(f"### :pushpin: Question: {question_1}")
    user_input_prompt_1 = st.text_area("Enter prompt 1:", default_text, height=200)
    process_input_with_button("Process Input 1", user_input_prompt_1, question_1)
    st.markdown("### Actual value:")
    st.table(df.sort_values("Rating", ascending=False)[:5])

    question_2 = QUESTIONS[2]
    st.markdown(f"### :pushpin: Question: {question_2}")
    user_input_prompt_2 = st.text_area("Enter prompt 2:", default_text, height=200)
    process_input_with_button("Process Input 2", user_input_prompt_2, question_2)
    st.markdown("### Actual value:")
    st.table(
        df[df["Cast"].str.contains("Leonardo DiCaprio")]
        .sort_values("Duration", ascending=False)
        .iloc[0]
    )

    question_3 = QUESTIONS[3]
    st.markdown(f"### :pushpin: Question: {question_3}")
    user_input_prompt_3 = st.text_area("Enter prompt 3:", default_text, height=200)
    process_input_with_button("Process Input 3", user_input_prompt_3, question_3)
    st.markdown("### Actual value:")
    st.table(
        df[df["Director"].str.contains("Martin Scorsese")]
        .sort_values("Meta Score", ascending=False)
        .iloc[0]
    )

    question_4 = QUESTIONS[4]
    st.markdown(f"### :pushpin: Question: {question_4}")
    user_input_prompt_4 = st.text_area("Enter prompt 4:", default_text, height=200)
    process_input_with_button("Process Input 4", user_input_prompt_4, question_4)
    st.markdown(f"### Actual value: {len(df[df['Duration'] > 150])}")

    st.markdown(
    "## :+1: Great job! I hope you enjoyed the prompt engineering process and my questions! \
    In this section, you have the opportunity to input any question you desire and check the results. \
    Feel free to use the `check_data.ipynb` notebook for the actual answers! Give it a try!"
)
    user_input_question = st.text_input("Enter your question:", default_text)
    user_input_prompt_5 = st.text_area("Enter prompt 5:", default_text, height=200)
    process_input_with_button("Process Input 5", user_input_prompt_5, user_input_question)

if __name__ == "__main__":
    main()
