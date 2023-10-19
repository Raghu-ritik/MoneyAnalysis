import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

import data_processor as DP
import plotter as PT
import text 

# ------------------***                Analyzing Data                                ***------------------
st.markdown("### Analyzing Data")

# Read
if st.session_state:
    dataframe = st.session_state['dataframe']
    st.dataframe(st.session_state['dataframe'])
    discrete_features = DP.DiscreteFeatures(dataframe)   
    st.markdown("The view cleaned of Dataframe ")
    st.dataframe(discrete_features)

st.subheader('Histograms for Discrete Features',help=text.HISTOGRAMS)
PT.Draw_Histograms(dataframe,discrete_features)

st.subheader('Heatmaps of Features',help=text.HEATMAPS)
PT.DrawHeatMaps(dataframe)


visualization_count = st.slider("How many Visulaization you want to make",min_value=1,max_value=5)
st.write(visualization_count)
for visuals in range(visualization_count):
    st.subheader('Scatterplots of Features',help=text.SCATTERPLOT)
    column_1 = st.selectbox("Select Column 1 ", dataframe.columns, index=visuals) #"Loan_Amount__c"
    sec_col_list = list(filter(lambda feature: (feature != column_1), dataframe.columns))  
    column_2= st.selectbox("Select Column 2 ",   sec_col_list)  #"Summary_Expenses__c"
    PT.DrawScatterPlots(dataframe,column_1,column_2 , "StageName")

     
 