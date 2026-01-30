# Ethiopia Financial Inclusion Forecasting

## Overview
This project aims to forecast financial inclusion in Ethiopia, focusing on **Access (account ownership)** and **Usage (digital payment adoption)**. Using historical Findex data, policy events, and infrastructure data, we build models to predict Ethiopia’s financial inclusion trajectory from 2025–2027 and provide actionable insights for stakeholders.

The project includes:
- Data exploration and enrichment
- Event impact modeling
- Forecasting with scenarios and uncertainty
- An interactive dashboard for stakeholders

---

## Project Structure

ethiopia-fi-forecast/
├── data/
│ ├── raw/ # Original datasets
│ └── processed/ # Cleaned & enriched data
├── notebooks/
│ └── eda_enrichment.ipynb # EDA & data enrichment
├── src/
│ └── init.py
├── dashboard/
│ └── app.py # Streamlit interactive dashboard
├── models/ # Saved model artifacts
├── reports/
│ └── figures/ # Plots and visualizations
├── tests/
│ └── init.py
├── requirements.txt
├── README.md
└── .gitignore


---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd ethiopia-fi-forecast
Set up Python environment:

python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
Install dependencies:

pip install -r requirements.txt
Run the notebook for EDA & enrichment:

Open notebooks/eda_enrichment.ipynb in VS Code or Jupyter.

Execute cells sequentially to explore and enrich the data.

Run the dashboard locally:

streamlit run dashboard/app.py
Open your browser to see interactive visualizations and forecasts.

Data
ethiopia_fi_unified_data.csv — Starter dataset with observations, events, and targets.

reference_codes.csv — Valid values for categorical fields.

data_enrichment_log.md — Documentation of new data added during enrichment.

Features & Capabilities
Data cleaning, enrichment, and exploration

Event impact modeling (policy, product launches, infrastructure)

Forecasting Access and Usage for 2025–2027

Scenario analysis (optimistic, base, pessimistic)

Interactive dashboard with:

Trends & growth rates

Event overlays

Forecasts with confidence intervals

P2P/ATM crossover visualization

Authors
Your Name

References
World Bank Global Findex Database

Telebirr, M-Pesa, EthSwitch, Fayda reports

Additional data sources (IMF FAS, GSMA, ITU, NBE)
