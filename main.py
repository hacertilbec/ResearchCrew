import streamlit as st
from crew import crew

st.title('Related Work Generator')
# Inputs
topic = st.text_input('Research Topic', '')
proposed_work = st.text_area('Proposed Work', '')
number_of_articles = st.number_input('Number of articles', min_value=1, step=1)

if topic and proposed_work and number_of_articles:
    if st.button('Generate Related Work'):
        with st.spinner('in progress...'):
            related_work = crew(proposed_work, topic, number_of_articles)
            st.success('success')
            st.write('Generated Related Work:')
            st.write(related_work)
else:
    st.warning('Please fill in all fields.')
