# 📰 TruthLens – AI News Veracity Detector

TruthLens is a web application that uses **Machine Learning** to detect whether a given news article is **REAL** or **FAKE**.

---

## 🚀 Features
- Paste any news headline or article text to check authenticity.
- ML model trained on **Kaggle's Fake & Real News Dataset**.
- Streamlit-based interactive UI.
- Displays prediction and confidence score.

---

## 📂 Project Structure
TruthLens/
│
├── app.py # Streamlit frontend
├── utils/
│ ├── predictor.py # Model loading & prediction
│ └── preprocessing.py # Text cleaning functions
├── model/
│ ├── fake_news_model.pkl # Trained ML model
│ └── vectorizer.pkl # TF-IDF vectorizer
├── data/ # Dataset (ignored in git)
├── requirements.txt # Python dependencies
└── README.md


## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yasickogul/AI-Powered-News-Veracity-Detector
   cd TruthLens
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   streamlit run app.py

📊 Dataset
This project uses the Fake and Real News Dataset.
Dataset link - https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/data

