 Email/SMS Spam Classifier

This is a Machine Learning based web application that classifies emails and SMS messages as either Spam or Not Spam using Natural Language Processing (NLP) techniques.
 Features
Interactive UI using Streamlit
Preprocessing of text with NLTK (Tokenization, Stopword Removal, and Stemming)
TF-IDF Vectorization for text representation
Machine Learning Model using Scikit-Learn
Deployed-ready with a Procfile and setup.sh script

 Tech Stack
Python
Streamlit (For UI)
NLTK (For NLP processing)
Scikit-learn (For ML Model)
Pickle (For model serialization)

📂 Project Structure
├── app.py               # Main application script
├── model.pkl            # Trained ML model
├── vectorizer.pkl       # TF-IDF Vectorizer
├── requirements.txt     # Dependencies
├── setup.sh             # Setup script for Streamlit
├── Procfile             # Deployment configuration
├── nltk.txt             # NLTK data requirements
└── README.md            # Project documentation

 How to Run
Clone the Repository:
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier
Create a Virtual Environment (Optional but Recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt
Run the Application:
streamlit run app.py

Open the browser and navigate to the localhost URL provided.
🚀 Deployment
This app is ready for deployment on platforms like Heroku or Streamlit Sharing.
Deploy on Heroku
Install Heroku CLI
Login to Heroku:
heroku login

Create a Heroku App:
heroku create your-app-name
Push to Heroku:
git add .
git commit -m "Initial commit"
git push heroku main

📞 Contact
Author: Dhruv Sarin
Email: dhruvsarin21@gmail.com
