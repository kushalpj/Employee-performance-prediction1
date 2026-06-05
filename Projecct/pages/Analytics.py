import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("data/combined_employee_dataset_1.csv")

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#020617,#000814,#020617);
    color: white;
}

/* Title */

.title {
    font-size: 55px;
    font-weight: 700;
    color: white;
    text-shadow: 0px 0px 25px #38bdf8;
}

/* Cards */

.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 22px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 0px 25px rgba(56,189,248,0.15);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="title">📈 Employee Analytics</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------- PIE CHART ----------------

fig1 = px.pie(
    df,
    names="performance_category",
    template="plotly_dark",
    title="Performance Distribution"
)

fig1.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font_color="white"
)

st.plotly_chart(fig1,use_container_width=True)

# ---------------- BOXPLOT ----------------

fig2 = px.box(
    df,
    x="department",
    y="performance_score",
    color="department",
    template="plotly_dark",
    title="Department vs Performance"
)

fig2.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font_color="white"
)

st.plotly_chart(fig2,use_container_width=True)

# ---------------- HEATMAP ----------------

corr = df.corr(numeric_only=True)

fig3 = px.imshow(
    corr,
    text_auto=True,
    template="plotly_dark",
    title="Correlation Heatmap"
)

fig3.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font_color="white"
)

st.plotly_chart(fig3,use_container_width=True)