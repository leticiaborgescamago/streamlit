# =====================================================================
# APOSTILA EXECUTÁVEL STREAMLIT: O GUIA DEFINITIVO DO SENAI
# Rode este arquivo para ver todos os comandos funcionando na prática!
# =====================================================================

import streamlit as st
import pandas as pd
import time
import numpy as np

# =====================================================================
# 1. CONFIGURAÇÃO INICIAL (Sempre na linha 1)
# =====================================================================
st.set_page_config(page_title="Apostila Streamlit", page_icon="📘", layout="wide")

# O Menu Lateral (Sidebar)
st.sidebar.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=500", caption="Apostila Interativa")
st.sidebar.title("Navegação Lateral")
st.sidebar.info("Tudo que usar 'st.sidebar' vem parar aqui neste menu escuro!")

