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
    <p style="line-height: 1.5; text-align: justify;"><span style="color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">Voizfm l&agrave; nền tảng nghe S&aacute;ch n&oacute;i v&agrave; Podcast chất lượng cao, 100% Bản quyền lớn nhất Việt Nam.&nbsp;</span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;"><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">Case study:</span><a class="waffle-rich-text-link" href="https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit" style="text-decoration: none; color: rgb(0, 0, 0); font-family: docs-Calibri; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-skip-ink: none;">&nbsp;</a><a class="waffle-rich-text-link" href="https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit" style="text-decoration: underline; color: rgb(17, 85, 204); font-family: docs-Calibri; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-skip-ink: none;">https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edi</a><span style="font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: underline; color: rgb(17, 85, 204); text-decoration-skip-ink: none;">t</span><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">&nbsp;</span></span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;"><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">Dựa tr&ecirc;n nhu cầu của Voizfm, nh&oacute;m thực hiện nghi&ecirc;n cứu v&agrave; triển khai b&agrave;i to&aacute;n sau:&nbsp;</span></span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;"><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">1. &nbsp; &nbsp; &nbsp; &nbsp;Journey of Content Consumption: Tập trung v&agrave;o nh&oacute;m high-value users, ph&acirc;n t&iacute;ch tương t&aacute;c giữa User v&agrave; Contents (Playlist, Category) trong bộ Data của Voizfm&nbsp;</span></span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">2. &nbsp; &nbsp; &nbsp; &nbsp;Use Cases: Cluster users theo khẩu vị &ldquo;nghe&quot;</span></p>
    """

    user_case ="""
    <p style="line-height: 1.5; text-align: justify;">Sau bước EDA, nh&oacute;m đ&atilde; liệt k&ecirc; ra được 4 user case kh&aacute;c nhau để chứng minh cho giả thiế của m&igrave;nh cụ thể như sau:</p>
    """

    #Title list
    h1=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">CASE STUDY</h2>
    </div>
    """
    h2=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">USE CASE</h2>
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
    # col1, col2 = st.beta_columns((1,1))
    # st.text("requirement")
    # checkbox = make_recording_widget(st.checkbox("hello"))

    # Use case
    st.markdown(h2,unsafe_allow_html=True)
    st.markdown(user_case, True)
    # case_study = pd.read_csv("/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/user_case.csv", sep = ",")
    # st.write(case_study)
    st.image('/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/image/case_study.png')
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