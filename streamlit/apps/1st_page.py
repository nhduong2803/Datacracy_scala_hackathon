from re import T
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import pickle
from sklearn.preprocessing import OrdinalEncoder
encoder=OrdinalEncoder()
from PIL import Image
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report

st.set_page_config(layout="wide")
# Load data

# Def Visualization

# Text describe

def main():
    
    st.title("Team 03")
    st.text("SCALA - HACKATHON")

    #Introduce team members


    #Title list
    h1=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">PROJECT OVERVIEW </h2>
    </div>
    """
    h2=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">DATA OVERVIEW </h2>
    </div>
    """
    h3=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">RESULT OVERVIEW </h2>
    </div>
    """
    
    # PROJECT OVERVIEW INFORMATION
    st.markdown(h1,unsafe_allow_html=True)
    st.markdown(overview_1, True)
    col1, col2, col3 = st.beta_columns((1,3,1))
    col2.image('image/analysis_flow.png')
    st.markdown(overview_2, True)


if __name__=='__main__':
    Res=main()
    # Res=str(int(result))
    # dict={"yes":'1',"no":'0'}    
    # for i,j in dict.items():
    #     Res=Res.replace(j,i)
    
            
    if st.sidebar.button("Show Prediction"):
        st.sidebar.subheader("The predicted response of customer or client to subscribe a term deposit is")
        st.sidebar.success(Res)
    
    
    if st.button("Thanks") :
        st.text("Thank you for visiting  and happy learning :)")
        st.balloons()