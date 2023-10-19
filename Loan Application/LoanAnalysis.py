import streamlit as st

from PIL import Image

im = Image.open("favicon.ico")

st.set_page_config(
    page_title="Loan Analysis",
    page_icon= im, 
)
    # initial_sidebar_state="collapsed"
st.markdown(""" <style> .eczjsme11 { display: none; } </style> """, unsafe_allow_html=True)

st.write("# Welcome to Loan Analysis! 👋")

st.markdown(
    """
    Loan analysis is to ensure that loans are made on appropriate terms to clients who can and will pay
    them back. What analysis is needed and what is the most efficient approach to fulfill that need is
    primarily determined by the type and nature of the loan.
    
    ### Objectives of Loan Analysis
    - **To place good and appropriate loans** -- can the loan generate income for repayment and will
    the client repay
    - **Determine eligibility of the applicant** -- is he/she eligible according to the the program
    criteria
    - **Training needs and skills**  -- to assess the training needs and develop the financial management
    skills level of the client. (This is the basic principal of programs that integrate their credit and
    training methodologies.)
    - **Program Indicators** -- loan analysis may also be used to generate the indicators that will be
    used to evaluate the impact of the loan.


    ### [MindRuby Technologies](https://mindruby.com/)

"""
)
st.link_button("Lets Get Started"," 1_Load_Data",type="primary")