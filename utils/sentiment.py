def get_sentiment(text):
    positive_keywords = ["good", "great", "excellent", "amazing", "awesome", "सही", "शानदार"]
    negative_keywords = ["bad", "poor", "worst", "terrible", "flicker", "drain", "खराब", "बेकार"]

    text = text.lower()
    if any(word in text for word in negative_keywords):
        return "negative"
    elif any(word in text for word in positive_keywords):
        return "positive"
    else:
        return "neutral"
