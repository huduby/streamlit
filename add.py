import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
import koreanize_matplotlib
import matplotlib.pyplot as plt
# import plotly.graph_objects as go

# pip install koreanize-matplotlib ( conda install 로는 찾을 수 없음 )

st.set_page_config(layout="wide")
empty1,content,empty2 = st.columns([0.5,8.0,1.5])

def main():
    with empty1:
        pass
    with content:
        st.title("부모님! 제 용돈을 올려야 합니다.")
        txt = """학교가 끝나고 학교 앞 문방구나 가게에서 사 먹는 간식.
맛도 달콤하고 나의 하루를 달콤하게 해주는데요..\n
이런 간식을 사 먹기 위해 우리는 용돈이 필요해요. 
간혹 용돈이 부족하다고 느껴질 때가 있나요?\n
하지만 부모님께 무턱대고 용돈을 올려달라고 말씀드렸다가는 퇴짜 맞기 쉽상이죠.\n
어떻게 하면 부모님을 설득하여 나의 용돈을 올릴 수 있을까요? """
        st.info(txt)        
        tab1,tab2 = st.tabs(["📋 데이터","📊 연도별 검색"])        
        with tab1:
            df = pd.read_csv("data\소비자물가지수_정제.csv",index_col="Unnamed: 0")
            st.subheader("년도별 간식 물가지수(2020년 100기준)")
            st.dataframe(df)
        with tab2:
            st.subheader("간식 종류별 물가지수 그래프")
            col1,col2 = st.columns([3,7],gap="medium")
            with col1:
                my_food = df.columns.to_list()
                choice = st.multiselect("",
                                        my_food,
                                        placeholder="==간식종류==")
            
            with col2:
                if len(choice):
                    df_1 = df[choice]
                    # st.dataframe(df_1)
                    x_label = np.arange(2003,2024)
                    fig = plt.figure(figsize=(15,8))
                    plt.rc("font",size=20)
                    for i in choice:
                        plt.plot(x_label,df_1[i],label=i,marker="o")
                    plt.xticks(x_label)
                    plt.title("내가 좋아하는 간식 물가지수",fontdict={"size":30})
                    plt.xticks(rotation=30)
                    plt.xlabel("연도")
                    plt.ylabel("물가지수")
                    plt.legend()
                    plt.grid()            
                    st.pyplot(fig)
    with empty2:
        pass
if __name__ == "__main__":

    main()



