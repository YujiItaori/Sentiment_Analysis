# Sentiment Analysis Web App

This is a simple **Sentiment Analysis** project built using **machine learning**. The application takes user input and classifies it as **Positive** or **Negative** sentiment based on a pre-trained model.

> 🔍 Originally designed for Twitter sentiment analysis, this version accepts direct text input and works independently of Twitter or external APIs.

---

## 🚀 Features

- ✅ Input your own text and get sentiment prediction
- ✅ Preprocessed using NLP (stopword removal, lowercasing, etc.)
- ✅ Uses a pre-trained ML model with `TfidfVectorizer`
- ✅ Built using Python and [Streamlit](https://streamlit.io/) (can also be adapted to Django)

---

## 🧠 Machine Learning

- **Model**: Trained on a labeled dataset (e.g., tweets or reviews)
- **Vectorization**: `TfidfVectorizer`
- **Classification**: Model loaded from `model.pkl`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pickle

---

## 📂 Project Structure

```bash
Sentiment_Analysis/
│
├── app.py                 # Main application code
├── model.pkl              # Trained ML model
├── vectorizer.pkl         # TF-IDF vectorizer used during training
├── requirements.txt       # Python dependencies
├── README.md              # You're here!
└── (Optional) dataset.csv # Not pushed due to GitHub size limits but added as a zip file
