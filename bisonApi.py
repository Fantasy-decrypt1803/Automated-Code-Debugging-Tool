import streamlit as st
import google.generativeai as palm

palm.configure(api_key="AIzaSyC_9Y-ZWMsE6g4SdcyAygNAHRaSWnmhdzU" )
model_name="models/chat-bison-001"
def debug_code(code_snippet):
prompt=f"Debug the following code and provide suggestions for fixing errors:\n\n{code_snippet}"

response=palm.chat(
       model=model_name,
       messages [prompt]

)

return response.candidates[0]["content"]
