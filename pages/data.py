import streamlit as st
import pandas as pd
import os

def processar_dados(caminho_csv):
    try:
        if os.path.exists(caminho_csv) and os.path.getsize(caminho_csv) > 0:
            df_interno = pd.read_csv(caminho_csv)
            df_interno.columns = df_interno.columns.str.strip()
            colunas_obrigatorias = ["Vlr. Unitário", "Quantidade"]
            if all(col in df_interno.columns for col in colunas_obrigatorias):
                if "Data Venda" in df_interno.columns:
                    df_interno["Data Venda"] = pd.to_datetime(df_interno["Data Venda"])
                
                df_interno["Faturamento"] = df_interno["Vlr. Unitário"] * df_interno["Quantidade"]
                return df_interno
            else:
                st.error(f"Erro no Cabeçalho! O arquivo contém: {list(df_interno.columns)}")
                return None
        return None
    except Exception:
        return None

st.set_page_config(layout="wide")
st.title("📊 Banco de Dados & Gestão")

arquivo = "data.csv"
df = processar_dados(arquivo)

if df is not None:
    col_kpi1, col_kpi2, col_filtro1, col_filtro2 = st.columns([1, 1, 1.5, 1.5])

    with col_filtro1:
        filtro_prod = st.multiselect(
            "Produto:",
            options=df["Produto"].unique() if "Produto" in df.columns else [],
            placeholder="Escolha os itens"
        )

    with col_filtro2:
        filtro_vend = st.multiselect(
            "Vendedor:",
            options=df["Vendedor"].unique() if "Vendedor" in df.columns else [],
            placeholder="Escolha os nomes"
        )

    df_exibicao = df.copy()
    if filtro_prod:
        df_exibicao = df_exibicao[df_exibicao["Produto"].isin(filtro_prod)]
    if filtro_vend:
        df_exibicao = df_exibicao[df_exibicao["Vendedor"].isin(filtro_vend)]

    with col_kpi1:
        st.metric("Total de Registros", len(df_exibicao))
    with col_kpi2:
        total_fat = df_exibicao["Faturamento"].sum()
        st.metric("Faturamento Total", f"R$ {total_fat:,.2f}")

    st.divider()

    st.write("### Registro Histórico")
    st.info("Clique na célula para editar, se necessário. Salve no botão abaixo.")
    
    df_editado = st.data_editor(
        df_exibicao, 
        use_container_width=True, 
        hide_index=True,
        disabled=["Faturamento"], 
        column_config={
            "Vlr. Unitário": st.column_config.NumberColumn("Vlr. Unitário *", format="R$ %.2f"),
            "Quantidade": st.column_config.NumberColumn("Quantidade *", min_value=0),
            "Data Venda": st.column_config.DateColumn("Data Venda *", format="DD/MM/YYYY"),
            "Faturamento": st.column_config.NumberColumn("Faturamento", format="R$ %.2f")
        }
    )

    if st.button(" 💾 "):
        df_editado["Faturamento"] = df_editado["Vlr. Unitário"] * df_editado["Quantidade"]
        df.update(df_editado)
        df.to_csv(arquivo, index=False)
        st.success("Alterações salvas!")
        st.rerun() 
        
else:
    st.warning("O banco de dados está vazio ou sem cabeçalho válido.")