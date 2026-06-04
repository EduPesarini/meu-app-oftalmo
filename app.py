import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# Configuração Visual Premium
st.set_page_config(page_title="VIP Oftalmo", page_icon="👁️")

st.title("👁️ Oftalmologia de Excelência")
st.subheader("Canal Exclusivo & Clube de Vantagens")

# Conexão com a Planilha Google
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception as e:
    st.error("Erro na conexão com a planilha. Verifique se as permissões foram concedidas.")
    st.stop()

# Organização por Abas no App
tab1, tab2 = st.tabs(["📅 Solicitar Atendimento", "🎁 Indicar & Ganhar"])

with tab1:
    st.markdown("### Solicitação de Encaixe Prioritário")
    st.write("Exclusivo para profissionais e parceiros do edifício.")
    
    with st.form("solicitacao_form"):
        nome = st.text_input("Seu Nome Completo")
        celular = st.text_input("WhatsApp para Contato (com DDD)")
        metodo = st.selectbox("Como prefere ser contatado?", ["WhatsApp", "Ligação Telefônica", "E-mail"])
        
        data_pref = st.date_input("Data de Preferência", min_value=datetime.today())
        periodo = st.radio("Período de Preferência", ["Manhã", "Tarde", "O mais breve possível"])
        
        # Captura indicação automática via link (parâmetro 'ref') ou manual
        ref_id = st.query_params.get("ref", "")
        indicacao = st.text_input("Indicado por (Nome ou Sala)", value=ref_id)
        
        submit = st.form_submit_button("Enviar Solicitação VIP")

    if submit:
        if nome and celular:
            try:
                # Organizando os dados para a Aba 1 da Planilha
                nova_linha = pd.DataFrame([{
                    "Data": str(data_pref),
                    "Preferência": periodo,
                    "Paciente": nome,
                    "Contato": celular,
                    "Canal": metodo,
                    "Indicação": indicacao,
                    "Status": "🚨 NOVO PEDIDO"
                }])
                
                # Enviando para a aba 'Solicitacoes'
                conn.create(worksheet="Solicitacoes", data=nova_linha)
                
                st.success(f"Solicitação enviada! Nossa equipe falará com você via {metodo} em breve.")
                st.balloons()
            except Exception as e:
                st.error(f"Erro ao salvar na planilha: {e}")
        else:
            st.error("Por favor, preencha seu nome e celular para contato.")

with tab2:
    st.markdown("### Seu Link de Indicação")
    st.write("Gere seu link exclusivo e compartilhe com colegas do prédio para acumular bônus.")
    
    nome_ref = st.text_input("Digite seu nome para gerar o link:")
    if nome_ref:
        # Pega a URL atual do app automaticamente
        app_url = "https://meu-app-oftalmo.streamlit.app" # Substitua pelo seu link real se souber
        link_personalizado = f"{app_url}/?ref={nome_ref.replace(' ', '%20')}"
        
        st.info("Copie o link abaixo e envie para seus amigos no WhatsApp:")
        st.code(link_personalizado, language=None)
        
        st.markdown("""
        **Premiações do Clube de Vantagens:**
        - **Saúde (Convênio):** 10 indicações convertidas = 1 Sessão Eye-Spa.
        - **Cirurgia Particular:** R$ 200,00 de bônus em procedimentos.
        - **Estética:** 5% de bônus por indicação (Cumulativo).
        
        *⚠️ Trava de Segurança: Os bônus acumulados respeitam o limite de custo operacional dos procedimentos.*
        """)

st.sidebar.markdown("---")
st.sidebar.info("Este canal é monitorado em tempo real para garantir sua prioridade no edifício.")
