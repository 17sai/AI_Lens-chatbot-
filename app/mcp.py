from app.functions import get_news

def decide_tool(query):
    # Always use news tool for this project
    return "get_news"


def execute_tool(tool_name, query):
    if tool_name == "get_news":
        return get_news(query)
    
    return []