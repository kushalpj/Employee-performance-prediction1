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
    transition: 0.4s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 0px 35px rgba(56,189,248,0.4);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="title"> Employee Dashboard</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------- METRICS ----------------

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="card">
    <h3>Total Employees</h3>
    <h1>{len(df)}</h1>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
    <h3>Average Score</h3>
    <h1>{round(df['performance_score'].mean(),1)}</h1>
    </div>
    """, unsafe_allow_html=True)

with c3:
    high = len(df[df['performance_category']=="High Performer"])

    st.markdown(f"""
    <div class="card">
    <h3>High Performers</h3>
    <h1>{high}</h1>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- CHARTS ----------------

fig1 = px.histogram(
    df,
    x="department",
    color="performance_category",
    template="plotly_dark",
    title="Department Performance"
)

fig1.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font_color="white"
)

st.plotly_chart(fig1,use_container_width=True)

fig2 = px.scatter(
    df,
    x="years_experience",
    y="performance_score",
    color="performance_category",
    size="performance_score",
    template="plotly_dark",
    title="Experience vs Performance"
)

fig2.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font_color="white"
)

st.plotly_chart(fig2,use_container_width=True)