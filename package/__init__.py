from langchain_community.llms import Ollama
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_community.embeddings import OllamaEmbeddings

url = 'http://localhost:11434'
model = 'llama3'

embedding = OllamaEmbeddings(base_url=url, model=model)
llm = Ollama(base_url=url, model=model, temperature=0)
agent_llm = OllamaFunctions(base_url=url, model=model, format="json", temperature=0)