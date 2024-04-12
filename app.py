import streamlit as st
st.title("campusx")

st.image("1.jpg")

col1,col2= st.columns(2)

with col1:
    st.image("unnamed.jpg")

with col2:
    st.header("campusX on the platform")

st.header("Course")
st.subheader("DSMP1")
st.subheader("DSM2")
st.subheader("DSM3")
st.subheader("DSM4")
st.subheader("DSA")

st.sidebar.title("Menu")
st.sidebar.markdown("""
- Home
- About
- Contact
- career
- login
""")

st.sidebar.selectbox("select",["teacher","student"])
st.sidebar.button("select")

st.title("hello  teacher")