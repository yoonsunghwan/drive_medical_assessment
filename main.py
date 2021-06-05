import streamlit as st
from graphs import fig,fig2,df, fig3, fig4
from datetime import date
import streamlit.components.v1 as components


st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Drive DeVilbiss Product Orders</h1>", unsafe_allow_html=True)
HtmlFile = open("Drive_Medical_data_assessment.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
with st.beta_expander("Click this to see the answers to the assessment"):
    components.html(source_code, height = 7100)

st.markdown("<p1 style='text-align: center; color: black;'>This is an interactive dashboard, feel free to hover around the graphs and play with the data. The data comes from Drive DeVilbiss Healthcare's PO Numbers data assessment.</p1>", unsafe_allow_html=True)

col1, col2 = st.beta_columns(2)
with col1.beta_container():
    col1.subheader("Plant BP02, has the greatest total value")
    col1.plotly_chart(fig)
with col2.beta_container():
    col2.subheader("Around 21.8% of PO Orders comes from A")
    col2.plotly_chart(fig2)
with col1.beta_container():
    col1.subheader("Transport/Wheelchair is the most popular category")
    col1.plotly_chart(fig3)
with col2.beta_container():
    col2.subheader("The value of ABCDS looks like a staircase moving down")
    col2.plotly_chart(fig4)




df['Average Price per Unit'] = df['Value']/df['Quantity']

with col1.beta_container():
    col1.subheader("Filter the PO data by date")
    start_date = col1.date_input('Start date', date(2021,8,1)).isoformat()
    end_date = col1.date_input('End date', date(2021,8,31)).isoformat()

    col1.dataframe(df[df['Delivery Date'].between(start_date,end_date)])


vlookup_df = df.groupby('Material').mean().drop('PO Number',axis= 1)
with col2.beta_container():
    col2.subheader('Get the average quantity, value, and price per unit for each Material')
    material = col2.multiselect("Use the multi-select tool"
                          , list(vlookup_df.index), default=['15528'])

    col2.dataframe(vlookup_df.loc[material])




