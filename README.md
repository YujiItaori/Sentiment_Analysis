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
```

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-webapp.git
   cd sentiment-analysis-webapp
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

---

## 🎯 Usage

1. Launch the application
2. Enter your text in the input field
3. Click "Analyze Sentiment"
4. View the prediction result (Positive/Negative)

---

## 📊 Model Performance

The model has been trained and tested on a comprehensive dataset with the following performance metrics:

- **Accuracy**: ~85%
- **Precision**: High for both positive and negative classes
- **Recall**: Balanced across sentiment categories

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to the open-source community for providing excellent tools and libraries
- Special thanks to contributors who helped improve this project

---

⭐ Star this repository if you find it helpful! ⭐

*"The best way to predict the future is to create it."* - Peter Drucker
