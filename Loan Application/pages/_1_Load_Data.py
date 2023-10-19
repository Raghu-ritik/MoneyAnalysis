import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def DropColumns(Dataframe,columns):
    Dataframe.drop(columns, inplace = True, axis = 1)
    return Dataframe


def NUniqueValues(Dataframe):
    st.dataframe(dataframe.nunique(),width=1000)
    

def DataCleaning(Dataframe):
    # Imputation of values 
    Dataframe.dropna(axis=0,inplace=True)
    return Dataframe

def DescribingData(Dataframe):
    st.dataframe(Dataframe.describe())

def featuresWithNA(Dataframe):
    ## Here we will check the percentage of NUll values present in each feature
    ## 1 -step make the list of features which has missing values
    features_with_na=[features for features in Dataframe.columns if Dataframe[features].isnull().sum()>1]
    if len(features_with_na)<1:
        st.write("There were no features with Null values")

    ## 2- step print the feature name and the percentage of missing values
    FeatureNA = {}
    for feature in features_with_na:
        FeatureNA[feature] = f"{np.round(Dataframe[feature].isnull().mean(), 4)} % missing Values"
    st.dataframe(FeatureNA, width=1000)

def ClassifyingTargetFeature(Dataframe,TargetColumn):
    Dataframe[TargetColumn] = Dataframe[TargetColumn].replace(['Closed Lost','Bad Debt Written Off','Bad Debt Pending', 'Bad Debt Watch'], 'Red')
    Dataframe[TargetColumn] = Dataframe[TargetColumn].replace(['Loan Paid'], 'Green')
    Dataframe[TargetColumn] = Dataframe[TargetColumn].replace(['Debt Management', 'Payment Plan',
                                            'Closed Won-Payment Failed', 'Closed Won-Funded'], 'Orange')
    return Dataframe

def DropTargetCategories(Dataframe,TargetColumn,TargetCategories):
    for target_category in TargetCategories:
        Dataframe.drop(Dataframe.index[(Dataframe[TargetColumn] == target_category)],axis=0,inplace=True)
    return Dataframe

def EncodingOfFeatures(Dataframe,TargetColumns):
    # Applying Label encoding on Categorical columns 
    label_encoder = LabelEncoder()
    for target_column in TargetColumns:
        Dataframe[target_column]= label_encoder.fit_transform(dataframe[target_column])
    return Dataframe

def ValueCountOfFeatures(DataFrame,FeatureColumn="StageName"):
    return DataFrame[FeatureColumn].value_counts()

def DiscreteFeatures(DataFrame):
    #Lets classify the features into discrete variables
    return [feature for feature in NumericalFeatures(DataFrame) if len(DataFrame[feature].unique())<10 and len(DataFrame[feature].unique())>0]


def NumericalFeatures(DataFrame):
    #Lets classify the features into continuous variables
    # list of numerical variables
    return [feature for feature in DataFrame.columns if DataFrame[feature].dtypes != 'O']


def uploadDataUsingFile(uploadDatasetOption):
    uploaded_file =  st.file_uploader("Upload a File!")
    if uploaded_file is not None:
        if uploaded_file.type == "text/csv":
            return pd.read_csv(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            return pd.read_excel(uploaded_file)
        elif uploaded_file.type == "application/json":
            return pd.read_json(uploaded_file)
    elif uploaded_file is not None:
        return "The file is not valid file please check the file else change the File file type !!"
        # st.warning()

uploadDatasetOption = st.selectbox("Selection option to Upload Dataset",
             ["DataBase connection","File Upload"],
             placeholder="Select a upload method")

if uploadDatasetOption == "DataBase connection":
    st.text_input("Database API Key ")
    st.text_input("Database API Key Password  ")
    st.text_input("Database API Source  ")

elif uploadDatasetOption == "File Upload":
 
    dataframe = uploadDataUsingFile(uploadDatasetOption)
    if dataframe is not None:
        st.dataframe(dataframe)
        # Initialization
        if 'dataframe' in st.session_state:
            del st.session_state['dataframe']
        st.session_state['dataframe'] = dataframe

        
        # currentDefaultValues = ['id','Opportunity_Origin__c', 'DNB_Scoring_Rate__c', 'Current_Balance__c', 'Opp_number__C', 'DP_Budget_Management_Services__c',
        #     'DP_Monthly_rent_amount_236__c', 'Income_source_is_a_government_benefit__c', 'DP_Primary_income_last_pay_date__c',
        #     'Primary_regular_benefit_last_pay_date__c', 'Multiple_Lenders_Hardship__c', 'DP_Monthly_rent_amount_236__c',  
        #     'DP_Monthly_rent_amount_236__c', 'loan_dishonours__c', 'Primary_regular_benefit_monthly_amount__c', 
        #     'Courts_and_Fines_transactions__c', 'DP_Total_Monthly_Benefit_Income__c', 'Hardship_Indicator_Gambling__c', 
        #     'SACC_commitments_due_next_month__c', 'Deposits_since_last_SACC_dishonour__c', 'Total_monthly_credits__c',
        #     'Collection_agency_transactions__c', 'Average_monthly_amount_of_Courts_and_Fin__c', 'Courts_and_Fines_providers__c', 
        #     'Deposits_since_last_dishonour__c', 'Bank_Report_Gov_Benefit__c', 'Last_pay_date_for_largest_inc_src_302__c', 
        #     'Next_pay_date_for_largest_income_source__c']
        # option = st.multiselect(
        #     "Select Features to Drop",
        #     options=dataframe.columns,
        #     default=currentDefaultValues,
        #     placeholder="Select Columns..."
        # )
        # # st.write(type(option))
        # dataframe = DropColumns(dataframe,option)
        # st.write(dataframe)
        # NUniqueValues(dataframe)
        # DescribingData(dataframe)
        # featuresWithNA(dataframe)

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

        # dataframe = DataCleaning(dataframe)



        # Initialization
        # if 'dataframe' in st.session_state:
        #     del st.session_state['dataframe']
        # st.session_state['dataframe'] = dataframe
 
        # ------------------***                Next Page of Analyzing Data                  ***------------------
        st.link_button("Start Data Cleaning","3_AnalyzingData",type="secondary")
        # ------------------***                                                             ***------------------
    # st.warning("The file is not a CSV file please check the file else change the File file type !!")
else:
    st.write("Not a proper Method to upload Dataset")




 