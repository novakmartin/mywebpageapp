import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg', width=300)
with col2:
    st.title('Martin Novak')
    content = """
    Hello, I am Martin and I am a web analyst at Notino.
    """
    st.write(content)

content2 = """
Below you can find some apps I built in Python. Feel free to contact me!
"""

st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')

no_of_apps = len(df.index)

with col3:
    for i, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for i, row in df[10:].iterrows():
        st.header(row['title'])
