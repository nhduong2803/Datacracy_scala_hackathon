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
import SessionState


st.set_page_config(layout="wide")
# Load data

# Def Visualization

# Text describe

def main():
    
    st.title("SCALA - HACKATHON - Team 03")

    #Introduce team members
    member = """
<p style="line-height: 0.15;"><br></p>
<p style="line-height: 0.15;">Nh&oacute;m gồm 5 th&agrave;nh vi&ecirc;n:</p>
<ul>
    <li style="line-height: 1.5;">Dương Thị Như Hải</li>
    <li style="line-height: 1.5;">L&ecirc; Thu Thảo</li>
    <li style="line-height: 1.5;">Nguyễn Trần Qu&acirc;n</li>
    <li style="line-height: 1.5;">Vũ Thị Bảo Ngọc</li>
    <li style="line-height: 1.5;">Đới Thị Hồng</li>
</ul>
    """

    overview = """
    <p style="line-height: 0.15;"><br></p>
<p>
    <style type="text/css">
        <!--td {border: 1px solid #ccc;}br {mso-data-placement:same-cell;}
        -->
    </style><span data-sheets-hyperlinkruns='{"1":103,"2":"https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit"}{"1":187}' data-sheets-textstyleruns='{"1":0}{"1":103,"2":{"2":{"1":2,"2":1136076},"9":1}}' data-sheets-userformat='{"2":1049089,"3":{"1":0},"12":0,"23":1}' data-sheets-value='{"1":2,"2":"Voizfm là nền tảng nghe Sách nói và Podcast chất lượng cao, 100% Bản quyền lớn nhất Việt Nam.\nYêu cầu: https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit"}' style="font-size:12pt;font-family:Calibri,Arial;font-style:normal;"><span style="font-size:12pt;font-family:Calibri,Arial;font-style:normal;">Voizfm l&agrave; nền tảng nghe S&aacute;ch n&oacute;i v&agrave; Podcast chất lượng cao, 100% Bản quyền lớn nhất Việt Nam.<br>Y&ecirc;u cầu:&nbsp;</span><span style="font-size:12pt;font-family:Calibri,Arial;font-style:normal;text-decoration:underline;-webkit-text-decoration-skip:none;text-decoration-skip-ink:none;color:#1155cc;"><a class="in-cell-link" href="https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit" target="_blank">https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit</a></span></span>
</p>
    """

    #Title list
    h1=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">CASE STUDY</h2>
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

    #streamlit def
    widget_values = {}
    def make_recording_widget(f):
        def wrapper(label, *args, **kwargs):
            widget_value = f(label, *args, **kwargs)
            widget_values[label] = widget_value
            return widget_value
        return wrapper

    
    # PROJECT OVERVIEW INFORMATION
    st.markdown(member, True)
    st.markdown(h1,unsafe_allow_html=True)
    st.markdown(overview, True)
    col1, col2 = st.beta_columns((1,1))
    st.text("requirement")
    checkbox = make_recording_widget(st.checkbox("hello"))

    # col2.image('image/analysis_flow.png')
    # st.markdown(overview_2, True)

state = SessionState.get(position=0)

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