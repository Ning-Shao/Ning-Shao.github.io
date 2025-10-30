import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Google Store User Data Dashboard")
st.markdown("_Prototype_by_Ning_Shao_")

data = pd.read_csv("googleplaystore.csv")

# Drop rows with missing or invalid values
data = data.dropna(subset=["Rating", "Installs"])
data["Installs"] = data["Installs"].replace('[+,]', '', regex=True).astype(int)

# Add a combined success score (0.6 * Rating + 0.4 * log(Installs))
data["Success_Score"] = (data["Rating"] * 0.6) + (np.log1p(data["Installs"]) * 0.4)

# App title
st.title("App Success Metrics Dashboard")

# Metric selection menu
metric = st.selectbox(
    "Select a metric to measure app success:",
    ("Rating", "Installs", "Success_Score")
)

# Category selection menu
category = st.selectbox("Select an app category:", sorted(data["Category"].unique()))

# Filter data based on the selected category
filtered = data[data["Category"] == category]

# Plot histogram showing rating distribution
st.subheader(f"Rating Distribution for {category}")
fig, sc = plt.subplots()
ax.hist(filtered["Rating"].dropna(), bins=10, color="skyblue", edgecolor="black")
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")
st.pyplot(fig)