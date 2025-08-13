import streamlit as st

st.set_page_config(
    page_title='Erin De Pree | portfolio',
    page_icon=':notebook:'
)
st.title('Erin De Pree, Ph.D. | Data Scientist')

st.markdown(':email: erindepree@gmail.com | [in/edepree](http://linkedin.com/in/edepree)')
st.markdown('_Greater DC/Baltimore metropolitian areas, willing to move_')

st.markdown('''
            I am a data scientist and experienced problem solver looking to improve the world by providing 
            accurate data to aid in constructing long-term solutions. I use my experience as a physics college 
            professor to mentor others, understand and negotiate with stakeholders with different backgrounds 
            and priorities, and experience researching best practices to empower employee contributions to 
            long-term solutions.
    ''')

# st.image('./images/erindepree.jpeg', width= 200)


st.header('Skills')
st.markdown('''
            * Python (pandas, numpy, matplotlib, seaborn, sklearn, streamlit, keras, etc)
            * Mathematica (modules, dynamic modules, plots (2D, 3D, vectors, contour, etc), animations)
            * SQL (SQlite and TAP)
            * GoogleCloud
            * VizieR
            * LaTeX (including TikZ, developed style and class files, BibTeX)
            ''')


st.header('Projects') # add a link

st.subheader('FelineMetrics | GitHub')
st.markdown('''
            _Tools Used:_ python, pandas, numpy, plotly.express, Dash, jupyter notebook, etc
''')

st.subheader('Regional Affiliations | [GitHub](https://github.com/erindepree/world-regions)')
st.markdown('''
            _Tools Used:_ python, etc
''')

st.subheader('Astrometry of Double Stars')
st.markdown('''
            _Tools Used:_ ADQL with TAP protocol on [VizieR](https://tapvizier.cds.unistra.fr/adql/), 
            Google Sheets, Mathematica
''')

st.subheader('Physics Majors Database')
st.markdown('''
_Tools Used:_ Google XXXX, Google Sheets (including searching the database, aggregating results, 
            plotting majors per year with a 5 year running average, and pivot tables)
''')

st.subheader('Title')
st.markdown('''
            _Tools Used:_ python, etc
''')


st.header('Experience')
st.markdown('''
            ##### Data Science Fellow | General Assembly | 2025
            * highlight
            * highlight

            ##### Visiting Associate Professor of Physics | Bates College | 2022 - 2025
            * highlight
            * highlight
        
            ##### Associate Professor of Physics | St. Mary's College of Maryland | 2008 - 2022
            * highlight
            * highlight
''')

st.header('Education')
st.markdown('''
            ##### Data Science Bootcamp | General Assembly | 2025

            ##### Ph.D., physics | The College of William & Mary | 2008

            ##### M.S., physics | The College of William & Mary | 2004

            ##### B.S., physics and math majors | Hillsdale College | 2003
''')