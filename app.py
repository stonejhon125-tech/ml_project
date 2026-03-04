import streamlit as st
import pandas as pd
import torch
import time
import os
from modules.nlp_analyzer import analyze_text
from modules.ml_model import EthicalModel, predict_outcome, train_model
from modules.recommender import RecommenderSystem
from modules.debate import DebateSimulator
from modules.reporting import generate_pdf_report
from utils.helpers import get_risk_color, generate_financial_impact

st.set_page_config(page_title="Ethical Dilemma Resolver", layout="wide")

# Initialize modules
@st.cache_resource
def load_recommender():
    return RecommenderSystem()

recommender = load_recommender()

@st.cache_resource
def load_ml_model():
    # Simple setup: 3 input features (sentiment, length, num_entities) -> 1 output (risk)
    model = EthicalModel(3, 10, 1)
    # Mock training for demo
    dummy_X = torch.rand(10, 3)
    dummy_y = torch.rand(10)
    train_model(model, dummy_X, dummy_y, epochs=10)
    return model

model = load_ml_model()

def main():
    st.title("⚖️ AI Ethical Dilemma Resolver")
    st.markdown("### AI-Powered Analysis for Corporate Ethics")
    
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ["Home", "Analyze Dilemma"])

    if options == "Home":
        st.info("Welcome! Select 'Analyze Dilemma' to start.")
        st.markdown("""
        **Features:**
        - 🧠 **NLP Analysis**: Extracts key entities and keywords.
        - 🤖 **Neural Network**: Predicts risk scores.
        - 💬 **Debate Simulation**: AI agents argue Pros & Cons.
        - 📊 **Recommendations**: Based on past case clusters.
        - 📄 **PDF Reporting**: Downloadable summaries.
        """)

    elif options == "Analyze Dilemma":
        st.header("Analyze a New Ethical Dilemma")
        
        with st.form("dilemma_form"):
            dilemma_text = st.text_area("Describe the Dilemma", height=150, help="E.g., Should we use AI for targeted ads?")
            company_values = st.text_input("Company Values (comma-separated)", help="E.g., Trust, Privacy, Innovation")
            submitted = st.form_submit_button("Analyze Dilemma")

        if submitted and dilemma_text:
            with st.spinner("Analyzing text and extracting entities..."):
                analysis = analyze_text(dilemma_text)
                time.sleep(1) # Logic simulation
            
            with st.spinner("Running Neural Network Simulation..."):
                # Mock features: len(text)/1000, len(entities), value_match_score (random)
                features = torch.tensor([len(dilemma_text)/1000.0, len(analysis['entities']), 0.5]).float()
                risk_score = predict_outcome(model, features) * 100
                financial_impact = generate_financial_impact()
            
            with st.spinner("Simulating Multi-Agent Debate..."):
                debate = DebateSimulator(dilemma_text, company_values)
                debate_log = debate.run_debate()
            
            with st.spinner("Generating Recommendations..."):
                recs = recommender.recommend(dilemma_text)

            # --- Display Results ---
            st.success("Analysis Complete!")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Ethical Risk Score", f"{risk_score:.1f}%", delta_color="inverse")
            col2.metric("Projected Financial Impact", f"${financial_impact:,}")
            col3.metric("Ethical Outcome", "Review Required" if risk_score > 50 else "Likely Positive")

            st.divider()
            
            c1, c2 = st.columns(2)
            
            with c1:
                st.subheader("🔍 NLP Analysis")
                st.write("**Entities Identified:**")
                st.json(analysis['entities'])
                st.write("**Keywords:**", ", ".join(analysis['keywords']))
                
            with c2:
                st.subheader("🤖 AI Debate Simulation")
                for log in debate_log:
                    if "PRO" in log:
                        st.success(log)
                    else:
                        st.error(log)

            st.subheader("💡 Recommendations")
            for r in recs:
                st.info(f"Suggestion: {r}")

            # Reporting
            st.divider()
            if st.button("Generate PDF Report"):
                pdf_file = generate_pdf_report(dilemma_text, analysis, debate_log, risk_score, recs)
                with open(pdf_file, "rb") as f:
                    st.download_button("Download Report", f, file_name="Ethical_Report.pdf")

if __name__ == "__main__":
    main()
