import streamlit as st
import random

st.header('주사위 게임', divider='rainbow')
st.write('신유정')
clicked=st.button('주사위던지기',type='primary')
if clicked:
    n=random.randit(1,6)
    st.image(f'./img/{n}.png')