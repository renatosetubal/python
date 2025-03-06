import streamlit as st
import data as dt

st.title('Filmes')
nome = st.text_input('Nome do filme:')
ano = st.number_input('Ano de lançamento:', min_value=1980, max_value=2024)
nota = st.slider('Nota:', min_value=0.0, max_value=10.0, step=0.1)

if st.button('Adicionar'):
    dt.add_filme(nome, ano, nota)   
    st.success('Filme adicionado com sucesso!')

filmes = dt.lista_filmes()
st.header('Lista de filmes')
st.table(filmes)
