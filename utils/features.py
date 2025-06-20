import yake

kw_extractor = yake.KeywordExtractor(lan="en", n=1, top=3)

def extract_features(text):
    try:
        keywords = kw_extractor.extract_keywords(text)
        return ", ".join([kw[0] for kw in keywords])
    except:
        return "unknown"
