from flask import Flask, render_template, request, jsonify, send_file
from io import BytesIO
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
import json
import config
import joblib



 
app = Flask(__name__)
app.static_folder = 'static'



def DropColumns(df):

    return df


def NullValues(df):
    features_with_na=[features for features in df.columns if df[features].isnull().sum()>1]
    if len(features_with_na)<1:
        return "<table><tr><td>There were no features with Null values</td></tr></table>"
    else:
        nullTable = ""
        nullTable += "<table><tr><td>The Feature with Null values and their percentages are : </td> </tr>"
        nullTable += "<tr><th> Features </th><th> Missing Values </th><tr>"
        for feature in features_with_na:
            nullTable += f"<tr><td> {feature} </td><td> {np.round(df[feature].isnull().mean(), 4)}  </td></tr>"
        nullTable += "</table>"
        return nullTable
    
def ImputingNullValues(df):
    
    return df

def LabelEncodingMethods(df,columnName):
    label_encoder = LabelEncoder()
    df[columnName]= label_encoder.fit_transform(df[columnName])
    return df

def EncodingTargetColumn(df,targetColumn):
    # Applying status from Stage Name column to Green, Orange and Red to classify the all stagenames to 3 classes.
    df[targetColumn] = df['StageName'].replace(['Closed Lost','Bad Debt Written Off','Bad Debt Pending', 'Bad Debt Watch'], 'Red')
    df[targetColumn] = df['StageName'].replace(['Loan Paid'], 'Green')
    df[targetColumn] = df['StageName'].replace(['Debt Management', 'Payment Plan', 'Closed Won-Payment Failed', 'Closed Won-Funded'], 'Orange')
    return df

def DroppingSomeUnUsedTargetRows(df,TargetFeature,UnusedTargets = ["Bank Statements Uploaded","Loan Amount Offered","Loan Offer Accepted"]):
    for Target in UnusedTargets:
        df.drop(df.index[(df[TargetFeature] == Target)],axis=0,inplace=True)
    return df
 
def show_loan_distrib(data):
    count = ""
    if isinstance(data, pd.DataFrame):
        count = data["StageName"].value_counts()
    else:
        count = data.value_counts()
    count.plot(kind = 'pie',  figsize = (4, 4), autopct = '%1.1f%%', shadow = False )
    plt.legend(["Red","GREEN","Orange"],loc=1)
    plt.show()


# @app.route('/createPlot')
def CreatePlot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    # Create a plot using Matplotlib
    plt.figure(figsize=(18, 16))
    plt.plot(x, y, marker='o')
    plt.title('Sample Plot')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')

    # Save the plot to a BytesIO object
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    plt.close()
    # Return the plot as an image to display on the web page
    return send_file(img_buf, mimetype='image/png')


@app.route('/')
def main_methods():
    DFFilePath = app.static_folder +"/"+  config.DF_FILES_PATH + "/Money_Analysis_SAAC.csv"
    # print(DFFilePath)
    df = pd.read_csv(DFFilePath)
    table = df.head().to_html(classes='table table-striped')
    try:
        df.drop(['id','Opportunity_Origin__c', 'DNB_Scoring_Rate__c', 'Current_Balance__c', 'Opp_number__C', 
            'DP_Budget_Management_Services__c','DP_Monthly_rent_amount_236__c', 'Courts_and_Fines_providers__c',
            'Income_source_is_a_government_benefit__c', 'DP_Primary_income_last_pay_date__c',
            'Primary_regular_benefit_last_pay_date__c', 'Multiple_Lenders_Hardship__c', 'DP_Monthly_rent_amount_236__c',  
            'DP_Monthly_rent_amount_236__c', 'loan_dishonours__c', 'Primary_regular_benefit_monthly_amount__c', 
            'Courts_and_Fines_transactions__c', 'DP_Total_Monthly_Benefit_Income__c', 'Hardship_Indicator_Gambling__c', 
            'SACC_commitments_due_next_month__c', 'Deposits_since_last_SACC_dishonour__c', 'Total_monthly_credits__c',
            'Collection_agency_transactions__c', 'Average_monthly_amount_of_Courts_and_Fin__c', 
            'Deposits_since_last_dishonour__c', 'Bank_Report_Gov_Benefit__c', 'Last_pay_date_for_largest_inc_src_302__c', 
            'Next_pay_date_for_largest_income_source__c'], inplace = True, axis = 1)
    except KeyError:
        print("The columns you are trying to drop had already been droped!")
    unique_counts = df.nunique()
    tableDescribe = df.describe().to_html(classes="table table-striped")
    tanleNullValues = NullValues(df)
    df = LabelEncodingMethods(df,"Applicant_Type__c")
    df = EncodingTargetColumn(df,"StageName")
    df = DroppingSomeUnUsedTargetRows(df,"StageName",["Bank Statements Uploaded","Loan Amount Offered","Loan Offer Accepted"])
    df = LabelEncodingMethods(df,"StageName")



    show_loan_distrib(df)
    return render_template('moneyAnalysis/index.html',table=table,unique_counts=unique_counts,tableDescribe=tableDescribe,tanleNullValues=tanleNullValues
                           )




 # Endpoint to create a new guide
@app.route('/api/QueryAnalysis', methods=["POST"])
def add_guide():
    title = request.json['title']
    content = request.json['content']
    loaded_model = joblib.load(f'PKL_Models/{config.PKL_MODEL_RandomForest}')
    print(loaded_model)
    dico = {
        "Title":title,
        "content":content
    }
    print("The APi Data is : ",dico)
    return dico
 

@app.route('/api/DataUpload', methods=["POST"])
def DataUpload():
    DataUploadMethod = request.json["UpoadMethod"]
    if DataUploadMethod == "DataBase":
        return "Making DB Connection"
    elif DataUploadMethod == "CSV":
        return "Uploading CSV File"
    elif DataUploadMethod == "ExcelFile":
        return "Uploading Excel File"
    elif DataUploadMethod == "JSON":
        return "Extracting Json Data"
    else :
        return "not a Valid Data Upload Method"



    return "Data Uploaded"

app.debug = True
if __name__ == '__main__':
    app.run()



