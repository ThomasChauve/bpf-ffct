import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Ajouter un BPF",layout="wide", page_icon="📊")

add_code = st.selectbox('Selectionner le BPF',st.session_state['data_bpf'])

st.text(add_code)