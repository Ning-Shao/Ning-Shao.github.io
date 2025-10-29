import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Google Store User Data Dashboard")
st.markdown("_Prototype_by_Ning_Shao_")

data = pd.read_csv("googleplaystore.csv")

st.subheader("Data Overview")
st.write(data.head())

category = st.selectbox("Select APP Category", data["Category"].dropna().unique())

filtered = data[data["Category"] == category]
