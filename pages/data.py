import streamlit as st
import pandas as pd
import os

def processar_dados(caminho_csv):
    if os.path.exists(caminho_csv) and os.path.getsize(caminho_csv) > 0:
        df_interno = pd.read_csv(caminho_csv)
        if "Data Venda" in df_interno.columns:
            df_interno["Data Venda"] = pd.to_datetime(df_interno["Data Venda"])
        df_interno["Faturamento"] = df_interno["Vlr. Unitário"] * df_interno["Quantidade"]
        return df_interno
    return None

st.set_page_config(layout="wide")
st.title("📊 Banco de Dados & Gestão")

arquivo = "data.csv"
df = processar_dados(arquivo)

if df is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total de Registros", len(df))
    with col2:
        st.metric("Faturamento Total", f"R$ {df['Faturamento'].sum():,.2f}")

    st.write("### Registro Histórico")
    st.info("Clique nas células para editar. Após concluir, clique no botão ' 💾 ' ao final da página.")
    df_editado = st.data_editor(
        df, 
        use_container_width=True, 
        hide_index=True,
        disabled=["Faturamento"], 
        column_config={
            "Vlr. Unitário": st.column_config.NumberColumn("Vlr. Unitário *", format="R$ %.2f"),
            "Quantidade": st.column_config.NumberColumn("Quantidade *", min_value=0, step=1),
            "Data Venda": st.column_config.DateColumn("Data Venda *", format="DD/MM/YYYY"),
            "Faturamento": st.column_config.NumberColumn("Faturamento", format="R$ %.2f")
        }
    )

    if st.button(" 💾 "):
        df_editado["Faturamento"] = df_editado["Vlr. Unitário"] * df_editado["Quantidade"]
        df_editado.to_csv(arquivo, index=False)
        
        st.success("Alterações salvas com sucesso!")
        st.rerun() 
        
else:
    st.warning("O banco de dados está vazio.")