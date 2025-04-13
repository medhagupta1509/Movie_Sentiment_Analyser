# 🎬 Movie Review Sentiment Analyzer

A simple and interactive web app built using **Streamlit** that predicts whether a movie review is **positive** or **negative** using **Natural Language Processing (NLP)** and **Machine Learning**.

---

## 🚀 Demo

Live App: [Click Here to Try It Out](https://moviesentimentanalyser-4hl6ps2czwbe4qp2w73amc.streamlit.app/)

---

## 📌 Features

- Input a movie review and get real-time sentiment prediction
- Uses **TF-IDF** vectorization for text processing
- Trained with a **Logistic Regression** model
- Fully deployed using **Streamlit Cloud**
- Clean and responsive UI

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- NLP (TfidfVectorizer)
- Pickle (for saving/loading model)

---

## 🧠 How it Works

1. **Preprocess the movie reviews dataset**
2. **Train** a Logistic Regression model on vectorized text data
3. **Save the model** and **vectorizer** using `pickle`
4. **Load them** in a Streamlit web app
5. **Predict** sentiment when user inputs a review



