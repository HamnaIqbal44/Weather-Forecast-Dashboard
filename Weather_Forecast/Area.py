import streamlit as st
from streamlit_option_menu import option_menu
import STC as stc
import SPCAI as spc
import Hostel as ht
import A2_Block as a2


def area():
    st.subheader("Areas")
    st.text("\n")
    st.text("\n")
    st.markdown("Select any area to know the detailed results of these areas.")
    st.text("\n")
    st.text("\n")
    # Areas = ["Home", "STC", "A2 Block", "SPCAI", "Hostel"]
    # choice = st.selectbox("Areas", Areas)
    choice = option_menu(
        menu_title="Areas",
        options=["Home", "STC", "A2 Block", "SPCAI", "Hostel"],
        menu_icon="house",
        icons=["house", "house", "house", "house", "house"],
        orientation="horizontal",
        styles={
            "container": {"background-color": "grey"},
            "icon": {"color": "red", "font-size": "25px"},
            "menu": {"color": "#266c81"},
            "nav-link-selected": {"background-color": "#266c81"},
        }
    )
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    st.markdown("Displaying the combine temperature of these 4 areas:")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    if choice == "Home":
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("STC", "70C", "1.2 C")
        col2.metric("A2 Block", "70 F", "1.2 C")
        col3.metric("SPCAI", "70 F", "1.2 C")
        col4.metric("Hostel", "70 F", "1.2 C")

    elif choice == "STC":
        stc.STC()
    elif choice == "A2 Block":
        a2.A2_block()
    elif choice == "SPCAI":
        spc.Spcai()
    elif choice == "Hostel":
        ht.hostel()
    else:
        pass
