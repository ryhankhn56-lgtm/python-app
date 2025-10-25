import requests
import streamlit as st
from streamlit_lottie import st_lottie

#Find more emojis here: https://pythonandvba.com/emojify/
st.set_page_config(page_title="MY Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()

#---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/3952c2bb-d2d3-4b39-8482-cd4f6ac898c4/xZZIDl8jKY.lottie")



#---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, Iam Rehan :wave:")
    st.title("A Data Analyst From Pakistan")
    st.write("I am passionate about finding python and VBA to more efficient and effective in business settings.")
    st.markdown("[Learn More>](https://pythonandvba.com/grafly/)")
    st_lottie(lottie_coding, height=300, key="coding")