import streamlit as st
import daten_page
import data_analyse_page
import Home_page
import data_distribution

def main():
    pages = {
        "1. Einführung": Home_page.app,
        "2. Dateneinblicke": daten_page.app, 
        "3. Geografische Verteilung": data_distribution.app,  
        "4. Datenanalyse": data_analyse_page.app
    }

    st.sidebar.title("Navigation")
    if "enable_month" not in st.session_state:
        st.session_state.enable_month = False
    # Set default page to "1. Home"
    page = st.sidebar.radio("Seiten auswählen", list(pages.keys()), index=0)
    if page == "4. Datenanalyse":
        dropdown_options_year =  [None] + list(range(2018,2024))
        dropdown_options_month =  [None] + list(range(1,13))
        if dropdown_options_year:
        
            year = st.sidebar.selectbox("Jahr:", dropdown_options_year, format_func=lambda x: x if x is not None else "Ein Jahr auswählen" , index = 0, key='year')
            if year is not None and year != st.session_state.year and 'year' in st.session_state:
                st.session_state.year = year
            st.sidebar.write(f"Ausgewählt Jahr: {year}")
            if year is None: 
                st.session_state.enable_month = False
            else:
                st.session_state.enable_month = True
            
        if dropdown_options_month:
            month = st.sidebar.selectbox("Monat:", dropdown_options_month, format_func=lambda x: x if x is not None else "Ein Monat auswählen",index = 0 ,key='month',disabled=not st.session_state.enable_month)
            if month is not None and month != st.session_state.month and 'month' in st.session_state:
                st.session_state.month = month
            st.sidebar.write(f"Ausgewählt Monat: {month}")

    pages[page]()  # Call the appropriate page function

if __name__ == "__main__":
    main()
