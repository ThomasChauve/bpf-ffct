import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Recapitulatif des BPF",layout="wide", page_icon="📈")

st.title('Statistiques')
tmp=np.array(st.session_state['data_bpf'].Ticks)
pc_all=np.sum(tmp)/len(tmp)

st.progress(pc_all, text='Nombres de BPF'+str(np.sum(tmp))+'/'+str(len(tmp)))