from streamlit_option_menu import option_menu
import DashBoard as dash
import Charts as ch
import Area as ar


def main_menu():
    selected = option_menu(
        menu_title="Main Menu",
        options=["Dashboard", "Pie chart", "Barchart", "Areas"],
        icons=["cast", "pie-chart", "bar-chart", "house"],
        orientation="horizontal",
        styles={
            "container": {"background-color": "grey"},
            "icon": {"color": "red", "font-size": "25px"},
            "menu": {"color": "#266c81"},
            "nav-link-selected": {"background-color": "#266c81"},
        }
    )
    if selected == 'Dashboard':
        dash.dashboard()

    elif selected == 'Pie chart':
        ch.pie_chart()
        pass

    elif selected == 'Barchart':
        ch.bar_chart()

    elif selected == 'Areas':
        ar.area()

    else:
        pass

