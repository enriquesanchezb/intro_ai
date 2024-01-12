"""
This is a simple example of how to use the summarize chain.
"""
from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

loader = WebBaseLoader("https://es.vikidia.org/wiki/Perro_Sanxe")
docs = loader.load()

llm = Ollama(model="mistral")
chain = load_summarize_chain(llm, chain_type="stuff")
print("Summary about, who is perro sanxe?")
result = chain.invoke(docs)
print(result)
