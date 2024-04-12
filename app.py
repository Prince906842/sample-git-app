import streamlit as st
st.title("campusx")

st.image("unnamed.jpg")

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