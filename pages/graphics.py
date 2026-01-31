import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")
st.title(" Análise Visual do Negócio 📈")

arquivo = "data.csv"

if os.path.exists(arquivo) and os.path.getsize(arquivo) > 0:
    df = pd.read_csv(arquivo)
    df["Faturamento"] = df["Quantidade"] * df["Vlr. Unitário"]
    st.subheader("Faturamento por Vendedor")
    vendasVendedor = df.groupby("Vendedor")["Faturamento"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    vendasVendedor.plot(kind="bar", color="skyblue", ax=ax)
    ax.set_ylabel("Faturamento (R$)")
    ax.set_xlabel("Vendedor")
    plt.xticks(rotation=45)
    
    st.pyplot(fig)

    st.divider()

    st.subheader("Vendas por Categoria")
    
    vendas_cat = df.groupby("Categoria")["Quantidade"].sum()
    
    fig2, ax2 = plt.subplots()
    ax2.pie(vendas_cat, labels=vendas_cat.index, autopct='%1.1f%%', startangle=90, colors=["#ff9999","#66b3ff","#99ff99"])
    ax2.axis('equal') 
    
    st.pyplot(fig2)

else:
    st.warning("Atenção: Sem dados para gerar gráficos. Registre as vendas no App!")