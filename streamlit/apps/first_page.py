from os import write
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
import plotly.express as px


st.set_page_config(layout="wide")
# Load data

contribution_cluster = pd.read_csv("/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/contribution_paid_cluster.csv", sep = ",")
bundle_new_paid = pd.read_csv("/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/bundle_new_paid.csv", sep = ",")
bundle_new_paid = bundle_new_paid[["consequents", "antecedents","lift"]].replace("[","").replace("'","")
bundle_potential = pd.read_csv("/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/bundle_potential_user.csv", sep = ",")
bundle_potential = bundle_potential[["consequents", "antecedents","lift"]]
bundle_loyal = pd.read_csv("/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/bundle_loyal_users.csv", sep = ",")
bundle_loyal = bundle_loyal[["consequents", "antecedents","lift"]]
listening_group = pd.read_csv("/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/listening_group.csv", sep = ",")
# Text describe

def main():
    st.title("SCALA - HACKATHON - Team 03")
    #Introduce team members
    member = """
<p style='box-sizing: border-box; margin: 0px 0px 1rem; padding: 0px; font-size: 16px; font-weight: normal; caret-color: rgb(38, 39, 48); color: rgb(38, 39, 48); font-family: "IBM Plex Sans", sans-serif; font-style: normal; font-variant-caps: normal; letter-spacing: normal; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; line-height: 1.15; text-align: justify;'><span style="box-sizing: border-box; color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">Voizfm l&agrave; n???n t???ng nghe S&aacute;ch n&oacute;i v&agrave; Podcast ch???t l?????ng cao, 100% B???n quy???n l???n nh???t Vi???t Nam.&nbsp;</span></p>
<p style='box-sizing: border-box; margin: 0px 0px 1rem; padding: 0px; font-size: 16px; font-weight: normal; caret-color: rgb(38, 39, 48); color: rgb(38, 39, 48); font-family: "IBM Plex Sans", sans-serif; font-style: normal; font-variant-caps: normal; letter-spacing: normal; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; line-height: 1.15; text-align: justify;'><span style="box-sizing: border-box; font-family: Georgia, serif;"><span style="box-sizing: border-box; color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">Case study:</span><a class="waffle-rich-text-link" href="https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit" style="box-sizing: border-box; color: rgb(0, 0, 0); text-decoration-line: underline; text-decoration: none; font-family: docs-Calibri; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px;">&nbsp;</a><a class="waffle-rich-text-link" href="https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit" style="box-sizing: border-box; color: rgb(17, 85, 204); text-decoration-line: underline; text-decoration: underline; font-family: docs-Calibri; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px;">https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edi</a><span style="box-sizing: border-box; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: underline; color: rgb(17, 85, 204);">t</span><span style="box-sizing: border-box; color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">&nbsp;</span></span></p>
<p style='box-sizing: border-box; margin: 0px 0px 1rem; padding: 0px; font-size: 16px; font-weight: normal; caret-color: rgb(38, 39, 48); color: rgb(38, 39, 48); font-family: "IBM Plex Sans", sans-serif; font-style: normal; font-variant-caps: normal; letter-spacing: normal; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; line-height: 1.15; text-align: justify;'><span style="box-sizing: border-box; font-family: Georgia, serif;"><span style="box-sizing: border-box; color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">D???a tr&ecirc;n nhu c???u c???a Voizfm, nh&oacute;m th???c hi???n nghi&ecirc;n c???u v&agrave; tri???n khai b&agrave;i to&aacute;n sau:&nbsp;</span></span></p>
<p style='box-sizing: border-box; margin: 0px 0px 1rem; padding: 0px; font-size: 16px; font-weight: normal; caret-color: rgb(38, 39, 48); color: rgb(38, 39, 48); font-family: "IBM Plex Sans", sans-serif; font-style: normal; font-variant-caps: normal; letter-spacing: normal; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; line-height: 1.15; text-align: justify;'><span style="box-sizing: border-box; font-family: Georgia, serif;"><span style="box-sizing: border-box; color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">1. &nbsp; &nbsp; &nbsp; &nbsp;Journey of Content Consumption: T???p trung v&agrave;o nh&oacute;m high-value users, ph&acirc;n t&iacute;ch t????ng t&aacute;c gi???a User v&agrave; Contents (Playlist, Category) trong b??? Data c???a Voizfm&nbsp;</span></span></p>
<p style='box-sizing: border-box; margin: 0px 0px 1rem; padding: 0px; font-size: 16px; font-weight: normal; caret-color: rgb(38, 39, 48); color: rgb(38, 39, 48); font-family: "IBM Plex Sans", sans-serif; font-style: normal; font-variant-caps: normal; letter-spacing: normal; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; line-height: 1.15; text-align: justify;'><span style="box-sizing: border-box; color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">2. &nbsp; &nbsp; &nbsp; &nbsp;Use Cases: Cluster users theo kh???u v??? &ldquo;nghe&quot;</span></p>
    """

    overview = """
    <p style="line-height: 1.5; text-align: justify;"><span style="color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">Voizfm l&agrave; n???n t???ng nghe S&aacute;ch n&oacute;i v&agrave; Podcast ch???t l?????ng cao, 100% B???n quy???n l???n nh???t Vi???t Nam.&nbsp;</span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;"><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">Case study:</span><a class="waffle-rich-text-link" href="https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit" style="text-decoration: none; color: rgb(0, 0, 0); font-family: docs-Calibri; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-skip-ink: none;">&nbsp;</a><a class="waffle-rich-text-link" href="https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edit" style="text-decoration: underline; color: rgb(17, 85, 204); font-family: docs-Calibri; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-skip-ink: none;">https://docs.google.com/document/d/1wQgf5Vmhp1nEYmtdoYJhQx93S1nQg0C6NyzIjCfEq7I/edi</a><span style="font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: underline; color: rgb(17, 85, 204); text-decoration-skip-ink: none;">t</span><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">&nbsp;</span></span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;"><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">D???a tr&ecirc;n nhu c???u c???a Voizfm, nh&oacute;m th???c hi???n nghi&ecirc;n c???u v&agrave; tri???n khai b&agrave;i to&aacute;n sau:&nbsp;</span></span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;"><span style="color: rgb(0, 0, 0); font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">1. &nbsp; &nbsp; &nbsp; &nbsp;Journey of Content Consumption: T???p trung v&agrave;o nh&oacute;m high-value users, ph&acirc;n t&iacute;ch t????ng t&aacute;c gi???a User v&agrave; Contents (Playlist, Category) trong b??? Data c???a Voizfm&nbsp;</span></span></p>
<p style="line-height: 1.5; text-align: justify;"><span style="color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none; text-decoration-skip-ink: none;">2. &nbsp; &nbsp; &nbsp; &nbsp;Use Cases: Cluster users theo kh???u v??? &ldquo;nghe&quot;</span></p>
    """

    user_case ="""
    <p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;">Sau b?????c EDA, nh&oacute;m ??&atilde; li???t k&ecirc; ra ???????c 4 user case kh&aacute;c nhau ????? ch???ng minh cho gi??? thi???t c???a m&igrave;nh c??? th??? nh?? sau:</span></p>
    """
    consumption = """
    <p style="line-height: 1.5;"><span style="font-family: Georgia, serif; font-size: 15px;">C&aacute;c segment m???c ti&ecirc;u m&agrave; nh&oacute;m ch???n l&agrave; nh???ng segment mang l???i t??? l??? doanh thu cao ?????i v???i doanh nghi???p, c??? th??? l&agrave; 3 nh&oacute;m: Loyal Users, Potential Users v&agrave; New Paid Users (th&ocirc;ng tin c??? th??? v??? vi???c ??&oacute;ng g&oacute;p doanh thu ???????c th??? hi???n ??? b???ng b&ecirc;n d?????i).</span></p>
    """

    bundle_introduction = """
    <p>T??? ??&oacute; nh&oacute;m x&aacute;c ?????nh ???????c c&aacute;c bundle cho m???i nh&oacute;m target kh&aacute;ch h&agrave;ng nh?? b&ecirc;n d?????i:</p>
    """

    summary = """
    <p style="line-height: 1.5;"><span style="font-size: 15px; font-family: Georgia, serif;">Nh???n x&eacute;t chung v??? b&agrave;i c???a nh&oacute;m:</span></p>
<p style="line-height: 1.5;"><span style="font-family: Georgia, serif;"><span style="font-size: 15px;"><span style="color: rgb(0, 0, 0); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;"><strong>T&iacute;nh hi???u qu???:&nbsp;</strong>Gi???i ph&aacute;p nh&oacute;m ????a ra t????ng ?????i ??&aacute;p ???ng ???????c c&aacute;c y&ecirc;u c???u c???a doanh nghi???p, t???p trung ch??? y???u v&agrave;o vi???c t??ng t&iacute;nh t????ng t&aacute;c cho nh&oacute;m paid users. Tuy nhi&ecirc;n do th???i gian h???n ch??? n&ecirc;n nh&oacute;m ch??a th??? t&igrave;m hi???u s&acirc;u h??n v??? b??? data v&agrave; th??? nghi???m th&ecirc;m v??? c&aacute;c m???i li&ecirc;n h??? gi???a c&aacute;c y???u t??? kh&aacute;c nhau v??? h&agrave;nh vi kh&aacute;ch h&agrave;ng ????? c&oacute; th??? ????a ra nh???ng gi???i ph&aacute;p chuy&ecirc;n s&acirc;u h??n cho t???ng nh&oacute;m user kh&aacute;c nhau tr&ecirc;n n???n t???n</span></span></span></p>
<p style="line-height: 1.5;"><span style="font-family: Georgia, serif;"><span style="font-size: 15px;"><span style="color: rgb(0, 0, 0); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;"><strong>T&iacute;nh gi&aacute; tr???:&nbsp;</strong>C&aacute;c gi???i ph&aacute;p nh&oacute;m ????? xu???t c&oacute; ti???m n??ng ???ng d???ng trong vi???c t??ng t&iacute;nh t????ng t&aacute;c c???a user v???i ???ng d???ng Voizfm. Tuy nhi&ecirc;n ch??? g&oacute;p ph???n &yacute; t?????ng v&agrave;o c&aacute;c chi???n d???ch marketing c???a doanh nghi???p, ch??a c&oacute; s??? ?????t ph&aacute; hay &yacute; t?????ng v&agrave; technique m???i l??? ????? t???o n&ecirc;n b?????c chuy???n ?????i cao v??? m???t doanh th</span></span></span></p>
<p style="line-height: 1.5;"><span style="color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;"><strong>T&iacute;nh b???n v???ng:&nbsp;</strong>Gi???i ph&aacute;p c???a nh&oacute;m ????a ra c&oacute; th??? ???ng d???ng v&agrave; tri???n khai ??? doanh nghi???p qua vi???c ????a th&ecirc;m c&aacute;c t&iacute;nh n??ng nh?? c?? ch??? g???i &yacute; v??? c&aacute;c quy???n s&aacute;ch ti???p theo, ????? xu???t c&aacute;c quy???n s&aacute;ch ph&ugrave; h???p cho nh???ng nh&oacute;m users c&oacute; l???ch s??? ?????c gi???ng nhau v&agrave; tri???n khai c&aacute;c ho???t ?????ng marketing v&agrave;o c&aacute;c th???i ??i???m trong ng&agrave;y. Doanh nghi???p c&oacute; th??? ???ng d???ng l&acirc;u d&agrave;i ????? g&oacute;p ph???n v&agrave;o c&aacute;c chi???n d???ch marketing c???a m&igrave;nh. </span></p>"""

    #Title list
    h1=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">CASE STUDY</h2>
    </div>
    """
    h2=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">CONSUMPTION</h2>
    </div>
    """
    h3=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">CASE STUDY </h2>
    </div>
    """

    h4=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">PROJECT RETRO</h2>
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

    def color_high_value(val):
        color = 'red' if int(val) < 0 else 'black'
        return 'color: %s' % color
    # PROJECT OVERVIEW INFORMATION
    # st.markdown(member, True)
    st.markdown(h1,unsafe_allow_html=True)
    st.markdown(overview, True)
    # col1, col2 = st.beta_columns((1,1))
    # st.text("requirement")
    # checkbox = make_recording_widget(st.checkbox("hello"))

    # consumption
    st.markdown(h2,unsafe_allow_html=True)
    st.markdown(consumption, True)
    # col1, col2, col3= st.beta_columns((1,4,1))
    # a = contribution_cluster.style.applymap(color_high_value)
    st.write(contribution_cluster)
    st.markdown(bundle_introduction, True)


    col1, col2= st.columns((1,5))
    # expand_bundle = st.expander()
    # expand_bundle.write("Bundle information on high value users")
    # with expand_bundle:
    #     clicked = st.button("Clieck me")
    info_selectbox = col1.selectbox("Segment",("Loyal users", "New paid", "Potential users"))
    if info_selectbox == "Loyal users":
        st.write(bundle_loyal)
    if info_selectbox == "New paid":
        # a1, a2, a3= st.beta_columns((1,10,1))
        st.write(bundle_new_paid)
    if info_selectbox == "Potential users":
        # a1, a2, a3= st.beta_columns((1,10,1))
        st.write(bundle_potential)

    # Use case
    a1, a2, a3= st.columns((2,8,2))
    st.markdown(h3,unsafe_allow_html=True)
    a2.markdown(user_case, True)

    
    # st.write(case_study)
    st.image('/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/image/case_study.png')
    duration_explain = """
    <p style="line-height: 1.5;"><span style="font-family: Georgia, serif; font-size: 15px;"><strong>Usercase 02</strong>: V??? y???u t??? nghe tr&ecirc;n m???i khung th???i gian, t&iacute;nh v??? t???ng quan tuy c&oacute; s??? thay ?????i kh&ocirc;ng nhi???u nh??ng n???u t&iacute;nh tr&ecirc;n t???ng category th&igrave; h&agrave;nh vi c???a ng?????i nghe c&oacute; s??? kh&aacute;c nhau nh???t ?????nh.</span></p>
    """
    st.markdown(duration_explain, True)
    col1, col2 = st.columns((1,1))
    col1.image('/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/image/image_1.png')
    col2.image("/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/image/image_2.png")
    
    a1, a2 = st.columns((1,1))
    a = listening_group[listening_group["sub_cat"]== "T??m linh"]
    b=a.groupby(["timepoint_of_the_day"]).agg({"actual_duation":'sum', "userID":'count'}).reset_index()
    a1.text("Sub-cat: H??? t??m linh")
    a1.write(b)

    c = listening_group[listening_group["sub_cat"]== "S??ch t??m t???t"]
    d=c.groupby(["timepoint_of_the_day"]).agg({"actual_duation":'sum', "userID":'count'}).reset_index()
    a2.text("Sub-cat: S??ch t??m t???t")
    a2.write(d)
    explain = """
    <p style="line-height: 1.5;"><span style="font-family: Georgia, serif; font-size: 15px;">K???t lu???n: ??? 2 b???ng tr&ecirc;n, Voiz c&oacute; th??? c&acirc;n nh???c c&aacute;c ch&iacute;nh s&aacute;ch promote m???t th??? lo???i s&aacute;ch c??? th??? v&agrave;o khung gi??? th&iacute;ch h???p tr&ecirc;n banner, tu??? v&agrave;o ?????nh h?????ng ph&aacute;t tri???n c???a Voiz ho???c tu??? v&agrave;o ch&iacute;nh s&aacute;ch k???t h???p v???i t&aacute;c gi???/ nh&agrave; xu???t b???n.</span></p>
    """
    st.markdown(explain, unsafe_allow_html=True)

    # XXX
    title_usecase2 = """
    <p><strong>User case 03</strong>: Recommend playlist s&aacute;ch y&ecirc;u th&iacute;ch theo category</p>
    """
    st.markdown(title_usecase2,unsafe_allow_html=True)
    cat_recommned=pd.read_csv(r"/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/cat_recommned.csv")
    cat_recommned.by_week = pd.to_datetime(cat_recommned['by_week'], format='%Y-%m-%d')
    cat_recommned['week'] = cat_recommned.by_week.dt.week
    cat_recommned['month'] = cat_recommned.by_week.dt.month
    book_cat = st.selectbox('Book Category ', ('S??ch n??i', 'S??ch t??m t???t', 'Truy???n n??i', 'Podcast', 'Thi???u nhi'))
    #require variable
    if book_cat  == 'S??ch n??i':
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == book_cat)]\
            .sort_values(by = ['avg_actual','actual_duation','playlistID','playlist_name'], ascending = False)\

        week = week.groupby(['cat','sub_cat','playlist_name']).agg({
            'avg_actual':'sum',
            'actual_duation': 'sum',
            'playlistID': 'sum'
        }).reset_index().sort_values(by = ['avg_actual','actual_duation','playlistID'], ascending = False)

        st.dataframe(week[['cat','sub_cat','playlist_name']].head(10))

    elif book_cat == 'S??ch t??m t???t':
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == book_cat)] \
                .sort_values(by=['avg_actual', 'actual_duation', 'playlistID', 'playlist_name'], ascending=False) \

        week = week.groupby(['cat', 'sub_cat', 'playlist_name']).agg({

            'avg_actual': 'sum',

            'actual_duation': 'sum',

            'playlistID': 'sum'

        }).reset_index().sort_values(by=['avg_actual', 'actual_duation', 'playlistID'], ascending=False)

        st.dataframe(week[['cat', 'sub_cat', 'playlist_name']].head(10))

    elif book_cat == 'Truy???n n??i':
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == book_cat)] \
                .sort_values(by=['avg_actual', 'actual_duation', 'playlistID', 'playlist_name'], ascending=False) \

        week = week.groupby(['cat', 'sub_cat', 'playlist_name']).agg({

            'avg_actual': 'sum',

            'actual_duation': 'sum',

            'playlistID': 'sum'

        }).reset_index().sort_values(by=['avg_actual', 'actual_duation', 'playlistID'], ascending=False)

        st.dataframe(week[['cat', 'sub_cat', 'playlist_name']].head(10))

    elif book_cat == 'Podcast':
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == book_cat)] \
                .sort_values(by=['avg_actual', 'actual_duation', 'playlistID', 'playlist_name'], ascending=False) \

        week = week.groupby(['cat', 'sub_cat', 'playlist_name']).agg({

            'avg_actual': 'sum',

            'actual_duation': 'sum',

            'playlistID': 'sum'

        }).reset_index().sort_values(by=['avg_actual', 'actual_duation', 'playlistID'], ascending=False)

        st.dataframe(week[['cat', 'sub_cat', 'playlist_name']].head(10))

    else :
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == book_cat)] \
                .sort_values(by=['avg_actual', 'actual_duation', 'playlistID', 'playlist_name'], ascending=False) \

        week = week.groupby(['cat', 'sub_cat', 'playlist_name']).agg({

            'avg_actual': 'sum',

            'actual_duation': 'sum',

            'playlistID': 'sum'

        }).reset_index().sort_values(by=['avg_actual', 'actual_duation', 'playlistID'], ascending=False)

        st.dataframe(week[['cat', 'sub_cat', 'playlist_name']].head(10))


    


    #retro
    st.markdown(h4,unsafe_allow_html=True)
    st.markdown(summary, True)



if __name__=='__main__':
    Res=main()
