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

1.**Clone this repository**
```bash
git clone https://github.com/yourusername/feedback-analyzer.git
cd feedback-analyzer
```
2.**Create a virtual environment**
```
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv/Scripts/activate   # For Windows
```
3.**Install requirements**
```
pip install -r requirements.txt
```
4.**Download FastText Language Model**
- Download lid.176.bin from:
- https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
- Place it inside the utils/ folder.

5.**Run the app**
```
streamlit run app.py
```
---
## Working Video: 
https://drive.google.com/file/d/1lcCKkNEA_R4qSRTsx09kvjcfoo9fqgmY/view?usp=sharing
---
✨ Future Work
- 🎯 Topic modeling using LDA for feedback clustering
- 🤖 Fully trained transformer for multi-lingual sentiment
- 🌐 Deployment on Streamlit Cloud or HuggingFace Spaces
- 📩 Email alerts to sellers for critical feedback
