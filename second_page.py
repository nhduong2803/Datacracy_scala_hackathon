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
        
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report


data=pd.read_csv(r"/home/quannt/Documents/GitHub/Datacracy_scala_hackathon/data/cat_recommned.csv")
data['week'] = data.by_week.dt.week()
data['month'] = data.by_week.dt.month
def main():
    
    st.title("Title name")
    
    htk=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">CUSTOMER DESPOIT PREDICTION APP </h2>
    </div>
    """
    st.markdown(htk,unsafe_allow_html=True)

### demo add variables
    #st.sidebar.header("Book Category")

    # scale varible
    book_cat = st.selectbox('Book Category ', ('Sách nói', 'Sách tóm tắt', 'Truyện nói', 'Podcast', 'Thiếu nhi'))


    # caterigorical variable
    # job=st.selectbox("Enter the type of job customer do",( <field note> ))
    # job=int(encoder.fit_transform([[job]]))

    #require variable
    if book_cat  == 'Sách nói':
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == 'Sách nói')]

        st.dataframe(week.head(10))
    else:
        if duration.isalpha() and duration.isalnum():
            st.warning("Please enter an integer number")
            pass
        else:
            duration=int(duration)
            if duration>4918 or duration<0:
                st.warning("Please enter an number between 0 & 4918")
            duration=int(scaler.fit_transform([[duration]]))

    #fix variable

    # show result

    # if marital!="select" and education!="select" and default!="select" and housing!="select" and loan!="select" and contact!="select" and month!="select" and day_of_week!="select" and poutcome!="select":
        ### marital=int(encoder.fit_transform([[marital]]))

    #     with open("D:\\random_model.pkl",'rb') as f:
    #         rf=pickle.load(f)
    #     res=rf.predict([[age,job]])
    #     res=str(res)
    #     dict={"yes":'1',"no":'0'}    
    #     for i,j in dict.items():
    #         res=res.replace(j,i)
    # else:
    #     res="None"



if __name__=='__main__':
    Res=main()
    # Res=str(int(result))
    # dict={"yes":'1',"no":'0'}    
    # for i,j in dict.items():
    #     Res=Res.replace(j,i)
            
    # if st.sidebar.button("Show Prediction"):
    #     st.sidebar.subheader("The predicted response of customer or client to subscribe a term deposit is")
    #     st.sidebar.success(Res)
    # test abc
    