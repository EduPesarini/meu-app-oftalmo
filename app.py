import streamlit as st
from datetime import time

# Define o título do aplicativo
st.title('Agendamento Oftalmológico')

# Cria um seletor de data para o usuário escolher o dia da consulta
data_selecionada = st.date_input('Selecione a data da consulta')

# Cria uma lista de horários de 30 em 30 minutos das 08:00 às 18:00
horarios = []
for hora in range(8, 18):
    horarios.append(time(hora, 0))
    horarios.append(time(hora, 30))

# Cria um seletor para o usuário escolher o horário
horario_selecionado = st.selectbox('Selecione o horário', horarios)

# Cria o botão de confirmação
if st.button('Confirmar Agendamento'):
    # Exibe uma mensagem de sucesso com os dados escolhidos
    st.success(f'Agendamento confirmado para o dia {data_selecionada} às {horario_selecionado.strftime("%H:%M")}.')
