import fasttext
import os

model_path = "lid.176.bin" 
if not os.path.exists(model_path):
    raise FileNotFoundError("🚨 'lid.176.bin' not found. Please place it in your project root directory.")

model = fasttext.load_model(model_path)

def detect_language(text):
    if not isinstance(text, str) or text.strip() == "":
        return "unknown"

    prediction = model.predict(text.strip().replace('\n', ' '))[0][0]
    lang_code = prediction.replace('__label__', '')
    return lang_code
