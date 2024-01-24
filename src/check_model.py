import requests
import os
from tqdm import tqdm


def is_directory_empty(directory_path="./model/"):
    if not os.path.exists(directory_path):
        print("making dir")
        os.makedirs(directory_path)
    return len(os.listdir(directory_path)) == 0


def download_llm(
    url="https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q8_0.gguf",
    local_filename="./model/mistral-7b-instruct-v0.2.Q8_0.gguf",
):
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get("content-length", 0))

    with open(local_filename, "wb") as output_file, tqdm(
        desc="Downloading",
        total=file_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                output_file.write(chunk)
                bar.update(len(chunk))
