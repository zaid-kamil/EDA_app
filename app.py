# to run the application -->
# streamlit run app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

@st.cache
def load_dataset():
    '''
    reads the data from the url
    '''
    df =  pd.read_csv('https://raw.githubusercontent.com/digipodium/Datasets/main/automobile.csv',index_col=0)
    df.replace(to_replace="?",value=np.nan,inplace=True)
    df['normalized-losses'] = df['normalized-losses'].astype(float) 
    df['num-of-doors'] = df['num-of-doors'].astype(str) 
    df['bore'] = df['bore'].astype(float) 
    df['stroke'] = df['stroke'].astype(float) 
    df['price'] = df['price'].astype(float) 
    df['price'].replace(np.nan,df['price'].mean(),inplace=True)
    return df


st.title("Exploratory Data Analytics")
st.subheader("using Automobile dataset")
st.sidebar.subheader("Select options")

df = load_dataset()

options = ['View dataset','Numeric Correlation','Categorical Correlation']

selection = st.sidebar.radio("your options are",options)

if selection == options[0]:
    st.write(df)

if selection == options[1]:
    column_names = [ 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-size', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
    colx = st.sidebar.selectbox('Select column for X axis',column_names,help='take a numerical column')
    coly = st.sidebar.selectbox('Select column for Y axis',column_names,index=1,help='take a numerical column')
    color = st.sidebar.selectbox('Select column for hue',['make','engine-location','num-of-doors'],index=1,help='take a numerical column')
    try:
        out = sns.lmplot(x=colx, y=coly, data=df,aspect=2,height=7,hue=color)
        st.pyplot(out)
    except Exception as e:
        st.error(e)

if selection == options[2]:
    column_names =['normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'engine-type', 'num-of-cylinders', 'fuel-system']
    num_col_names = [ 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-size', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
    colx = st.sidebar.selectbox('Select column for X axis',column_names,help='take a categorical column')
    coly = st.sidebar.selectbox('Select column for Y axis',num_col_names,index=1,help='take a numerical column')
    ori = st.sidebar.radio("graph orientation",['h','v'])
    x_size = st.sidebar .number_input("graph size on x axis",5,30)
    y_size = st.sidebar .number_input("graph size on y axis",5,30)

    try:
        fig,ax= plt.subplots(figsize=(x_size,y_size))
        sns.boxplot(x=colx,y=coly,data=df,orient=ori,palette='rainbow',ax=ax)
        st.pyplot(fig)
    except Exception as e:
        st.error(e)