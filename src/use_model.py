from langchain_community.llms import LlamaCpp


def get_llm():
    llm = LlamaCpp(
        model_path="./model/mistral-7b-instruct-v0.2.Q8_0.gguf",
        temperature=0,
        max_tokens=2048,
        use_mmap=True,
        use_mlock=False,
        n_ctx=1024,
        n_gpu_layers=22,
        n_batch=512,
        top_k=20,
        verbose=True,
    )
    return llm
