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
text = open("Datacracy_scala_hackathon/data/bundle_new_paid.csv", "r")
text = ''.join([i for i in text]).replace("[", "AAA")
x = open("output.csv","w")
x.writelines(text)
x.close()
contribution_cluster = pd.read_csv("data/contribution_paid_cluster.csv", sep = ",")
bundle_new_paid = pd.read_csv("data/bundle_new_paid.csv", sep = ",")
bundle_new_paid = bundle_new_paid[["consequents", "antecedents","lift"]].replace("[","").replace("'","")
bundle_potential = pd.read_csv("data/bundle_potential_user.csv", sep = ",")
bundle_potential = bundle_potential[["consequents", "antecedents","lift"]]
bundle_loyal = pd.read_csv("data/bundle_loyal_users.csv", sep = ",")
bundle_loyal = bundle_loyal[["consequents", "antecedents","lift"]]
listening_group = pd.read_csv("data/listening_group.csv", sep = ",")
# Text describe

def main():
    st.title("SCALA - HACKATHON - Team 03")
    #Introduce team members
    member = """
<p style='box-sizing: border-box; margin: 0px 0px 1rem; padding: 0px; font-size: 16px; font-weight: normal; caret-color: rgb(38, 39, 48); color: rgb(38, 39, 48); font-family: "IBM Plex Sans", sans-serif; font-style: normal; font-variant-caps: normal; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; line-height: 1.5;'><span style="font-family: Georgia, serif; font-size: 15px;">Nh&oacute;m gồm 5 th&agrave;nh vi&ecirc;n:</span></p>
<ul style='box-sizing: border-box; margin: 0px 0px 1rem; padding: 0px; font-size: 16px; font-weight: normal; caret-color: rgb(38, 39, 48); color: rgb(38, 39, 48); font-family: "IBM Plex Sans", sans-serif; font-style: normal; font-variant-caps: normal; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none;'>
    <li style="box-sizing: border-box; margin: 0.2em 0px 0.2em 1.2em; padding: 0px 0px 0px 0.6em; font-size: 1rem; line-height: 1.5;"><span style="font-size: 15px;"><span style="font-family: Georgia, serif;">Dương Thị Như Hải</span></span></li>
    <li style="box-sizing: border-box; margin: 0.2em 0px 0.2em 1.2em; padding: 0px 0px 0px 0.6em; font-size: 1rem; line-height: 1.5;"><span style="font-size: 15px;"><span style="font-family: Georgia, serif;">L&ecirc; Thu Thảo</span></span></li>
    <li style="box-sizing: border-box; margin: 0.2em 0px 0.2em 1.2em; padding: 0px 0px 0px 0.6em; font-size: 1rem; line-height: 1.5;"><span style="font-size: 15px;"><span style="font-family: Georgia, serif;">Nguyễn Trần Qu&acirc;n</span></span></li>
    <li style="box-sizing: border-box; margin: 0.2em 0px 0.2em 1.2em; padding: 0px 0px 0px 0.6em; font-size: 1rem; line-height: 1.5;"><span style="font-size: 15px;"><span style="font-family: Georgia, serif;">Vũ Thị Bảo Ngọc</span></span></li>
    <li style="box-sizing: border-box; margin: 0.2em 0px 0.2em 1.2em; padding: 0px 0px 0px 0.6em; font-size: 1rem; line-height: 1.5;"><span style="font-family: Georgia, serif; font-size: 15px;">Đới Thị Hồng</span></li>
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
    <p style="line-height: 1.5; text-align: justify;"><span style="font-family: Georgia, serif;">Sau bước EDA, nh&oacute;m đ&atilde; liệt k&ecirc; ra được 4 user case kh&aacute;c nhau để chứng minh cho giả thiết của m&igrave;nh cụ thể như sau:</span></p>
    """
    consumption = """
    <p style="line-height: 1.5;"><span style="font-family: Georgia, serif; font-size: 15px;">C&aacute;c segment mục ti&ecirc;u m&agrave; nh&oacute;m chọn l&agrave; những segment mang lại tỉ lệ doanh thu cao đối với doanh nghiệp, cụ thể l&agrave; 3 nh&oacute;m: Loyal Users, Potential Users v&agrave; New Paid Users (th&ocirc;ng tin cụ thể về việc đ&oacute;ng g&oacute;p doanh thu được thể hiện ở bảng b&ecirc;n dưới).</span></p>
    """

    bundle_introduction = """
    <p>Từ đ&oacute; nh&oacute;m x&aacute;c định được c&aacute;c bundle cho mỗi nh&oacute;m target kh&aacute;ch h&agrave;ng như b&ecirc;n dưới:</p>
    """

    summary = """
    <p style="line-height: 1.5;"><span style="font-size: 15px; font-family: Georgia, serif;">Nhận x&eacute;t chung về b&agrave;i của nh&oacute;m:</span></p>
<p style="line-height: 1.5;"><span style="font-family: Georgia, serif;"><span style="font-size: 15px;"><span style="color: rgb(0, 0, 0); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;"><strong>T&iacute;nh hiệu quả:&nbsp;</strong>Giải ph&aacute;p nh&oacute;m đưa ra tương đối đ&aacute;p ứng được c&aacute;c y&ecirc;u cầu của doanh nghiệp, tập trung chủ yếu v&agrave;o việc tăng t&iacute;nh tương t&aacute;c cho nh&oacute;m paid users. Tuy nhi&ecirc;n do thời gian hạn chế n&ecirc;n nh&oacute;m chưa thể t&igrave;m hiểu s&acirc;u hơn về bộ data v&agrave; thử nghiệm th&ecirc;m về c&aacute;c mối li&ecirc;n hệ giữa c&aacute;c yếu tố kh&aacute;c nhau về h&agrave;nh vi kh&aacute;ch h&agrave;ng để c&oacute; thể đưa ra những giải ph&aacute;p chuy&ecirc;n s&acirc;u hơn cho từng nh&oacute;m user kh&aacute;c nhau tr&ecirc;n nền tản</span></span></span></p>
<p style="line-height: 1.5;"><span style="font-family: Georgia, serif;"><span style="font-size: 15px;"><span style="color: rgb(0, 0, 0); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;"><strong>T&iacute;nh gi&aacute; trị:&nbsp;</strong>C&aacute;c giải ph&aacute;p nh&oacute;m đề xuất c&oacute; tiềm năng ứng dụng trong việc tăng t&iacute;nh tương t&aacute;c của user với ứng dụng Voizfm. Tuy nhi&ecirc;n chỉ g&oacute;p phần &yacute; tưởng v&agrave;o c&aacute;c chiến dịch marketing của doanh nghiệp, chưa c&oacute; sự đột ph&aacute; hay &yacute; tưởng v&agrave; technique mới lạ để tạo n&ecirc;n bước chuyển đổi cao về mặt doanh th</span></span></span></p>
<p style="line-height: 1.5;"><span style="color: rgb(0, 0, 0); font-family: Georgia, serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;"><strong>T&iacute;nh bền vững:&nbsp;</strong>Giải ph&aacute;p của nh&oacute;m đưa ra c&oacute; thể ứng dụng v&agrave; triển khai ở doanh nghiệp qua việc đưa th&ecirc;m c&aacute;c t&iacute;nh năng như cơ chế gợi &yacute; về c&aacute;c quyển s&aacute;ch tiếp theo, đề xuất c&aacute;c quyển s&aacute;ch ph&ugrave; hợp cho những nh&oacute;m users c&oacute; lịch sử đọc giống nhau v&agrave; triển khai c&aacute;c hoạt động marketing v&agrave;o c&aacute;c thời điểm trong ng&agrave;y. Doanh nghiệp c&oacute; thể ứng dụng l&acirc;u d&agrave;i để g&oacute;p phần v&agrave;o c&aacute;c chiến dịch marketing của m&igrave;nh. </span></p>"""

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
    st.markdown(member, True)
    st.markdown(h1,unsafe_allow_html=True)
    st.markdown(overview, True)
    # col1, col2 = st.beta_columns((1,1))
    # st.text("requirement")
    # checkbox = make_recording_widget(st.checkbox("hello"))

    # consumption
    st.markdown(h2,unsafe_allow_html=True)
    st.markdown(consumption, True)
    col1, col2, col3= st.beta_columns((1,4,1))
    # a = contribution_cluster.style.applymap(color_high_value)
    col2.write(contribution_cluster)
    st.markdown(bundle_introduction, True)


    col1, col2= st.beta_columns((1,5))
    # expand_bundle = st.expander()
    # expand_bundle.write("Bundle information on high value users")
    # with expand_bundle:
    #     clicked = st.button("Clieck me")
    info_selectbox = col1.selectbox("Segment",("Loyal users", "New paid", "Potential users"))
    if info_selectbox == "Loyal users":
        a1, a2, a3= st.beta_columns((1,10,1))
        a2.write(bundle_loyal)
    if info_selectbox == "New paid":
        a1, a2, a3= st.beta_columns((1,10,1))
        a2.write(bundle_new_paid)
    if info_selectbox == "Potential users":
        a1, a2, a3= st.beta_columns((1,10,1))
        a2.write(bundle_potential)

    # Use case
    st.markdown(h3,unsafe_allow_html=True)
    st.markdown(user_case, True)

    
    # st.write(case_study)
    st.image('Datacracy_scala_hackathon/image/case_study.png')
    # st.markdown(overview_2, True)
    fig_1 = px.bar(listening_group, x="", y="sub_cat", color = "timepoint_of_the_day", title="Long-Form Input")
    st.plotly_chart(fig_1)

    fig_2 = px.pie(listening_group, values='actual_duation', names='timepoint_of_the_day', title='Population of European continent')
    st.plotly_chart(fig_2)

    fig_3 = px.pie(listening_group, values='userID', names='timepoint_of_the_day', title='Population of European continent')
    st.plotly_chart(fig_3)


    #retro
    st.markdown(h4,unsafe_allow_html=True)
    st.markdown(summary, True)


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