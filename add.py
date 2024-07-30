import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# import plotly.graph_objects as go


def main():
    st.title("부모님! 제 용돈을 올려야 합니다.")
    st.write("""학교가 끝나고 학교 앞 문방구나 가게에서 사 먹는 간식.
             맛도 달콤하고 나의 하루를 달콤하게 해주는데요.. 
             이런 간식을 사 먹기 위해 우리는 용돈이 필요해요. 
             간혹 용돈이 부족하다고 느껴질 때가 있나요?
             하지만 부모님께 무턱대고 용돈을 올려달라고 말씀드렸다가는 퇴짜 맞기 쉽상이죠.
             어떻게 하면 부모님을 설득하여 나의 용돈을 올릴 수 있을까요? 
             """)
    st.divider()
    
    tab1,tab2 = st.tabs(["📋 데이터","📊 연도별 검색"])
    
    with tab1:
        df = pd.read_csv("data\소비자물가지수_정제.csv",index_col="Unnamed: 0")
        st.subheader("년도별 간식 물가지수(2020년 100기준)")
        st.dataframe(df)
    with tab2:
        my_food = df.columns.to_list()
        my_food.insert(0,"==간식종류==")
        st.subheader("간식 종류별 물가지수 그래프")
        choice = st.selectbox("",my_food)        
        if choice != "==간식종류==":
            df_1 = df[choice]
            fig = px.line(df_1,x=df_1.index,y=df_1.values)
            fig.update_layout(
                xaxis_title=dict(
                    text="<b>연도</b>"
                ),
                yaxis_title=f"<b>{choice} 물가지수</b>",
                font=dict(
                    family="Courier New, Monospace",
                    size=12,
                    color="#000000"
                )
            )
            st.plotly_chart(fig)
    
if __name__ == "__main__":
    main()



