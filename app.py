import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração Visual Premium
st.set_page_config(page_title="Agendamento Premium Oftalmo", page_icon="👁️")

st.title("👁️ Consultório Oftalmológico")
st.subheader("Agendamento Exclusivo & Clube de Vantagens")

st.markdown("""
Bem-vindo ao nosso canal de atendimento prioritário. 
Aqui, sua visão é tratada com a exclusividade que você merece.
""")

st.divider()

# Formulário de Agendamento
with st.form("agendamento_form"):
    nome = st.text_input("Seu Nome Completo")
    data = st.date_input("Data Desejada", min_value=datetime.today())
    
    # Horários de 30 em 30 min
    horarios = [f"{h:02d}:{m:02d}" for h in range(8, 18) for m in (0, 30)]
    horario = st.selectbox("Horário Disponível", horarios)
    
    st.info("🎁 **Clube de Vantagens:** Ganhe bônus em seus procedimentos ao indicar novos pacientes!")
    indicacao = st.text_input("Quem indicou você? (Nome ou Código)")
    
    submit = st.form_submit_button("Confirmar Agendamento Premium")

if submit:
    if nome:
        # Aqui o app salva na sua planilha (via Streamlit Connections)
        st.success(f"Excelente, {nome}! Seu horário às {horario} no dia {data} foi pré-reservado.")
        st.balloons()
        st.write("---")
        st.write(f"**Resumo do Clube de Vantagens:**")
        st.write(f"Indicação registrada: *{indicacao if indicacao else 'Nenhuma'}*")
    else:
        st.error("Por favor, preencha seu nome para confirmar.")

st.sidebar.markdown("""
### Sobre o Clube
Indique colegas do prédio e acumule bônus para seus próximos exames ou procedimentos.
""")
