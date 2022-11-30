#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:16:13 2021

@author: crodri
"""


import spacy_streamlit
import streamlit as st
from spacy_streamlit.util import Demotype

models = ["ca_bsc_demo_trf","ca_core_news_md","ca_core_news_trf"]
st.set_page_config(page_title="CA Spacy demo", header_title="Spacy", layout='wide', initial_sidebar_state='auto', menu_items={
    'Get Help': 'https://huggingface.co/projecte-aina',
    'Report a bug': 'https://github.com/projecte-aina/spacy_ca_demo/issues',
    'About': None})
default_text = "El Futbol Club Barcelona, ​​conegut popularment com a Barça, és una entitat poliesportiva amb seu a Barcelona."
st.title("Demo de les pipelines  d'Spacy 3.4 per al català")
st.subheader("*Trieu un model a la dreta*")
visualizers = ["ner", "similarity", "tokens","parser", "textcat"]
similarity_texts = ('gos','gat')
spacy_streamlit.visualize(models, default_text, visualizers, similarity_texts=('gos','gat'), show_visualizer_select=True,sidebar_title="Visualització models Spacy-AINA",sidebar_description="Es pot triar el model i la funcionalitat de la visualització", demo_type=Demotype.AINA)
#streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081 --browser.serverAddress http://aina.bsc.es
