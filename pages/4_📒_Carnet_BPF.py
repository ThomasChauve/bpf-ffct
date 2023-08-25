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

col1, col2, col3 = st.columns(3)

with col1:
    for i in [0,1]:
        st.header(tmp_df.Ville.loc[i])
        if tmp_df.Ticks.loc[i]==1:
            st.write(tmp_df.Date.loc[i])
            if tmp_df.Photo.loc[i] is not None:
                st.image(tmp_df.Photo.loc[i])

if len(tmp_df)>2:
    with col2:
        for i in [2,3]:
            st.header(tmp_df.Ville.loc[i])
            if tmp_df.Ticks.loc[i]==1:
                st.write(tmp_df.Date.loc[i])
                if tmp_df.Photo.loc[i] is not None:
                    st.image(tmp_df.Photo.loc[i])

    with col3:
        for i in [4,5]:
            st.header(tmp_df.Ville.loc[i])
            if tmp_df.Ticks.loc[i]==1:
                st.write(tmp_df.Date.loc[i])
                if tmp_df.Photo.loc[i] is not None:
                    st.image(tmp_df.Photo.loc[i])