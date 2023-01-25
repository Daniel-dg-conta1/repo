import streamlit as st


st.sidebar.title('menu')
paginaSelecionada=st.sidebar.selectbox('Selecione a página',['Página 1', 'Página 2'])

if paginaSelecionada== 'Página 1':
    st.title('Video Exemplo')
    st.selectbox('Selecione uma opção',['opção 1', 'opção 2'])
elif paginaSelecionada== 'Página 2':
    st.title('Você selecionou a página 2')
