import streamlit as st

st.set_page_config(
    page_title='Erin De Pree | portfolio',
    page_icon=':bar_chart:'
)

st.title('Projects')

st.header('🐈‍⬛ Feline Metrics | GitHub')
col1, col2 = st.columns([1,3])

col1.image('./images/Mel_alert_2023.jpeg', width=150)

col2.markdown('''
            _Tools Used:_ python, pandas, numpy, plotly.express, Dash, jupyter notebook, etc.

            * Cloud-based, secure medical record for my cat, Mel
            * Creates automated reports on significant data over time (especially weight, liver and kidney values)
            * Inspired after an emergency when I couldn't find my notebook with her 14 year medical 
            history (don't worry, Mel is fine, soft tissue injury to her leg)
''')


st.header('Predicting Deaths Globally from Extreme Temperatures')
st.subheader('Group GitHub | Personal GitHub')
st.markdown('''
            _Tools Used:_ python, pandas, numpy, matplotlib, seaborn, sklearn, etc.
            * Group project using ERA5 satelite temperature data to identify extreme temperature events
            * Used the EM-DAT emergency database to model deaths as a function of extreme temperature and duration of the event
            * I served as the group leader, organized the group's GitHub repository, kept the group on track, and wrote at least half of the report
''')

st.header('Predicting Housing Prices | GitHub')
st.markdown('''
            _Tools Used:_ python, pandas, numpy, sklearn, etc

            * EDA, feature extraction
            * Multiple models
''')

st.header('🌍 Regional Affiliations | [GitHub](https://github.com/erindepree/world-regions)')
st.markdown('''
            _Tools Used:_ python, etc
''')

st.header('Astrometry of Double Stars')
st.markdown('''
            _Tools Used:_ ADQL with TAP protocol on [VizieR](https://tapvizier.cds.unistra.fr/adql/), 
            Google Sheets, Mathematica

            * description
            * link to paper with Matt
            * [paper](http://www.jdso.org/volume20/number4/DePree_503_510.pdf)
''')

st.header('Physics Majors Database')
st.markdown('''
            _Tools Used:_ Google Fusion Tables, Google Sheets (searching, aggregating, plots, pivot tables, etc)
            
            * Tracked contact information for all physics majors, minors, and alums.  
            Including awards won while a student, career tracking
            * Aggregated data to study alumni characteristics and changes over time
''')