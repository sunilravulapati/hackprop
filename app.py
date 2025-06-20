import streamlit as st
import pandas as pd
from utils.language import detect_language
from utils.sentiment import get_sentiment
from utils.features import extract_features
import plotly.express as px

st.set_page_config(page_title="Multilingual Feedback Analyzer", layout="wide")
st.title("Multilingual Customer Feedback Dashboard")

#process  raw csv
with st.expander("📂 Upload Raw CSV (Preprocess it into Our Format)"):
    raw_file = st.file_uploader("Upload your raw CSV", type="csv", key="raw_csv")

    if raw_file:
        raw_df = pd.read_csv(raw_file)
        st.write("### Raw Data Preview")
        st.dataframe(raw_df)

        st.markdown("**💡 Instructions:**")
        st.markdown("- Select the column that contains the review text")
        st.markdown("- If you don't have a product column, leave it as 'None'. Reviews will be tagged as 'Unknown Product'")

        review_col = st.selectbox("Select column containing reviews", raw_df.columns)
        product_col = st.selectbox("Select column containing product name (optional)", ["None"] + list(raw_df.columns))

        if st.button("✅ Format CSV"):
            clean_df = pd.DataFrame()
            clean_df["review"] = raw_df[review_col]

            if product_col != "None":
                clean_df["product"] = raw_df[product_col]
            else:
                clean_df["product"] = "Unknown Product"

            st.success("✅ CSV formatted successfully!")
            st.dataframe(clean_df)

            formatted_csv = clean_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Formatted CSV", formatted_csv, "formatted_reviews.csv", "text/csv")

st.markdown("---")
#actual
uploaded_file = st.file_uploader("📤 Upload Review CSV for Analysis", type="csv", key="main_csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 📄 Uploaded Reviews")
    st.dataframe(df)

    # Ensure required columns exist
    if "review" not in df.columns:
        st.error("❌ 'review' column not found in your uploaded file. Please check your formatting.")
    else:
        if "product" not in df.columns:
            st.warning("⚠️ 'product' column not found. Tagging all reviews as 'Unknown Product'.")
            df["product"] = "Unknown Product"
        #Language Detection
        st.write("### 🌍 Language Detection")
        df["language"] = df["review"].apply(detect_language)
        lang_counts = df["language"].value_counts()
        st.bar_chart(lang_counts)
        #sentiment analysis
        st.write("### 😊 Sentiment Analysis (Offline)")
        df["sentiment"] = df["review"].apply(get_sentiment)
        st.plotly_chart(px.pie(df, names="sentiment", title="Sentiment Distribution"))

        #extraction of features
        st.write("### 🔍 Extraction of Features")
        df["features"] = df["review"].apply(extract_features)
        st.dataframe(df[["review", "product", "features", "sentiment"]])
        #Alerts
        negative_count = df[df["sentiment"] == "negative"].shape[0]
        if negative_count / len(df) > 0.3:
            st.error("⚠️ High amount of negative sentiment detected!")
        else:
            st.success("✅ Sentiment trend looks healthy.")
        #Export!    
        csv_output = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Analysis Report", csv_output, "analyzed_reviews.csv", "text/csv")