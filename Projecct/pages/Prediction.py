import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(layout="wide")

# ---------------- LOAD ----------------

df = pd.read_csv("data/combined_employee_dataset_1.csv")
model = joblib.load("model.pkl")

# ---------------- CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #030712;
    color: white;
}

.stApp {
    background: linear-gradient(135deg,#020617,#000814,#020617);
}

/* Main Title */

.title {
    font-size: 55px;
    font-weight: 700;
    color: white;
    text-shadow: 0px 0px 25px #38bdf8;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {
        text-shadow: 0 0 10px #38bdf8;
    }
    to {
        text-shadow: 0 0 30px #38bdf8;
    }
}

/* Cards */

.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 22px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 0px 25px rgba(56,189,248,0.15);
    transition: 0.4s;
}

.metric-card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 0px 35px rgba(56,189,248,0.4);
}

/* Prediction */

.prediction-box {
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    animation: pulse 2s infinite;
    margin-top: 20px;
}

.high {
    background: linear-gradient(135deg,#064e3b,#10b981);
    box-shadow: 0px 0px 25px #10b981;
}

.medium {
    background: linear-gradient(135deg,#78350f,#f59e0b);
    box-shadow: 0px 0px 25px #f59e0b;
}

.low {
    background: linear-gradient(135deg,#7f1d1d,#ef4444);
    box-shadow: 0px 0px 25px #ef4444;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.03); }
    100% { transform: scale(1); }
}

/* Button */

.stButton>button {
    width: 100%;
    border-radius: 18px;
    background: linear-gradient(135deg,#38bdf8,#8b5cf6);
    color: white;
    border: none;
    padding: 16px;
    font-size: 18px;
    font-weight: 600;
    transition: 0.4s;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 25px #38bdf8;
}

/* Sliders */

.stSlider > div > div {
    color: #38bdf8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="title"> Employee Performance Prediction</div>',
    unsafe_allow_html=True
)

st.write("")

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h4>Total Employees</h4>
        <h1>{len(df)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h4>Average Score</h4>
        <h1>{round(df['performance_score'].mean(),1)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    high_count = len(df[df['performance_category']=="High Performer"])

    st.markdown(f"""
    <div class="metric-card">
        <h4>High Performers</h4>
        <h1>{high_count}</h1>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- INPUTS ----------------

left,right = st.columns(2)

with left:

    age = st.slider("Age",18,60,30)

    experience = st.slider("Experience",0,40,5)

    score = st.slider("Performance Score",1,10,5)

with right:

    education = st.selectbox(
        "Education",
        ["High School","Bachelor","Master","PhD"]
    )

    department = st.selectbox(
        "Department",
        ["HR","Finance","Sales","Tech"]
    )

# ---------------- ENCODING ----------------

edu_map = {
    "High School":0,
    "Bachelor":1,
    "Master":2,
    "PhD":3
}

dept_map = {
    "HR":0,
    "Finance":1,
    "Sales":2,
    "Tech":3
}

# ---------------- PREDICTION ----------------

input_data = np.array([[
    age,
    experience,
    edu_map[education],
    dept_map[department],
    score
]])

# ---------------- BUTTON ----------------

if st.button(" Analyze Employee"):

    prediction = model.predict(input_data)[0]

    # Adjust according to your model output

    if prediction == 2:
        label = " High Performer"
        css = "high"

    elif prediction == 1:
        label = " Medium Performer"
        css = "medium"

    else:
        label = " Low Performer"
        css = "low"

    st.markdown(f"""
    <div class="prediction-box {css}">
        {label}
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ---------------- COMPARISON GRAPH ----------------

    st.subheader("📊 Your Position vs Dataset")

    user_df = pd.DataFrame({
        "years_experience":[experience],
        "performance_score":[score],
        "type":["You"]
    })

    temp = df[["years_experience","performance_score"]]
    temp["type"] = "Dataset"

    final = pd.concat([temp,user_df])

    fig = px.scatter(
        final,
        x="years_experience",
        y="performance_score",
        color="type",
        size="performance_score",
        template="plotly_dark",
        title="Comparison Analysis"
    )

    fig.update_layout(
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font_color="white"
    )

    st.plotly_chart(fig,use_container_width=True)

    # ---------------- AI INSIGHT ----------------

    st.subheader(" AI Insight")

    if score > df['performance_score'].mean():
        st.success("✅ Above average performance")

    else:
        st.warning("⚠ Performance below average")

    if experience > 10:
        st.info("💼 Strong experience level")

    else:
        st.info("📈 Employee still growing professionally")