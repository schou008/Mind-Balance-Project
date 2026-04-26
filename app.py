import streamlit as st
import pandas as pd
import numpy as np
import time

from model import predict_risk, compute_score, get_shap_values
from db import init_db, save_record
from pdf_report import generate_pdf

init_db()

st.set_page_config(page_title="Mind Balance", layout="wide")

# GLOBAL STYLE
st.markdown("""
<style>
html, body {
    font-family: 'Inter', sans-serif;
    background: #f6f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    font-weight: 700;
    color: #111;
}
</style>
""", unsafe_allow_html=True)

st.title("Mind Balance")
st.caption("Lifestyle-based wellbeing insight tool")
st.caption("This tool estimates your mental health risk based on lifestyle patterns, It is NOT a clinical diagnosis")

st.markdown("---")

# INPUT SECTION
col1, col2, col3, col4 = st.columns(4)

sleep = col1.slider("Sleep (hrs a Day)", 0, 12, 7)
screen = col2.slider("Screen Time (hrs a Day)", 0, 12, 5)
exercise = col3.slider("Exercise (hrs a Week)", 0, 10, 3)
social = col4.slider("Social Time (hrs a Week)", 0, 10, 4)

# RECOMMENDATIONS
def generate_recommendations(data):
    rec = []
    if data["sleep"] < 6:
        rec.append(
            "Your sleep is below the recommended range (7–9 hours). "
            "Poor sleep reduces emotional stability, memory performance, and stress resilience. "
            "Try consistent sleep/wake times and reduce screen exposure 1 hour before bed."
        )
        
    if data["screen"] > 7:
        rec.append(
            "Your screen time is high. Excessive digital exposure can increase mental fatigue and reduce sleep quality. "
            "Introduce screen-free periods, especially in the evening, and use the 20–20–20 eye rule."
        )
        
    if data["exercise"] < 3:
        rec.append(
            "Physical activity is low. Exercise improves dopamine regulation, mood stability, and stress control. "
            "Start with 20–30 minute walks and gradually add light weekly workouts."
        )

    if data["social"] < 3:
        rec.append(
            "Social interaction is limited. Reduced interaction can increase stress sensitivity and isolation. "
            "Try scheduling 2–3 small social moments per week (even short conversations help)."
        )

    if not rec:
        rec.append(
            "Your lifestyle is well balanced. Maintain consistency across sleep, activity, and social engagement. "
            "Small improvements can still enhance long-term wellbeing stability."
        )
    return rec

# MAIN
if st.button("Generate Report"):

    data = {
        "sleep": sleep,
        "screen": screen,
        "exercise": exercise,
        "social": social
    }

    score = compute_score(data)
    risk = predict_risk(data)
    save_record(sleep, screen, exercise, social, risk, score)

    # HEALTH SCORE
    st.markdown("## Health Score")

    color = "#22c55e" if score >= 70 else "#f59e0b" if score >= 40 else "#ef4444"

    placeholder = st.empty()

    # SMOOTH ANIMATION
    for i in range(0, score + 1, 2):
        placeholder.markdown(f"""
        <div style="
            width:260px;
            height:260px;
            border-radius:50%;
            margin:auto;
            background: conic-gradient({color} {i * 3.6}deg, #e5e7eb 0deg);
            display:flex;
            align-items:center;
            justify-content:center;
            box-shadow:0 0 10px {color};
        ">
            <div style="
                width:180px;
                height:180px;
                border-radius:50%;
                background:white;
                display:flex;
                flex-direction:column;
                align-items:center;
                justify-content:center;
                box-shadow:0 8px 20px rgba(0,0,0,0.08);
            ">
                <h1 style="margin:0; font-size:40px; color:#111;">{i}</h1>
                <p style="margin:0; color:#111;">/100</p>
                <b style="color:{color};">{risk} Risk</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.01)

    # PULSE EFFECT
    time.sleep(0.15)

    placeholder.markdown(f"""
    <div style="
        width:260px;
        height:260px;
        border-radius:50%;
        margin:auto;
        background: conic-gradient({color} {score * 3.6}deg, #e5e7eb 0deg);
        display:flex;
        align-items:center;
        justify-content:center;
        box-shadow:0 0 25px {color};
    ">
        <div style="
            width:180px;
            height:180px;
            border-radius:50%;
            background:white;
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            box-shadow:0 8px 20px rgba(0,0,0,0.08);
        ">
            <h1 style="margin:0; font-size:40px; color:#111;">{score}</h1>
            <p style="margin:0; color:#111;">/100</p>
            <b style="color:{color};">{risk} Risk</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # SUMMARY
    st.markdown("## Summary")

    c1, c2 = st.columns(2)
    c1.metric("Health Score", f"{score}/100")
    c2.metric("Risk Level", risk)

    st.markdown("---")

    # RECOMMENDATIONS UPDATED RESULTS
    st.markdown("## Recommendations")

    rec = generate_recommendations(data)
    for r in rec:
        st.info(r)
        
    st.markdown("---")

    # LIFESTYLE BREAKDOWN
    st.markdown("## Lifestyle Breakdown")

    risk_data = {
        "Sleep": max(0, 6 - sleep),
        "Screen Time": screen,
        "Exercise": max(0, 4 - exercise),
        "Social": max(0, 4 - social)
    }

    df_risk = pd.DataFrame(list(risk_data.items()), columns=["Factor", "Risk"])
    st.bar_chart(df_risk.set_index("Factor"))
    st.markdown("---")

    # SHAP
    st.markdown("## Explainability (SHAP Insight)")

    shap_vals = get_shap_values(data)

    shap_clean = {
        k: int(abs(v)) if v is not None else 0
        for k, v in shap_vals.items()
    }

    df_shap = pd.DataFrame({
        "Feature": list(shap_clean.keys()),
        "Impact": list(shap_clean.values())
    })

    st.bar_chart(df_shap.set_index("Feature"))
    st.markdown("---")

    # PDF
    file = generate_pdf(data, score, risk, rec)

    with open(file, "rb") as f:
        st.download_button(
            "Download Report",
            f,
            file_name="mind_balance_report.pdf"
        )