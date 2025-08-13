import streamlit as st

st.set_page_config(
    page_title='Erin De Pree | portfolio',
    page_icon=':notebook:'
)
st.title('Erin De Pree, Ph.D. | Data Scientist')

st.markdown(':email: erindepree@gmail.com | [in/edepree](http://linkedin.com/in/edepree) | [github.com/erindepree](https://github.com/erindepree)')
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
            * Deep learning (keras, pytorch, hugging faces, etc)
            * Mathematica (modules, dynamic modules, plots (2D, 3D, vector, contour, etc), animations)
            * SQL (SQlite and TAP)
            * GoogleBigQuery
            * Google Colab
            * LaTeX (including TikZ, developed style and class files, BibTeX)
            ''')


st.header('Projects') # add a link

st.subheader('FelineMetrics | GitHub')
st.markdown('''
            _Tools Used:_ python, pandas, numpy, plotly.express, Dash, jupyter notebook, etc
''')

st.subheader('Identifying Kidney Conditions | GitHub')
st.markdown('''
            _Tools Used:_ python, keras, pytorch

            Deep learning of images.  Constructed a convolution neural network with an accuracy of over 0.99 
            on validation dataset.
''')

st.subheader('Predicting Deaths from Extreme Temperatures | GitHub')
st.markdown('''
            _Tools Used:_ python, pandas, numpy, matplotlib, seaborn, sklearn, etc.
            * Group project using ERA5 satelite temperature data to identify extreme temperature events
            * Used the EM-DAT emergency database to model deaths as a function of extreme temperature and duration of the event
            * I served as the group leader, organized the group's GitHub repository, kept the group on track, and wrote about half of the report
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
            _Tools Used:_ Google Fusion Tables, Google Sheets
''')



st.header('Experience')
st.markdown('''
            ##### Data Science Fellow | General Assembly | 2025
            * 13 week, full-time program on data science, to update my software skills and switch career paths
            * Completed 5 projects (including a group project) through the entire data science lifecycle from 
            data cleaning, early data analysis, modeling, improving models, interpretations, and deployment

            ##### Visiting Associate Professor of Physics | Bates College | 2022 - 2025
            * Mentored new faculty as they adjusted to Bates
            * Maintained a welcoming a supportive environments with students
            * Taught introductory physics to upper-level elective in quantum mechanics
            
        
            ##### Associate Professor of Physics | St. Mary's College of Maryland | 2008 - 2022
            * Created a 10 part career program that helps students explore post-college options resulting in an 
            increase of student research participation from 60% to 95%.
            * Improved learning environment by developing an in-class inclusion and anti-bullying workshop, 
            dramatically increased graduation rates among underrepresented groups in physics.
            * Developed a semester-long computer programming course to solve a range of physics problems using 
            Mathematica which was self-taught

''')

st.header('Education')
st.markdown('''
            **Data Science Bootcamp** | General Assembly | 2025

            **Ph.D., physics** | The College of William & Mary | 2008

            **M.S., physics** | The College of William & Mary | 2004

            **B.S., physics and math majors** | Hillsdale College | 2003
''')