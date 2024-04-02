import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg', width=300)
with col2:
    st.title('Martin Novak')
    content = """
    Hello, I am Martin and I am a web analytic at Notino.
    """
    st.write(content)

