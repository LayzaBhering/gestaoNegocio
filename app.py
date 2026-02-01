import streamlit as st
import pandas as pd
from datetime import date
import os

st.set_page_config(layout="wide")

st.markdown("# Insira os dados")

df = pd.DataFrame(
    [
        {
        "Categoria": "",
        "Produto": "", 
         "Un. Medida": "UN",
         "Vendedor": "",
         "Turno": "",
         "Quantidade": 0, 
         "Vlr. Unitário": 0.00,
         "Data Venda": date.today()
        }
    ]
)

#Realizei as configurações das colunas da tabela
tabela = st.data_editor(
    df, num_rows="dynamic",use_container_width=True,
    column_config={
        "Vlr. Unitário": st.column_config.NumberColumn(
            "Vlr. Unitário *",
            help="Preço unitário em reais",
            format="R$ %.2f"
        ),
        "Quantidade": st.column_config.NumberColumn(
            "Quantidade *",
            min_value= 0,
            step=1
        ),
        "Data Venda": st.column_config.DateColumn(
            "Data Venda *",
            format="DD/MM/YYYY"
        ),
        "Un. Medida": st.column_config.SelectboxColumn(
            "Un. Medida",
            help="Selecione a unidade de medida",
            width="medium",
            options=[
                "UN", "KG", "LT", "ML", "CX", "PCT"
            ],
            required=True
        ),
        "Categoria": st.column_config.SelectboxColumn(
            "Categoria *",
            help="Selecione a categoria",
            width="medium",
            options=[
                "Salgado",
                "Bebida Alcoólica",
                "Bebida",
                "Bolo / Doce",
                "Salada",
                "Carne",
                "Porção",
                "Adicional",
                "Hámburguer",
                "Pizza",
                "Molhos"
            ]
        ),
        "Turno": st.column_config.SelectboxColumn(
            "Turno *",
            help="Selecione o turno",
            width="medium",
            options=[
                "Matutino",
                "Vespertino",
                "Noturno"
            ]
        )
    }
)

#Configuração do botão de enviar dados adicionados na tabela. Em seeguida, o usuário é direcionado para a página data.py
if st.button("Enviar", type="primary"):
    bancoDadosTratado = tabela.dropna(subset=["Produto","Quantidade", "Categoria", "Data Venda", "Vlr. Unitário", "Turno"])
    bancoDados = bancoDadosTratado[
        (bancoDadosTratado["Produto"] != "") & 
        (bancoDadosTratado["Quantidade"] != "") &
        (bancoDadosTratado["Categoria"] != "") &
        (bancoDadosTratado["Data Venda"] != "") &
        (bancoDadosTratado["Vlr. Unitário"] != "") &
        (bancoDadosTratado["Turno"] !="")
    ]
    
    if not bancoDados.empty:
        arquivo = "data.csv"
        precisa_cabecalho = not os.path.exists(arquivo) or os.path.getsize(arquivo) == 0
        bancoDados.to_csv(
            arquivo, 
            mode='a', 
            index=False, 
            header=precisa_cabecalho, 
            encoding='utf-8'
        )
        
        st.success("Dados registrados com sucesso!")
        st.switch_page("pages/data.py")
    else:
        st.error("Erro: A tabela está vazia ou um dos campos obrigatórios não foram preenchidos.")

#Mostro na tela do usuário quantas linhas ele adicionou
registrosTabela = len(tabela)
st.write(f"Há {registrosTabela} registros.")