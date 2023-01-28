import pdfplumber
import streamlit as st
import streamlit as st
import pandas as pd
from io import StringIO

st.write("GPT Essay")

def extract_data(feed):
    data = []
    with pdfplumber.load(feed) as pdf:
        pages = pdf.pages
        for p in pages:
            data.append(p.extract_tables())
            st.write(p.extract_tables())
    return None


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    fdata = stringio

