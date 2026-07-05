from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from app.core.retrieval import retrieve_context
from config.settings import settings

def ask_bot(question: str):
    context = retrieve_context(question)
    
    template = """
    You are an expert Data Science assistant. 
    Use the provided context to answer the question thoroughly and in detail.
    Explain the concepts clearly, use bullet points if necessary to make it easier to read.
    If the information is not in the context, say that you don't know.
    
    Context: {context}
    
    Question: {question}
    
    Detailed Answer:
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    
    model = ChatOllama(model=settings.LLM_MODEL)
    
    chain = prompt | model
    
    response = chain.invoke({"context": context, "question": question})
    
    return response.content