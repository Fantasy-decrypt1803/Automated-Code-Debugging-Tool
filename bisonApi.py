import streamlit as st
import google.generativeai as palm

palm.configure(api_key="AIzaSyC_9Y-ZWMsE6g4SdcyAygNAHRaSWnmhdzU" )
model_name="models/chat-bison-001"
def bison_request(code):
    try:
        response = requests.post(
            'https://chat-bison-api-endpoint.com',  # Replace with the actual endpoint
            json={'prompt': f'Find and fix the bug in the following code:\n{code}'},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        return response.json()
    except Exception as e:
        print(f'Error: {e}')
        return None
