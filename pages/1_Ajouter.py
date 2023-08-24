import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Ajouter un BPF",layout="wide", page_icon="📊")

add_code = st.selectbox('Selectionner le BPF',st.session_state['data_bpf'])

f_date=st.date_input('Date',value=st.session_state['d_date'], label_visibility="visible")

id=list(st.session_state['data_bpf'].Ville).index(add_code)

st.write('You selected:', id)