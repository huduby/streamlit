import streamlit as st

# working with widgets
# buttons/radio/checkbox/select/

# working with buttons
name = "Jesse"

# 같은 이름으로 위젯을 만들수는 없음.(key를 줘야함)
if st.button("Submit"):
    st.write(f"Name : {name.upper()}")

if st.button("Submit",key="new02"):
    st.write(f"First Name : {name.lower()}")
st.divider()
# radiobuttons
status = st.radio("What is your status",("Active","Inactive"))
if status == "Active":
    st.success("You ar active")
elif status == "Inactive":
    st.warning("Inactive")
    
st.divider()
# checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing something")

# expander
with st.expander("Python"):
    st.success("Hello Python")
st.divider()

# select/multi select
my_lang = ["Python","C","Java","C++","Julia","Go"]
choice = st.selectbox("Language",my_lang)
st.write("You selected ", choice)

# multiple selection
spoken_lang = ("English","Korea","French","Spanish")
my_spoken_lang = st.multiselect("Spoken Lang",spoken_lang,default="English")

# slider 
# numbers ( int/float )
age = st.slider("Age",1,100,20)
st.write(age)

# Any data
# select slider
color = st.select_slider("Choose Color",options=["red","yellow","blue","purple"],value=("red","yellow"))
