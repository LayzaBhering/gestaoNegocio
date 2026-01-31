import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("📊 Banco de Dados")

arquivo = "data.csv"

# Verificamos se o arquivo existe e se não está vazio
if os.path.exists(arquivo) and os.path.getsize(arquivo) > 0:
    try:
        df = pd.read_csv(arquivo)
        if "Data Venda" in df.columns:
            df["Data Venda"] = pd.to_datetime(df["Data Venda"])

        df["Faturamento"] = df["Vlr. Unitário"] * df["Quantidade"]

        st.write("### Registros Históricos")

        st.dataframe(
            df, 
            use_container_width=True, 
            hide_index=True,
            column_config={
                "Vlr. Unitário": st.column_config.NumberColumn(
                    "Vlr. Unitário",
                    help="Preço unitário em reais",
                    format="R$ %.2f"
                ),
                "Quantidade": st.column_config.NumberColumn(
                    "Quantidade",
                    help="Quantidade vendida",
                    min_value=0,
                    step=1
                ),
                "Data Venda": st.column_config.DateColumn(
                    "Data Venda",
                    format="DD/MM/YYYY"
                ),
                "Faturamento": st.column_config.NumberColumn(
                    "Faturamento",
                    help="Total da linha (Qtd x Vlr)",
                    format="R$ %.2f"
                )
            }
        )
        
        faturamento_total = df["Faturamento"].sum()
        st.metric("Faturamento Total", f"R$ {faturamento_total:,.2f}")
            
    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
else:
    st.warning("O banco de dados está vazio ou ainda não foi criado.")
    st.info("Vá até a página inicial para registrar sua primeira venda.")

