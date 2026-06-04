import streamlit as st
from datetime import datetime

# Configuração da página para um visual mais profissional
st.set_page_config(page_title="Consultório Oftalmológico", page_icon="👁️")

# Estilo personalizado (Skill #Legendas Elegantes)
st.title("👁️ Agendamento de Consultas")
st.markdown("""
### Bem-vindo ao seu cuidado ocular de excelência.
*Agende sua consulta de forma rápida e segura. Escolha abaixo o melhor momento para cuidarmos da sua visão.*
""")

st.divider()

# Lógica de seleção
data = st.date_input("Selecione a data da consulta", min_value=datetime.today())
horario = st.selectbox("Escolha o horário disponível (Intervalos de 30min)", 
                      ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30"])

nome = st.text_input("Nome completo do paciente")

if st.button("Confirmar Agendamento"):
    if nome:
        st.success(f"Solicitação enviada com sucesso para {nome} no dia {data} às {horario}!")
        st.balloons()
    else:
        st.warning("Por favor, insira o nome do paciente para continuar.")

st.sidebar.info("📍 Localização: [Seu Endereço Aqui]\n\n📞 Contato: (XX) XXXX-XXXX")
