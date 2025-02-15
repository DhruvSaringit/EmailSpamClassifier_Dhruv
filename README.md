# Email/SMS Spam Classifier

This is a Machine Learning-based web application that classifies emails and SMS messages as either **Spam** or **Not Spam** using **Natural Language Processing (NLP)** techniques.

## Features
- 📌 **Interactive UI** using Streamlit
- 🔍 **Preprocessing** of text with NLTK (Tokenization, Stopword Removal, and Stemming)
- 📝 **TF-IDF Vectorization** for text representation
- 🤖 **Machine Learning Model** using Scikit-Learn
- 🚀 **Deployment-Ready** with a Procfile and setup.sh script

---

## Tech Stack
- **Python** (Backend)
- **Streamlit** (UI Framework)
- **NLTK** (NLP processing)
- **Scikit-learn** (Machine Learning)
- **Pickle** (Model Serialization)

---

## 📂 Project Structure
```
📂 Project Structure
├── app.py               # Main application script
├── model.pkl            # Trained ML model
├── vectorizer.pkl       # TF-IDF Vectorizer
├── requirements.txt     # Dependencies
├── setup.sh             # Setup script for Streamlit
├── Procfile             # Deployment configuration
├── nltk.txt             # NLTK data requirements
├── README.md            # Project documentation
```

---

## 🚀 How to Run
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier
```
### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 🌐 Deployment
This app is ready for deployment on platforms like **Heroku** or **Streamlit Sharing**.
### Deploy on Heroku:
```bash
# Install Heroku CLI
heroku login

# Create a Heroku App
heroku create your-app-name

# Push to Heroku
git add .
git commit -m "Initial commit"
git push heroku main
```

---

## 📩 Contact
📧 **Author:** Dhruv Sarin  
📬 **Email:** dhruvsarin21@gmail.com


