import streamlit as st
import numpy as np
import pandas as pd
import io
import os
import datetime
from random import randrange
from datetime import timedelta


st.set_page_config(
    page_title="Brevet des Provinces Francaise",
    page_icon="🚲",
)

with st.sidebar:
    st.session_state['data_bpf'].to_csv('tmp'+str(k)+'.csv',sep=';')
    st.download_button('Télécharger les données .csv',data=Path('tmp'+str(k)+'.csv').read_text(),file_name='list_BPF.csv')
    
st.title('Brevet des Provinces Francaise')

st.warning("Une fois les modifications réalisées n'oublié pas de télécharger vos données mise à jour.", icon="⚠️")

st.header('Charger les données')

st.session_state['d_date']=datetime.date.today()

if 'data_bpf' not in st.session_state:
    df=pd.read_csv('BPF.csv')
    df['Date']=np.full(len(df),None)
    df['Ticks']=np.zeros(len(df))
    st.session_state['data_bpf']=df

def data_load(file):
    data=pd.read_csv(file)
    return data

uploaded_file=st.file_uploader('Charger fichier ".csv"',accept_multiple_files=True, type='csv', label_visibility="visible")
if uploaded_file is not None:
    for f in uploaded_file:
        st.session_state['data_bpf'].append(data_load(f))