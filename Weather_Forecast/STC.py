import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd


def STC():
    st.subheader("STC Temperature")
    st.text("\n")
    st.text("\n")
    st.subheader("Pie Chart")
    st.text("\n")
    st.text("\n")
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
    st.subheader("STC Temperature vs Time Pie-Chart")
    st.text("\n")
    st.text("\n")

    Pie_chart = px.pie(df,
                       values='STC_Temperature',
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
    st.subheader("Temperature vs Time Bar-Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # making dictionary of the graph and using list as their values
    STC_temperature = df['STC_Temperature']
    time = df['Time']

    fig2 = px.bar(df,
                  x=time,
                  y=STC_temperature,
                  )

    st.plotly_chart(fig2)
