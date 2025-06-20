# 🧠 Multilingual Customer Feedback Analyzer

A lightweight, AI-powered Streamlit app that analyzes customer reviews across multiple languages — detecting sentiment, extracting key product features, and prioritizing critical issues for sellers and product teams.

---

## 🚀 Key Features

- 🌐 **Language Detection** (Offline) — Powered by FastText to support 170+ languages.
- 😊 **Sentiment Analysis** (Offline) — Keyword-based model for fully offline scoring.
- 🛠 **Feature Extraction** — Uses YAKE to identify key product issues in feedback.
- ⚠️ **Priority Tagging** — Classifies reviews as 🔴 Critical / 🔥 High / ⚠️ Medium / ✅ Low.
- 🛍 **Product + Platform Analysis** — Flags product issues from Amazon, Flipkart, etc.
- 📈 **Trend Graphs** — Visualize rise in negative sentiment over time.
- 🌍 **Language-Based Insights** — Alerts when certain issues spike in regional feedback.

---

## 🧩 Tech Stack

| Component       | Tool/Library             |
|----------------|--------------------------|
| Frontend       | Streamlit                |
| Language ID    | Facebook FastText        |
| Sentiment      | Custom keyword matcher   |
| Feature Extraction | YAKE (unsupervised NLP) |
| Visualizations | Plotly + Streamlit native |
| File Handling  | CSV / JSON / Streamlit UI |

---

## 🧪 How to Run Locally

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/feedback-analyzer.git
cd feedback-analyzer
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\\Scripts\\activate   # For Windows
Install requirements

bash
Copy
Edit
pip install -r requirements.txt
Download FastText Language Model
Download lid.176.bin from:
https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
Place it inside the utils/ folder.

Run the app

bash
Copy
Edit
streamlit run app.py
📊 Demo Wireframe
mathematica
Copy
Edit
+--------------------------------------------------------+
| Product Summary                                        |
| Product A  | Total Reviews: 1532 | Positive: 78%       |
+--------------------------------------------------------+
| 📊 Sentiment Over Time                                 |
| [Graph showing daily/weekly sentiment trends]          |
+--------------------------------------------------------+
| 🛠 Feature-Level Breakdown                             |
| Feature   | Positive | Negative | Neutral | Trend      |
| Battery   |   80%    |   15%    |   5%    | ↓          |
+--------------------------------------------------------+
| 🌍 Language Stats & Alerts                             |
| Hindi: 30% | English: 50% | Tamil: 20%                 |
| 🔔 Alert: Battery complaints rising in Hindi reviews   |
+--------------------------------------------------------+
✨ Future Work
🎯 Topic modeling using LDA for feedback clustering

🤖 Fully trained transformer for multi-lingual sentiment

🌐 Deployment on Streamlit Cloud or HuggingFace Spaces

📩 Email alerts to sellers for critical feedback
