import streamlit as st
import Menu as mnu
# import sensor as sen


st.set_page_config("Weather Forecast")

# calling the navigation bar function
mnu.main_menu()


with open('main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)




