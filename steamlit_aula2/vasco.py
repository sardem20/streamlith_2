import streamlit as st
import pandas as pd

#DAVI SENA É FARMADOR DE AURA DE ÔNIBUS
st.title("Painel Operacional - Expresso Mobilidade")
st.subheader("Sistema de Gestão de Frotas e Itinerários")
st.markdown("---")

nome = st.text_input("Digite seu nome de operador:")
if nome:
    st.success(f"Bem-vindo(a) ao sistema, **{nome}**!")
else:
    st.info("Por favor, digite seu nome para iniciar a sessão.")

st.markdown("---")

st.header("Consulta de Rota Prioritária")
linha_selecionada = st.selectbox(
    "Escolha uma linha para verificar detalhes:",
    ["510", "520", "550", "620"]
)
st.write(f"**Linha selecionada para monitoramento:** {linha_selecionada}")


st.header("Relatórios Consolidados")
linhas_multiselect = st.multiselect(
    "Escolha as linhas para gerar o relatório de passageiros:",
    ["510", "520", "550", "620"],
    default=["510", "520"]
)

dados_operacionais = pd.DataFrame({
    'Linhas': ["510", "520", "550", "620"],
    'Motoristas': ["Carlos Silva", "Ana Souza", "João Pereira", "Maria Santos"],
    'Demanda Média (Passageiros)': [1200, 950, 1500, 800],
    'Status': ["Em Operação", "Em Operação", "Atrasada", "Garagem"]
})

if linhas_multiselect:
    st.subheader("Dados das Linhas Selecionadas")
    df_filtrado = dados_operacionais[dados_operacionais['Linhas'].isin(linhas_multiselect)]
    st.dataframe(df_filtrado)
else:
    st.warning("Selecione ao menos uma linha acima para visualizar os dados.")

st.markdown("---")

st.header("Operações de Frota")
if st.button("Calcular Demanda e Distribuição"):
    st.write("Calculando demanda e alocação de frota em tempo real...")
    st.success("Cálculo concluído com sucesso!")