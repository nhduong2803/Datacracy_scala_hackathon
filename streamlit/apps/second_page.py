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


cat_recommned=pd.read_csv(r"/Users/hato/Documents/GitHub/Datacracy_scala_hackathon/data/cat_recommned.csv")
cat_recommned.by_week = pd.to_datetime(cat_recommned['by_week'], format='%Y-%m-%d')
cat_recommned['week'] = cat_recommned.by_week.dt.week
cat_recommned['month'] = cat_recommned.by_week.dt.month
def main():
    
    st.title("Title name")
    
    htk=  """
    <div style="background-color:#004d99;padding:0px">
    <h2 style="color:white;text-align:center;">Những cuốn sách có lượt đọc cao trong 7 ngày </h2>
    </div>
    """
    st.markdown(htk,unsafe_allow_html=True)

### demo add variables

    # scale varible
    book_cat = st.selectbox('Book Category ', ('Sách nói', 'Sách tóm tắt', 'Truyện nói', 'Podcast', 'Thiếu nhi'))
    #require variable
    if book_cat  == 'Sách nói':
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == book_cat)]\
            .sort_values(by = ['avg_actual','actual_duation','playlistID','playlist_name'], ascending = False)\

        week = week.groupby(['cat','sub_cat','playlist_name']).agg({
            'avg_actual':'sum',
            'actual_duation': 'sum',
            'playlistID': 'sum'
        }).reset_index().sort_values(by = ['avg_actual','actual_duation','playlistID'], ascending = False)

        st.dataframe(week[['cat','sub_cat','playlist_name']].head(10))

    elif book_cat == 'Sách tóm tắt':
        week = cat_recommned[(cat_recommned.week == cat_recommned.week.max()) & (cat_recommned.cat == book_cat)] \
                .sort_values(by=['avg_actual', 'actual_duation', 'playlistID', 'playlist_name'], ascending=False) \

        week = week.groupby(['cat', 'sub_cat', 'playlist_name']).agg({

            'avg_actual': 'sum',

            'actual_duation': 'sum',

            'playlistID': 'sum'

        }).reset_index().sort_values(by=['avg_actual', 'actual_duation', 'playlistID'], ascending=False)

        st.dataframe(week[['cat', 'sub_cat', 'playlist_name']].head(10))

    elif book_cat == 'Truyện nói':
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