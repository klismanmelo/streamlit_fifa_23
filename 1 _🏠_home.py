from datetime import datetime
import streamlit as st
import pandas as pd
import webbrowser

if "data" not in st.session_state:
    df_data = pd.read_csv("dataset/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA 23 OFFICIAL DATASET ⚽️")

st.sidebar.markdown("Desenvolvido por [Klisman Melo]('https://github.com/klismanmelo')")

btn = st.button("Acesse os dados no Kagle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
Aqui vai uma descricao sobre o dataset do kaggle    

"""
)