import google.generativeai as palm

api_key = "AIzaSyBpwzDczq9AHjqJfcxhJfHKbr2GNvE9ECE" 
palm.configure(api_key=api_key)
model = palm.get_model("models/chat-bison-001")  

def initialize_palm():
    """Initializes the PaLM Chat-Bison-001 model."""
    # No need to define model here anymore
    return model

#Function to debug a code snippet
def debug_code(code_snippet):
    prompt = "promptf-Debug the following code and provide suggestions for fixing errors: \n\n[code_snippet)"
    response = palm.chat(model=model,messages=[prompt])
    return response.candidates[0]["content"]


