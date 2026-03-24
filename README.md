# 🏢 AI Company Verification System

Welcome to the **AI Company Verification System**, an enterprise-grade AI-powered web application built to accurately trace, analyze, and verify businesses and corporate entities. Built natively using Streamlit, this sophisticated platform provides rapid data analysis, AI fuzzy-matching, dynamic originality metrics, and highly interactive analytic dashboards.

---

## ✨ Core Features

1. **🔐 Secure Authentication Gateway**
   - Protected routing that enforces authentication before granting access to internal analytics and verification tools.
   - Beautiful, glassmorphic login interface supporting global Gmail authentication.

2. **🤖 AI Welcome Chatbot**
   - Built-in intelligent Help Bot capable of answering user queries.
   - Guides users fluidly through the Verification metrics, Dashboard analytics, and Industry Categories.

3. **🛡️ Deep Verification Engine (`pages/2_verification.py`)**
   - **Company Name & URL Matcher:** Search any business name or web domain to instantly verify its existence.
   - **Fuzzy AI Matching & Originality Score:** Automatically calculates an `Originality Percentage` reflecting the likelihood of a business being authentic based on ratings, reviews, and web footprints.
   - **Similar Name Detection:** Uses `rapidfuzz` algorithms to catch identically named replica businesses.

4. **📊 Interactive Data Explorer (`pages/3_dashboard.py`)**
   - Visually stunning Plotly analytic distributions showing global company ratings, total dataset frauds, and top business locations.
   - Powerful interactive filter system allowing deep-dives into specific location metrics, instantly loading matching dynamic Company Cards.

5. **🗂️ Visual Business Categories (`pages/4_categories.py`)**
   - An intuitive, visual grid representing the dataset's top industries (e.g., IT Services, Health Care, Construction, Retail).
   - Generates simulated company metadata (Founders, Phone numbers, Avatars) via highly styled dynamic UI cards.

---

## 🛠️ Technology Stack

- **Frontend / Framework:** Streamlit (`v1.x`)
- **Data Engineering:** Pandas (`pd`)
- **Visual Analytics:** Plotly Express (`px`)
- **AI Matching Algorithms:** RapidFuzz (`process`)
- **UI Integrations:** ui-avatars API, Unsplash Architecture

---

## 📁 Project Structure

```bash
AI_Company_Verification_System/
│
├── app.py                      # Main entry point (Auth, Welcome, & Chatbot flow)
├── requirements.txt            # Python dependencies
├── README.md                   # System Documentation
│
├── data/                       
│   └── final_dataset.csv       # Core company dataset containing logic markers
│
├── pages/                      # Auto-loaded by Streamlit framework
│   ├── 2_verification.py       # Security lookup and original scoring algorithms
│   ├── 3_dashboard.py          # Interactive global analytic metric charts
│   └── 4_categories.py         # Visual industry explorer layout
│
├── utils/                      # Helper libraries
│   ├── ui.py                   # Dynamic Google-like Company Card Renderer component
│   └── verify.py               # Algorithmic fuzz-matching and scoring logic engine
│
└── assets/                     
    ├── bg.jpg                  # Standard application background
    └── categories/             # Locally generated UI placeholder visuals
```

---

## 🚀 How to Run Locally

### 1. Prerequisites
Make sure you have Python 3.9+ installed on your machine.

### 2. Install Dependencies
Open your terminal in the main project folder and install the required modules:
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
Start the Streamlit runtime environment using the following command:
```bash
python -m streamlit run app.py
```

### 4. Application Login
When your browser opens the local server link (typically `http://localhost:8501`):
* Use any valid `@gmail.com` address.
* Type any standard password (must not be empty).
* Click **Secure Login** to access the entire system!
