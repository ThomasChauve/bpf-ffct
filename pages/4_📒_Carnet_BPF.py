import streamlit as st
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Carnet BPF", page_icon="📒")

with st.sidebar:
    st.session_state['data_bpf'].to_csv('tmp_bpf.csv')
    st.download_button('Télécharger les données .csv',data=Path('tmp_bpf.csv').read_text(),file_name='list_BPF.csv')

st.title('Carte BPF')

sum_type = st.selectbox('Satistique pour ',np.unique(st.session_state['data_bpf'].Departement))

tmp_df= st.session_state['data_bpf'][st.session_state['data_bpf'].Departement==sum_type]
tmp=np.array(tmp_df.Ticks)
tmp_pc=np.sum(tmp)/len(tmp)
st.progress(tmp_pc, text=sum_type+': '+str(np.int64(np.sum(tmp)))+'/'+str(len(tmp)))

