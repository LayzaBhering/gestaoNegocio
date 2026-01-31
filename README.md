# Gestão de Negócio

### Aplicação de gestão de vendas desenvolvida em:
Python e Streamlit

### Projetada para:
Registrar, gerenciar e visualizar transações comerciais de forma persistente e intuitiva. 

O sistema utiliza conceitos de Engenharia de Atributos e persistência em arquivos planos para oferecer uma experiência de Business Intelligence (BI) leve e funcional.

### Funcionalidades

### Registro de Vendas Interativo: 
Interface baseada no st.data_editor com suporte a seleção de unidades de medida (Selectbox) e validação de campos obrigatórios.

### Persistência de Dados: 
Armazenamento automático em arquivo data.csv, utilizando a lógica de append para garantir que novos registros sejam adicionados ao histórico sem apagar os anteriores.

### Engenharia de Atributos: 
Cálculo dinâmico de faturamento por linha (Quantidade * Valor Unitário) e métricas de faturamento Total.

### Gestão de Registros: 
Página dedicada para visualização histórica com capacidade de edição e exclusão de linhas diretamente pelo navegador.Análise Visual: Geração de gráficos de desempenho por vendedor e distribuição por categoria utilizando Matplotlib.