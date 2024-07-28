# core pkgs
import streamlit as st
import pandas as pd
import numpy as np

# import Dat a Viz pkgs
import matplotlib.pyplot as plt
import matplotlib
# import seaborn as sns


# matplotlib.use("Agg") # TkAgg

def main():
    st.title("Plotting with st.pyplot")
    df = pd.read_csv("iris.csv")
    df2 = pd.read_csv("lang_data.csv")
    st.dataframe(df2.head())

    # previous method
    # df["spices"].value_counts().plot(kind="bar")
    # st.pyplot()
    
    # recommend
    fig,ax = plt.subplots()
    ax.scatter(*np.random.random(size=(2,100)))
    st.pyplot(fig)
    
    # recommend2
    fig = plt.figure()
    df["species"].value_counts().plot(kind="bar")
    st.pyplot(fig)
    
    # recommend3
    fig,ax=plt.subplots()
    df["species"].value_counts().plot(kind="bar")
    st.pyplot(fig)

    fig =plt.figure()
    sns.countplot(df["species"])
    st.pyplot(fig)    
    
    st.bar_chart(df[["sepal_length","petal_length"]])
    
    st.divider()
    
    lang_list = df2.columns[1:].tolist()
    # st.write(lang_list)
    lang_choices = st.multiselect("Language",lang_list,default="Python")
    new_df = df2[lang_choices]
    st.line_chart(new_df)
    
    st.area_chart(new_df)
if __name__ == "__main__":
    main()
    
    
