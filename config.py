class Config:
    PAGE_TITLE = "Llama3 Chatbot - Disha Himani"

    OLLAMA_MODELS = ('llama3')

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic."""
    