import streamlit as st
import pandas as pd
import numpy as np
import koreanize_matplotlib
import matplotlib.pyplot as plt


@st.cache_data
def data_load():
    # 전체 데이터 1번 가져오기
    df_k = pd.read_csv("국내성씨별인구수데이터_수업용_정제.csv")
    df_e = pd.read_csv("미국lastname_상위100_수업용_정제.csv")
    df_e = df_e.sort_values(by="인구수",ascending=True)
    # 우리나라 성씨 랭킹 업데이트
    df_k["랭킹"] = df_k["인구수"].rank(method="min",ascending=False).astype(int)
    return df_k,df_e

# 웹 페이지 넓게 쓰기
st.set_page_config(layout="wide")
# 컬럼으로 나눠서 중간 컨텐츠 부분 사용하기
empty1,content,empty2 = st.columns([0.5,8.0,1.5])

def main():
    # 데이터 가져오기
    df_k,df_e = data_load()
    with empty1:
        pass
    with content:
        # 타이틀
        st.title("야!!! 너두 Smith??")
        txt = """도심 길거리에서 “김씨“ 를 부른다면 과연 몇 명이나 돌아볼까?
우리나라의 김씨만큼 미국에는 Smith씨가 많다고 한다.\n
우리나라와 미국의 성씨 데이터를 살펴보고 다양한 시각화를 통해서 그 말이 사실인지 알아보자. """
        st.info(txt)
        
        # 탭 만들기
        tab1,tab2,tab3 = st.tabs(["📊 우리나라 성씨 그래프","🔎 우리나라 성씨 랭킹 찾아보기","📊 미국 성씨 그래프"])        
        
        with tab1:
            st.success("""
                우리나라 성씨 데이터 시각화를 통해서 김(金)씨가 가장 많은 인구수를 차지한다는
                것을 알 수 있었다.    
                       """)                
            col1,col2 = st.columns([3,7],gap="medium")
            with col1:                
                # 데이터 보여주기        
                st.subheader("우리나라 성씨 살펴보기")
                st.dataframe(df_k[["성씨","인구수"]])
            with col2:
                # 성씨 TOP 10 랭킹 보여주기
                df_n = df_k.sort_values(by="인구수",ascending=False).head(10)
                fig = plt.figure(figsize=(7,5))
                plt.bar(df_n["성씨"],df_n["인구수"],color=["m","b","r","c"])
                plt.title("우리나라 성씨 TOP 10")
                plt.xlabel("성씨")
                plt.ylabel("인구수")
                plt.show()
                st.pyplot(fig)              
        with tab2:
            # 성씨 랭킹 찾아보기
            st.subheader("내 성씨는 몇 등? ")
            first_name = st.text_input(label="어떤 성씨를 찾아볼까?",max_chars=6)            
            query = df_k[["성씨","인구수","랭킹"]].sort_values(by="인구수",ascending=False)
            if first_name != "":
                query = df_k[df_k["성씨"].str.contains(first_name)][["성씨","인구수","랭킹"]].sort_values(by="인구수",ascending=False)
            st.dataframe(query)
        with tab3:
            st.success("""
                미국 성씨 데이터 시각화를 통해서 SMITH 씨가 가장 많은 인구수를 차지한다는
                것을 알 수 있었다.    
                       """)                  
            col3,col4 = st.columns([3,7],gap="medium")
            with col3:              
                st.subheader("미국 성씨 살펴보기")
                st.dataframe(df_e)
            with col4:
                # 미국 성씨 TOP 10 그래프 그리기
                fig = plt.figure(figsize=(6,4))
                df_g = df_e.tail(10)
                plt.barh(df_g["성씨"],df_g["인구수"],color=["m","b","r","c"])
                plt.title("미국 성씨 TOP 10")
                plt.xlabel("성씨")
                plt.ylabel("인구수")
                plt.show()
                st.pyplot(fig)
    with empty2:
        pass
if __name__ == "__main__":
    main()
