#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:16:13 2021

@author: crodri
"""


import spacy_streamlit
import streamlit as st

models = ["ca_bsc_demo_trf","ca_core_news_md","ca_core_news_trf"]
st.set_page_config(page_title="CA Spacy demo", page_icon="aina_small.jpg", layout='wide', initial_sidebar_state='auto')
default_text = "Aquest dissabte, Francesc Solé va arribar a la meta a Ordino com el guanyador del Ultra Trail d'Andorra després de 170km amb un desnivell altitudinal de 13 500 metres, en un temps de 31 hores i 9 minuts.   "
st.title("Demo de les pipelines  d'Spacy 3.4 per al català")
st.subheader("*Trieu un model a la dreta*")
visualizers = ["ner", "similarity", "tokens","parser", "textcat"]
similarity_texts = ('gos','gat')
spacy_streamlit.visualize(models, default_text, visualizers, similarity_texts=('gos','gat'), show_visualizer_select=True,sidebar_title="Visualització models Spacy-AINA",sidebar_description="Es pot triar el model i la funcionalitat de la visualització")
#streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081 --browser.serverAddress http://aina.bsc.es
