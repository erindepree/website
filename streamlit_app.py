import streamlit as st

main_page = st.Page('./pages/home.py', title='Main Page', icon = '🏡')
page_2 = st.Page('./pages/projects.py', title='Projects', icon = '📊')

with st.sidebar: 
    st.image('./images/erindepree.jpeg', width= 200)
    st.header('Erin De Pree, Ph.D.')
    st.markdown('''
                * :email: erindepree@gmail.com
                * [in/edepree](http://linkedin.com/in/edepree)
                * [github.com/erindepree](https://github.com/erindepree)
                ''')

pg = st.navigation([main_page, page_2])

pg.run()

