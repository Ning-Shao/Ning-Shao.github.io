#========================================================
# 1. libraries & confi
#========================================================
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Google Store User Data Dashboard",
    layout="centered",
    initial_sidebar_state="collapsed"
)
#========================================================
# 2. page styling
#========================================================
st. markdown("""
<style>
.main {
    background-color: #F7F7F5;
    color: #3C3C3C;
    font-family: 'Inter', 'Lato', 'Avenir', sans-serif;
}
h1, h2, h3 {
    color: #4A4A4A;
    text-align: center;
    font-weight: 600;
}
p, li {
    color: #4F5D4E;
    font-size: 16px;
    line-height: 1.6;
}
div[data-baseweb="select"] {
    background-color: #EDEDE9;
    border-radius: 8px;
}
hr {
    border: none;
    border-top: 1px solid #CFE8CC;
    margin: 1.5em 0;
}
</style>
""", unsafe_allow_html=True)

#========================================================
# 3. header
#========================================================
st.title("Google Store User Data Dashboard")
st.markdown("<p style='text-align:center; color:#5C8374; font-style:italic;'>Prototype by Ning Shao</p>", unsafe_allow_html=True)
st.markdown("---")

#========================================================
# 4. data loading & cleaning
#========================================================
data = pd.read_csv("projects/googleplaystore.csv")

data["Installs"] = (
    data["Installs"]
    .replace('[+,]', '', regex=True)
    .replace('Varies with device', None)
    .replace('Free', None)
)
data["Installs"] = pd.to_numeric(data["Installs"], errors='coerce')
data = data.dropna(subset=["Installs", "Rating"])
data["Success_Score"] = (data["Rating"] * 0.6) + (np.log1p(data["Installs"]) * 0.4)

# =====================================================
# 5. description
# =====================================================
st.subheader("App Success Metrics Dashboard")
st.markdown("""
About the **Success Score**:  
This metric combines *user satisfaction* (Rating) and *popularity* (Installs)  
to reflect an app’s overall success.  
> **Success_Score = 0.6 × Rating + 0.4 × log(Installs)**  

A higher score means the app is both well-rated and widely installed.
""")
st.markdown("---")

# =====================================================
# 6. USER CONTROLS
# =====================================================
metric = st.selectbox("Select a metric to measure app success:", ("Rating", "Installs", "Success_Score"))
category = st.selectbox("Select an app category:", sorted(data["Category"].unique()))
filtered = data[data["Category"] == category]

# =====================================================
# 7. VISUALIZATION TABS
# =====================================================
sns.set_style("whitegrid")
plt.rcParams.update({
    "axes.facecolor": "#F8F9F8",
    "axes.edgecolor": "#5C8374",
    "axes.labelcolor": "#4A4A4A",
    "xtick.color": "#4A4A4A",
    "ytick.color": "#4A4A4A",
    "text.color": "#4A4A4A",
})

tab1, tab2, tab3 = st.tabs(["Histogram", "Pie Chart", "Box Plot"])

# --- Tab 1: Histogram ---
with tab1:
    fig, ax = plt.subplots(figsize=(7, 4))
    if metric == "Rating":
        sns.histplot(filtered["Rating"].dropna(), bins=10, kde=True, color="#88C9BF", edgecolor="#5C8374", ax=ax)
        ax.set_title(f"Rating Distribution for {category}")
    elif metric == "Installs":
        sns.histplot(filtered["Installs"].dropna(), bins=10, kde=True, color="#BFD8B8", edgecolor="#5C8374", ax=ax)
        ax.set_xscale("log")
        ax.set_title(f"Installs Distribution for {category}")
    elif metric == "Success_Score":
        sns.kdeplot(filtered["Success_Score"].dropna(), fill=True, color="#5C8374", alpha=0.5, ax=ax)
        ax.set_title(f"Success Score Distribution for {category}")
    ax.set_xlabel(metric)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# --- Tab 2: Pie Chart ---
with tab2:
    st.markdown("### Category Share in Dataset")

    # Count all categories
    cat_counts = data["Category"].value_counts()

    N = 7
    top_cats = cat_counts.head(N)

    while (cat_counts[N:].sum() / cat_counts.sum())>0.4 and N <15: 
        N += 2
        top_cats = cat_counts.head(N)
        
    if category not in cat_counts.index:
        top_cats[category] = cat_counts[category]
        
    others_sum = cat_counts[~cat_counts.index.isin(top_cats.index)].sum()
    top_cats["OTHERS"] = others_sum

    top_cats = top_cats.sort_values(ascending=False)

    if "OTHERS" in top_cats.index:
        others_index = lsit(top_cats.index).index("OTHERS")
        wedges[others_index].set_alpha(0.3)
    
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax2.pie(
        top_cats,
        labels=top_cats.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#88C9BF", "#B8E0D2", "#C4DFE6", "#6B9080", "#A4C3B2", "#CCE3DE", "#D8E2DC", "#F8EDEB"],
        textprops={"color": "#3C3C3C", "fontsize": 10}
    )
    ax2.axis("equal")
    ax2.set_title("Category Distribution (Top Categories + Current)", fontsize=13, color="#4A4A4A", pad=20)
    st.pyplot(fig2)

# --- Tab 3: Box Plot ---
with tab3:
    fig3, ax3 = plt.subplots(figsize=(9, 14))
    sns.boxplot(y="Category", x=metric, data=data, palette=["#88C9BF"], ax=ax3)

    ax3.set_title(f"{metric} Spread Across Categories", fontsize=13, color="#4A4A4A", pad=20)
    ax3.set_xlabel(metric, fontsize=11)
    ax3.set_ylabel("Category", fontsize=11)

    st.pyplot(fig3)


# =====================================================
# 8. descriptive statistics
# =====================================================

desc = filtered[["Rating", "Installs", "Success_Score"]].describe().T
desc = desc.rename(columns={
    "mean": "Mean",
    "std": "Std. Dev.",
    "min": "Min",
    "max": "Max"
})[["Mean", "Std. Dev.", "Min", "Max"]]

# header
st.markdown(f"### Descriptive Statistics for *{category}* Apps")

# use streamlit dataframe
st.dataframe(desc.style.set_properties(**{'text-align': 'right'}))

st.markdown("""
    <style>
        .stDownloadButton button {
            background-color: #88C9BF;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5em 1.2em;
            font-size: 15px;
            transition: all 0.3s ease;
        }
        .stDownloadButton button:hover {
            background-color: #5C8374;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# offer csv download button
st.download_button(
    "Download CSV",
    desc.to_csv().encode("utf-8"),
    "summary.csv",
    help="Download descriptive statistics as CSV file"
)

# =====================================================
# 9. summary statistics
# =====================================================
col1, col2, col3 = st.columns(3)
col1.metric("Average Rating", f"{filtered['Rating'].mean():.2f}")
col2.metric("Average Installs", f"{filtered['Installs'].mean():,.0f}")
col3.metric("Average Success Score", f"{filtered['Success_Score'].mean():.2f}")








