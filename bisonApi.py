import requests

API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your actual API key

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
