import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Cartes des BPF",layout="wide", page_icon="📊")


index=self.cols.columns

fig_map = px.scatter_mapbox(st.session_state['data_bpf'], lat=index[4], lon=index[3], hover_name=index[1], hover_data=[index[0], index[2],index[6]],
                        color_discrete_sequence=["blue"], zoom=4)
fig_map.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig_map, use_container_width=True, sharing="streamlit")