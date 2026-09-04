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

# =====================================================================
# 2. TEXTOS E TIPOGRAFIA
# =====================================================================
# st.expander cria uma caixa que abre e fecha para organizar a tela
with st.expander("📝 1. TEXTOS E TIPOGRAFIA (Clique para abrir)", expanded=True):
    st.title("Isso é um st.title() - Título Gigante")
    st.header("Isso é um st.header() - Subtítulo Grande")
    st.subheader("Isso é um st.subheader() - Tópico")
    
    st.markdown("**Texto em Negrito** feito com st.markdown()")
    st.markdown("*Texto em Itálico* feito com st.markdown()")
    
    st.write("O st.write() é o coringa! Ele escreve textos normais e substitui o antigo print().")
    