# 1. Libraries
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 2. Page Config
st.set_page_config(
    page_title="Google Store User Data Dashboard",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 3. Custom CSS to match my personal brand aesthetics
st.markdown("""
<style>
    /* General background */
    .main {
        background-color: #F7F7F5;
        color: #3C3C3C;
        font-family: 'Inter', 'Lato', 'Avenir', sans-serif;
    }

    /* Titles */
    h1, h2, h3 {
        color: #4A4A4A;
        text-align: center;
        font-weight: 600;
    }

    /* Description box */
    .stMarkdown p {
        color: #4F5D4E;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Select boxes */
    div[data-baseweb="select"] {
        background-color: #EDEDE9;
        border-radius: 8px;
    }

    /* Subtle divider */
    hr {
        border: none;
        border-top: 1px solid #CFE8CC;
        margin: 1.5em 0;
    }
</style>
""", unsafe_allow_html=True)

# 4. Headings
st.title("Google Store User Data Dashboard")
st.markdown("<p style='text-align:center; color:#5C8374; font-style:italic;'>Prototype by Ning Shao</p>", unsafe_allow_html=True)

# 5. Load Dataset
data = pd.read_csv("projects/googleplaystore.csv")

# 6. Data Cleaning
data["Installs"] = (
    data["Installs"]
    .replace('[+,]', '', regex=True)
    .replace('Varies with device', None)
    .replace('Free', None)
)

data["Installs"] = pd.to_numeric(data["Installs"], errors='coerce')
data = data.dropna(subset=["Installs", "Rating"])

# 7. Derived Metric
data["Success_Score"] = (data["Rating"] * 0.6) + (np.log1p(data["Installs"]) * 0.4)

# 8. Subheader
st.markdown("### App Success Metrics Dashboard")
st.markdown("""
**About the Success Score:**  
This metric combines *user satisfaction* (Rating) and *popularity* (Installs) to reflect an app’s overall success.  
It is calculated as:  
> **Success_Score = 0.6 × Rating + 0.4 × log(Installs)**  

A higher score means the app is both well-rated and widely installed.
""")

st.markdown("---")

# 9. User Controls
metric = st.selectbox(
    "Select a metric to measure app success:",
    ("Rating", "Installs", "Success_Score")
)

category = st.selectbox(
    "Select an app category:",
    sorted(data["Category"].unique())
)

filtered = data[data["Category"] == category]

# 10. Visualization
fig, ax = plt.subplots(figsize=(6, 4))
plt.style.use("seaborn-v0_8-whitegrid")

if metric == "Rating": 
    ax.hist(filtered["Rating"].dropna(), bins=10, color="#88C9BF", edgecolor="#5C8374")
    ax.set_title(f"Rating Distribution for {category}", color="#4A4A4A")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Frequency")

elif metric == "Installs":
    ax.hist(filtered["Installs"].dropna(), bins=10, color="#BFD8B8", edgecolor="#5C8374")
    ax.set_title(f"Installs Distribution for {category}", color="#4A4A4A")
    ax.set_xlabel("Installs (log scale)")
    ax.set_ylabel("Frequency")
    ax.set_xscale("log")

elif metric == "Success_Score":
    ax.scatter(filtered["Rating"], filtered["Installs"], alpha=0.6, color="#A3BFA8")
    ax.set_title(f"Success Score Distribution for {category}", color="#4A4A4A")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Installs (log scale)")
    ax.set_yscale("log")

st.pyplot(fig)

# 11. Summary Statistics
st.markdown("---")
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Rating", f"{filtered['Rating'].mean():.2f}")
col2.metric("Average Installs", f"{filtered['Installs'].mean():,.0f}")
col3.metric("Average Success Score", f"{filtered['Success_Score'].mean():.2f}")
