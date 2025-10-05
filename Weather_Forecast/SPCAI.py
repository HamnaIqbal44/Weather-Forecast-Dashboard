import streamlit as st
import plotly.express as px
import pandas as pd


def Spcai():
    st.subheader("SPCAI Temperature")
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
    st.subheader("SPCAI Temperature vs Time Pie-Chart")
    st.text("\n")
    st.text("\n")
    Pie_chart = px.pie(df,
                       values='SPCAI_Temperature',
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
    st.subheader("SPCAI Temperature vs Time Bar Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # making dictionary of the graph and using list as their values
    SPCAI_temperature = df['SPCAI_Temperature']
    time = df['Time']

    fig1 = px.bar(df,
                  x=time,
                  y=SPCAI_temperature,
                  )

    st.plotly_chart(fig1)
