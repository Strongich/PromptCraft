from langchain.chains.retrieval_qa.base import RetrievalQA
from create_retriever import create_retriever
from langchain.prompts import PromptTemplate

def create_chain(llm, template):
    retriever = create_retriever()
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    llm_chain = RetrievalQA.from_llm(llm=llm, retriever=retriever, prompt=prompt)
    return llm_chain
