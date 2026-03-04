# AI Ethical Dilemma Resolver

A SaaS application to analyze corporate ethical dilemmas using AI technologies.

## Tech Stack
- **Frontend**: Streamlit
- **NLP**: SpaCy (en_core_web_sm)
- **ML**: PyTorch (Neural Network for Risk Prediction)
- **Recommendations**: Scikit-Learn (KMeans Clustering)
- **Reporting**: ReportLab (PDF Generation)

## Setup

1. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

3. **Run Application:**
   ```bash
   streamlit run app.py
   ```

## Features
- **Analyze Dilemma**: Input text and values to get risk analysis.
- **Debate Simulation**: View simulated arguments from AI agents.
- **Reports**: Download PDF summary of the analysis.

## Project Structure
- `app.py`: Main application entry point.
- `modules/`: Contains logic for NLP, ML, Debate, Recommendations, and Reporting.
- `data/`: Contains dataset (synthetic).
