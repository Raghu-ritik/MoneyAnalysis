import streamlit as st
import data_processor as DP
import data_cleaning as DC

# ------------------***                Analyzing Data                                ***------------------
st.markdown("### Cleaning Data")

# Read
if st.session_state:
    dataframe = st.session_state['dataframe']
    st.dataframe(st.session_state['dataframe'])
    currentDefaultValues = []
    currentDefaultValues = ['id','Opportunity_Origin__c', 'DNB_Scoring_Rate__c', 'Current_Balance__c', 'Opp_number__C', 'DP_Budget_Management_Services__c',
                'DP_Monthly_rent_amount_236__c', 'Income_source_is_a_government_benefit__c', 'DP_Primary_income_last_pay_date__c',
                'Primary_regular_benefit_last_pay_date__c', 'Multiple_Lenders_Hardship__c', 'DP_Monthly_rent_amount_236__c',  
                'DP_Monthly_rent_amount_236__c', 'loan_dishonours__c', 'Primary_regular_benefit_monthly_amount__c', 
                'Courts_and_Fines_transactions__c', 'DP_Total_Monthly_Benefit_Income__c', 'Hardship_Indicator_Gambling__c', 
                'SACC_commitments_due_next_month__c', 'Deposits_since_last_SACC_dishonour__c', 'Total_monthly_credits__c',
                'Collection_agency_transactions__c', 'Average_monthly_amount_of_Courts_and_Fin__c', 'Courts_and_Fines_providers__c', 
                'Deposits_since_last_dishonour__c', 'Bank_Report_Gov_Benefit__c', 'Last_pay_date_for_largest_inc_src_302__c', 
                'Next_pay_date_for_largest_income_source__c']
    if not set(currentDefaultValues).intersection(set(dataframe.columns)):
        st.warning("some columns are already been droped in the last rerun!"    )        
        currentDefaultValues = []
    
    option = st.multiselect(
        "Select Features to Drop",
        options=dataframe.columns,
        default=currentDefaultValues,
        placeholder="Select Columns..."
    )
    # st.write(type(option))
    dataframe = DC.DropColumns(dataframe,option)

    st.write(dataframe)
    st.markdown("Count of unique values of Features")
    DC.NUniqueValues(dataframe)
    st.markdown("Summary Description of Features")
    DC.DescribingData(dataframe)
    st.markdown("Features having the Null Values with their null value percentage")
    DC.featuresWithNA(dataframe)
    dataframe = DC.DataCleaning(dataframe)
    st.markdown("Features having the Null Values with their null value percentage")
    DC.featuresWithNA(dataframe)
    # # ------------------***     Classifying Target Feature into RED,GREEN,Orange       ***------------------
    # ClassifyingTargetFeature(dataframe,"StageName")
    # # ------------------***                                                            ***------------------    
    # # ------------------*** Target Class Drop Because Some of Them may be irrevelent  ***------------------
    # target_categories = st.multiselect(
    #     "Select target to Drop",
    #     options=dataframe['StageName'].unique(),
    #     default=[],
    #     placeholder="Select Columns..."
    # )
    # DropTargetCategories(dataframe,"StageName",target_categories)
    # st.write(dataframe)
    # # ------------------***                                                            ***------------------
    # # ------------------***                   Encoding the Features                    ***------------------    
    # option_label_encoding = st.multiselect(
    #     "Select Columns to apply Label Encoding",
    #     options=dataframe.columns,
    #     default=[],
    #     placeholder="Select Columns..."
    # )
    # dataframe = EncodingOfFeatures(dataframe,option_label_encoding)
    # st.dataframe(dataframe)
    # # ------------------***                                                             ***------------------
    # # ------------------***        Showing the count of value in FeatureColumns         ***------------------
    # st.markdown("###### Printing the count of each of 3 classes RED, GREEN, Orange to verify its inputation and Class counts.")
    # option_feature_Column_value_count = st.selectbox(
    #     "Select Columns to view Value Counts",
    #     options=dataframe.columns,
    #     placeholder="Select Feature Column "
    # )
    # st.dataframe(ValueCountOfFeatures(dataframe,option_feature_Column_value_count),width=900)
    # # ------------------***                                                             ***------------------
    # st.markdown("###### Printing the Numerical Features.")
    # st.dataframe(NumericalFeatures(dataframe),width=900)   
    # st.markdown("###### Printing the Discrete Features.")
    # discrete_features = DiscreteFeatures(dataframe)
    # st.dataframe(discrete_features,width=900)   



    # Initialization
    if 'dataframe' in st.session_state:
        del st.session_state['dataframe']
        st.session_state['dataframe'] = dataframe