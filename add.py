import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px

def main():
    st.title("Plotting In streamlit with plotly")
    df = pd.read_csv("prog_languages_data.csv")
    st.dataframe(df)
    
    fig1 = px.pie(df.head(10),values="Sum",names="lang",title="프로그래밍 언어에 대한 Pie 그래프")
    st.plotly_chart(fig1)
    
    fig2= px.bar(df.head(10),x="lang",y="Sum")
    st.plotly_chart(fig2)
    

if __name__ == "__main__":
    main()
