import streamlit as st
import numpy as np
import plotly.express as px

def Draw_Histograms(DataFrame,columns):
    for feature in columns:
        st.markdown(f"###### {feature}")
        st.subheader("",divider='rainbow')
        hist_values = np.histogram(
            DataFrame[feature], bins=8, range=(0,8))[0]
        st.bar_chart(hist_values)


# @st.experimental_memo
# def get_chart_8045850():
def DrawHeatMaps(DataFrame):
    correlation_matrix = DataFrame.corr()
    fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto")
    st.plotly_chart(fig, theme="streamlit")

    # tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])


# @st.experimental_memo
# def get_chart_72502475():
def DrawScatterPlots(DataFrame,Col1,Col2,HUE):

    fig = px.scatter(DataFrame, y=Col1 , x=Col2, color=HUE) # symbol=HUE
    fig.update_traces(marker_size=10)
    st.plotly_chart(fig, theme="streamlit")

    # df = px.data.medals_long()
    # tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    # with tab1:
    # with tab2:
    #     st.plotly_chart(fig, theme=None)