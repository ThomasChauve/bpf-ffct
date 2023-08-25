import streamlit as st
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Ajouter un BPF", page_icon="➕")

with st.sidebar:
    st.session_state['data_bpf'].to_csv('tmp_bpf.csv')
    st.download_button('Télécharger les données .csv',data=Path('tmp_bpf.csv').read_text(),file_name='list_BPF.csv')

st.title('Ajouter un BPF')

tmp_code_df=st.session_state['data_bpf'][st.session_state['data_bpf'].Ticks==0]

add_code = st.selectbox('Selectionner le BPF',tmp_code_df)

f_date=st.date_input('Date',value=st.session_state['d_date'], label_visibility="visible")

id=list(st.session_state['data_bpf'].Ville).index(add_code)

def photo_load(file):
    st.image(file)
    bytes_data = file.getvalue()
    return bytes_data

uploaded_photo=st.file_uploader('Charger photo', accept_multiple_files=False, label_visibility="visible")


if st.button('Ajouter'):
    st.session_state['data_bpf'].loc[id, 'Ticks'] = 1
    st.session_state['data_bpf'].loc[id, 'Date'] = f_date

    if uploaded_photo is not None:
        st.session_state['data_bpf'].loc[id, 'Photo']=photo_load(uploaded_photo)

    st.success(add_code+' est ajouté !', icon="✅")

# Add small map
index=st.session_state['data_bpf'].columns

tmp_df= st.session_state['data_bpf'][st.session_state['data_bpf'].Ville==add_code]
fig_map = px.scatter_mapbox(tmp_df, lat=index[4], lon=index[3], hover_name=index[0], hover_data=[index[1], index[2]],
                        color_discrete_sequence=["blue"], zoom=4)
fig_map.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig_map, use_container_width=True, sharing="streamlit")


