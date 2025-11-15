import streamlit as st
import pandas as pd
st.set_page_config(page_title='Business Automation dashboard')
st.title('Business Automation Dashboard')
df = pd.read_csv('data/sample_sales.csv')
st.metric('Total ventas', f"${df['amount'].sum():,.2f}")
st.line_chart(df.groupby('date')['amount'].sum())
if st.button('Exportar reporte'):
    df.to_excel('reporte.xlsx', index=False)
    st.success('Reporte generado: reporte.xlsx')
