import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Recapitulatif des BPF",layout="wide", page_icon="📈")

st.title('Statistiques')

pc_all=np.sum(st.session_state['data_bpf'].Ticks)/len(st.session_state['data_bpf'])

st.progress(pc_all, text='Nombres de BPF')