import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import time as time
import random

excel_file = 'Olympic_Athletes.xlsx'
sheet_name = 'Sheet1'
#
df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='A:J', header=0)

# x = df['Athlete']
# y = df['Gold']
# plt.bar(x, y)
# plt.show()
#
#
# def bar_chart():
#     st.subheader("Bar Chart")
#     st.text("\n")
#     st.text("\n")
#     st.text("\n")
#     st.text("\n")
#     st.markdown("The data presented below shows the combine results of the temperatures of these 4 areas.")
#     st.text("\n")
#     st.text("\n")
#     st.subheader("Temperature vs Area Bar Chart")
#     st.text("\n")
#     st.text("\n")
#     st.text("\n")
#     st.text("\n")
#
#
#     athlete = df['Athlete']
#     gold = df['Gold']
#
#     fig = px.bar(df,
#                  x=athlete,
#                  y=gold,
#                  )
#
#     st.plotly_chart(fig)

# csv_file = 'sensor_data.csv'

# df0 = pd.read_csv(csv_file, header=0)

st.dataframe(df)

placeholder = st.empty()

# def chart():
A2_temperature = df['Gold'] * random.randrange(0, 22)
athlete = df['Athlete']

fig3 = px.bar(df,
              x=athlete,
              y=A2_temperature,
              )

placeholder.write(fig3)


# df[“fitness_new”] = df[“fitness”] * np.random.choice (range (1,5))


