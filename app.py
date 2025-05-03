import streamlit as st
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk

# Download stopwords once, using Streamlit's caching
@st.cache_resource
def load_stopwords():
    nltk.download('stopwords')
    return stopwords.words('english')

# Load model and vectorizer once
@st.cache_resource
def load_model_and_vectorizer():    
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Define sentiment prediction function
def predict_sentiment(text, model, vectorizer, stop_words):
    # Preprocess text
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stop_words]
    text = ' '.join(text)
    text = [text]
    text = vectorizer.transform(text)
    
    # Predict sentiment
    sentiment = model.predict(text)
    return "Negative" if sentiment == 0 else "Positive"

# Function to create a colored card
def create_card(input_text, sentiment):
    color = "green" if sentiment == "Positive" else "red"
    card_html = f"""
    <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin: 10px 0;">
        <h5 style="color: white;">{sentiment} Sentiment</h5>
        <p style="color: white;">{input_text}</p>
    </div>
    """
    return card_html

# Main app logic
def main():
    st.title("Sentiment Analysis")

    # Load stopwords, model, and vectorizer
    stop_words = load_stopwords()
    model, vectorizer = load_model_and_vectorizer()

    # User input
    text_input = st.text_area("Enter text to analyze sentiment")
    if st.button("Analyze"):
        sentiment = predict_sentiment(text_input, model, vectorizer, stop_words)
        card_html = create_card(text_input, sentiment)
        st.markdown(card_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
