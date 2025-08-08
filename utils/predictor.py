import joblib
from utils.preprocessing import clean_text

model = joblib.load('model/fake_news_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

def predict_news_veracity(text):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    prediction = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0].max()
    label = 'REAL' if prediction == 1 else 'FAKE'
    return label, prob
