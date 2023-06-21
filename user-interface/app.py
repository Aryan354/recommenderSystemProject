import streamlit as st
import pickle
import pandas as pd


def recommend(uni):
    uni_index = unis[unis['Uni Name'] == uni].index[0]
    distance = similarity[uni_index]
    uni_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_unis = []
    for i in uni_list:
        recommended_unis.append(unis.iloc[i[0]])
    return recommended_unis


similarity = pickle.load(open('similarity.pkl', 'rb'))
uni_list = pickle.load(open('dataset.pkl', 'rb'))
unis = pd.DataFrame(uni_list)

st.title('University Recommender System Project')

selected_uni = st.selectbox(
    'Which university are you thinking about?',
    unis['Uni Name'])

if st.button('Recommend'):
    uni_data = recommend(selected_uni)
    st.write("Recommended Universities:")
    for i, uni in enumerate(uni_data, start=1):
        with st.container():
            st.subheader(f"#{i} - {uni['Uni Name']}")
            st.write("State:", uni['State'])

