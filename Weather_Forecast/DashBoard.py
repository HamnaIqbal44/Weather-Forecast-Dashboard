import streamlit as st
import Charts as ch
import sensor as sen


def dashboard():
    st.subheader("Dashboard")
    st.text("\n")
    st.text("\n")
    st.error("Important Note")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.markdown("Hello Users!!\nThis dashboard only show you the temperature of four areas of **PAK-AUSTRIA "
                "FACHHOCHSCHULE (Institute of applied sciences and technology)**. Their pie-charts and their "
                "bar-charts.\n "
                )
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    col1, col2 = st.columns(2)

    with col1:
        st.success("STC")
        st.success("SPCAI")

    with col2:
        st.success("Hostel")
        st.success("A2 Block")

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    ch.pie_chart()
    ch.bar_chart()

