import streamlit as st
import plotly.express as px
import pandas as pd


def A2_block():
    st.subheader("A2 Block Temperature")
    st.text("\n")
    st.text("\n")
    st.subheader("Pie Chart")
    st.text("\n")
    st.text("\n")
    # reading the Excel file
    csv_file = 'sensor_data.csv'
    df = pd.read_csv(csv_file, header=0)
    st.dataframe(df)

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.markdown("The data presented below shows the report of STC Temperature in the form of Pie Chart.")
    st.text("\n")
    st.text("\n")
    st.subheader("A2 Temperature vs Days Pie-Chart")
    st.text("\n")
    st.text("\n")
    Pie_chart = px.pie(df,
                       values='A2_Temperature',
                       names='Time')
    st.plotly_chart(Pie_chart)
    st.text("\n")
    st.text("\n")

    st.subheader("Bar Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.markdown("The data presented below shows the report of STC Temperature in the form of Bar chart.")
    st.text("\n")
    st.text("\n")
    st.subheader("Temperature vs Days Bar Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    A2_temperature = df['A2_Temperature']
    time = df['Time']

    fig3 = px.bar(df,
                  x=time,
                  y=A2_temperature,
                  )

    st.plotly_chart(fig3)
