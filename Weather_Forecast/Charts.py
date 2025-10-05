import streamlit as st
import pandas as pd
import plotly.express as px
import sensor as sen


def pie_chart():
    st.subheader("Pie Chart")
    st.text("\n")
    st.text("\n")
    csv_file = 'sensor_data.csv'

    df0 = pd.read_csv(csv_file, header=0)

    st.dataframe(df0)

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.markdown("The data presented below shows the combine results of the temperatures of these 4 areas.")
    st.text("\n")
    st.text("\n")
    st.subheader("STC Temperature vs Time Pie-Chart")
    st.text("\n")
    st.text("\n")

    STC_Pie_chart = px.pie(df0,
                           values='STC_Temperature',
                           names='Time')

    A2_Pie_chart = px.pie(df0,
                          values='A2_Temperature',
                          names='Time')

    SPCAI_Pie_chart = px.pie(df0,
                             values='SPCAI_Temperature',
                             names='Time')

    Hostel_Pie_chart = px.pie(df0,
                              values='B_Hostel_Temperature',
                              names='Time')

    st.plotly_chart(STC_Pie_chart)

    st.subheader("A2 Block Temperature vs Time Pie-Chart")
    st.text("\n")
    st.text("\n")
    st.plotly_chart(A2_Pie_chart)

    st.subheader("SPCAI Temperature vs Time Pie-Chart")
    st.text("\n")
    st.text("\n")
    st.plotly_chart(SPCAI_Pie_chart)

    st.subheader("Hostel Temperature vs Time Pie-Chart")
    st.text("\n")
    st.text("\n")
    st.plotly_chart(Hostel_Pie_chart)

    st.text("\n")
    st.text("\n")


def bar_chart():
    csv_file = 'sensor_data.csv'
    st.subheader("Bar Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.markdown("The data presented below shows the combine results of the temperatures of these 4 areas.")
    st.text("\n")
    st.text("\n")
    st.subheader("Temperature vs Hostel Bar-Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    df = pd.read_csv(csv_file, header=0)

    hostel_temperature = df['B_Hostel_Temperature']
    time = df['Time']

    fig = px.bar(df,
                 x=time,
                 y=hostel_temperature,
                 )

    st.plotly_chart(fig)

    st.subheader("Temperature vs SPCAI Bar-Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    SPCAI_temperature = df['SPCAI_Temperature']
    time = df['Time']

    fig1 = px.bar(df,
                  x=time,
                  y=SPCAI_temperature,
                  )

    st.plotly_chart(fig1)

    st.subheader("Temperature vs STC Bar-Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    STC_temperature = df['STC_Temperature']
    time = df['Time']

    fig2 = px.bar(df,
                  x=time,
                  y=STC_temperature,
                  )

    st.plotly_chart(fig2)

    st.subheader("Temperature vs A2_Block Bar-Chart")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    A2_temperature = df['A2_Temperature']
    time = df['Time']

    fig3 = px.bar(df,
                  x=time ,
                  y=A2_temperature,
                  )

    st.plotly_chart(fig3)
