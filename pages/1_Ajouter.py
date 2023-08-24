import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Ajouter un BPF",layout="wide", page_icon="📊")

add_code = st.selectbox('Selectionner le BPF',st.session_state['data_bpf'])

f_date=st.date_input('Date',value=st.session_state['d_date'], label_visibility="visible")

id=list(st.session_state['data_bpf'].Ville).index(add_code)


# Add small map
index=st.session_state['data_bpf'].columns

fig_map = px.scatter_mapbox(st.session_state['data_bpf'].loc[id], lat=index[4], lon=index[3], hover_name=index[0], hover_data=[index[1], index[2]],
                        color_discrete_sequence=["blue"], zoom=4)
fig_map.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig_map, use_container_width=True, sharing="streamlit")