# PromptCraft

## Overview 
Welcome to PromptCraft, an educational app for prompt engineering training.

Engage in the fascinating task of crafting prompts that serve as the key to unlocking the model's proficiency in responding to questions, related on `imdb_movie_data_2023.csv` file. Delve into the intricacies of prompt engineering, following the instructions provided below to fine-tune your approach. Witness the journey of optimizing prompt formulation unfold, leading to precise and accurate model responses. Your contribution to this process shapes a dynamic exploration into the world of natural language understanding and generation.

## Objective

Explore and actively engage in the practice of prompt engineering utilizing an **Open-Source** model. Gain a comprehensive understanding and hands-on experience with the process, fostering a practical approach to enhance your skills in shaping model responses.

## Models

1. **LLM:** `Mistral-7b-instruct-v0.2.Q8`
2. **Embedding:** `all-MiniLM-L6-v2`
3. **VectorDB:** `FAISS`

## Usage
> **Important:**
>
> Running the LLM model on your local machine is a prerequisite for using this app. Depending on your GPU specifications:
>
> - If your GPU has less than 6GB of VRAM, modify the `n_gpu_layers=22` parameter in the `use_model.py` file.
>
> - If your videocard boasts a minimum of 10GB of VRAM, consider setting `n_gpu_layers=-1` to optimize processing speed.
>
> - Keep in mind, similar to my situation, you must also ensure sufficient RAM to run this model efficiently on both GPU and CPU.

### **To use this app, follow the instructions below:**

1. First clone the repository. To do this, open a terminal, go to the directory where you want to clone the project and then enter the command:
```bash
git clone https://github.com/Strongich/PromptCraft.git
```
2. Go to folder with project and install virtualenv, write the following command and press Enter:
```bash
pip install virtualenv
```
3. Next create a new environment, write the following command and press Enter:
```bash
virtualenv name_of_the_new_env
```
### Example:
```bash
virtualenv promptcraft
```
4. Next activate the new environment, write the following command and press Enter:
```bash
name_of_the_new_env\Scripts\activate
```
### Example:
```bash
promptcraft\Scripts\activate
```
5. Write the following command and press Enter:
 ```bash
pip install -r requirements.txt
```
6. To launch the backend for model, open folder with project and write the following command and press Enter:
```bash
python src/backend.py
```
6. To launch the frontend for model, open folder with project and write the following command and press Enter:
```bash
streamlit run src/ui.py
```
7. Open this link in your browser [http://localhost:8501](http://localhost:8501) and you free to go!

## Conclusion

In this project, we have developed an application for the prompt engineering process. This application utilizes an open-source LLM model, a custom vector database, and an embedding system to answer questions related to our `imdb_movie_data_2023_1.csv` file.

For comprehensive implementation instructions and examples, please consult the project documentation and code. Enjoy your prompt engineering journey!

## Author

This PromptCraft app was created by Vitenko Igor. If you have any questions or require further assistance, feel free to contact igor.vitenko13@gmail.com.

