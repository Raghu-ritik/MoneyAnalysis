import streamlit as st

independent_features = []
dependent_features = None


if st.session_state:
    dataframe = st.session_state['dataframe']
    st.dataframe(st.session_state['dataframe'])

dependent_features = st.selectbox(
            "Select the Dependent Features",
            options=dataframe.columns,
            key="depenentFeatures",
            placeholder="Select Columns..."
        )

independent_features = st.multiselect(
            "Select the Independent Features",
            options=dataframe.columns,
            placeholder="Select Columns..."
        )