import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Recapitulatif des BPF", page_icon="📈")

with st.sidebar:
    st.session_state['data_bpf'].to_csv('tmp'+str(k)+'.csv',sep=';')
    st.download_button('Télécharger les données .csv',data=Path('tmp'+str(k)+'.csv').read_text(),file_name='list_BPF.csv')
    
st.title('Statistiques')
tmp=np.array(st.session_state['data_bpf'].Ticks)
pc_all=np.sum(tmp)/len(tmp)

st.progress(pc_all, text='Nombres de BPF: '+str(np.int64(np.sum(tmp)))+'/'+str(len(tmp)))

sum_type = st.selectbox('Satistique pour ',['Province','Departement'])

for pp in np.unique(st.session_state['data_bpf'][sum_type]):
    tmp_df= st.session_state['data_bpf'][st.session_state['data_bpf'][sum_type]==pp]
    tmp=np.array(tmp_df.Ticks)
    tmp_pc=np.sum(tmp)/len(tmp)
    st.progress(tmp_pc, text=pp+': '+str(np.int64(np.sum(tmp)))+'/'+str(len(tmp)))
