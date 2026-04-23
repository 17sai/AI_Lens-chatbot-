from app.retriever import retrieve_relevant

def get_news(query):
    return retrieve_relevant(query)