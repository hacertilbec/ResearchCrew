import streamlit as st
from crew import crew

# Arayüz başlığı
st.title('Related Work Generator')


# Input alanları
topic = st.text_input('Research Topic', '')
proposed_work = st.text_area('Proposed Work', '')
number_of_articles = st.number_input('Number of articles', min_value=1, step=1)

# Inputların zorunlu olduğunu belirten kontrol
if topic and proposed_work and number_of_articles:
    if st.button('Generate Related Work'):
        with st.spinner('in progress...'):
            related_work = crew(proposed_work, topic, number_of_articles)

            # Üretilen sonucu gösterme
            st.success('success')
            st.write('Generated Related Work:')  # Üretilen text burada gösterilecek
            # Örneğin:
            st.write(related_work)
else:
    st.warning('Please fill in all fields.')

#proposed_work = "In this project, for the first time, an additional signal beyond clicks will be added to a Bayesian click model. This model will offer a new perspective and its comparison with existing click models will contribute to the literature. Another significant innovation we will introduce is adapting these click models, which are developed for search engines, to the business models of online marketplaces. In doing so, we will incorporate the user’s subsequent steps in their search journey into the model.\n"
#topic = "Bayesian Click Models\n"
#number_of_articles = 5