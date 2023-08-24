import streamlit as st
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Cartes des BPF",layout="wide", page_icon="🗺️")

with st.sidebar:
    st.session_state['data_bpf'].to_csv('tmp_bpf.csv')
    st.download_button('Télécharger les données .csv',data=Path('tmp_bpf.csv').read_text(),file_name='list_BPF.csv')

st.title('Carte des BPF')


index=st.session_state['data_bpf'].columns


fig_map = px.scatter_mapbox(st.session_state['data_bpf'], lat=index[4], lon=index[3], hover_name=index[0], hover_data=[index[1], index[2], index[5]],
                    color='Ticks', zoom=4, color_continuous_scale=px.colors.sequential.Bluered_r)


fig_map.update_layout(mapbox_style="open-street-map")

fig_map.update(layout_coloraxis_showscale=False)

st.plotly_chart(fig_map, use_container_width=True, sharing="streamlit")