import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder


def DropColumns(Dataframe,columns):
    Dataframe.drop(columns, inplace = True, axis = 1)
    return Dataframe


def NUniqueValues(Dataframe):
    st.dataframe(Dataframe.nunique(),width=1000)
    

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
        st.success("There are No Columns with NULL Values")
    else:
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
        Dataframe[target_column]= label_encoder.fit_transform(Dataframe[target_column])
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