import streamlit as st
from bison_api import bison_request

st.title('Bugbuster: Automated Debugging Tool')

code = st.text_area('Enter your code here:')

if st.button('Debug Code'):
    result = bison_request(code)
    if result:
        corrected_code = result.get('corrected_code', 'No corrected code found.')
        st.write('Corrected Code:')
        st.code(corrected_code, language='python')
    else:
        st.error('Error: Unable to process request')

st.caption('Brought to you by Bugbuster')
