import streamlit as st
import plotly.express as px
import pandas as pd


def hostel():
    st.subheader("Hostel Temperature")
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
    st.subheader("Hostel Temperature vs Time Pie-Chart")
    st.text("\n")
    st.text("\n")
    Pie_chart = px.pie(df,
                       values='B_Hostel_Temperature',
                       names='Time')
    st.plotly_chart(Pie_chart)
    st.text("\n")
    st.text("\n")

    st.subheader("Bar Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.markdown("The data presented below shows the report of Hostel Temperature in the form of Bar-chart.")
    st.text("\n")
    st.text("\n")
    st.subheader("Hostel Temperature vs Time Bar Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # making dictionary of the graph and using list as their values
    hostel_temperature = df['B_Hostel_Temperature']
    time = df['Time']

    fig = px.bar(df,
                 x=time,
                 y=hostel_temperature,
                 )

    st.plotly_chart(fig)
