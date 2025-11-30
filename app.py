import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)


nltk.download('punkt')
nltk.download('stopwords')
import nltk
import os


nltk_data_dir = os.path.expanduser("~/.nltk_data")
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)


nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('stopwords', download_dir=nltk_data_dir)

nltk.data.path.append(nltk_data_dir)



ps = PorterStemmer()
#by Dhruv Sarin

# Text transformationfunction
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Spam Classifier",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS for advanced styling
st.markdown("""
    <style>
    /* Navbar styling */
    .navbar {
        background-color: #007bff;
        padding: 10px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        color: white;
        text-align: center;
    }

    .navbar h2 {
        margin: 0;
        color: white;
    }

    /* Sidebar styling */
    .css-18e3th9 {
        background-color: #f4f4f9;
        padding: 20px;
        border-right: 2px solid #eee;
    }

    /* Main content styling */
    .main {
        background-color: #fff;
        padding: 20px;  /* Reduced padding */
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        max-width: 900px;
        margin: auto;
        margin-top: 10px; /* Reduced margin-top */
    }

    /* Custom button styling */
    button {
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    button:hover {
        background-color: #0056b3;
    }

    /* Custom alert styling */
    .stAlert {
        font-size: 20px;
        font-weight: bold;
        color: white;
        background-color: #28a745;
        border-radius: 5px;
        padding: 20px;
    }
    .stAlert:has(h1:contains("Spam")) {
        background-color: #dc3545;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
    <div class="navbar">
        <h2>📧 Email/SMS Spam Classifier</h2>
    </div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Go to", ["Spam Classifier", "About", "Contact"])

# Main Content Logic
if page == "Spam Classifier":
    st.write("<div class='main'>", unsafe_allow_html=True)

    st.title("Spam Classifier")

    st.write("""
    Enter a message below to check if it is classified as spam or not.
    """)

    input_sms = st.text_area("Enter the message", height=150)

    if st.button('📬 Predict'):
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)
        # 2. Vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. Predict
        result = model.predict(vector_input)[0]

        # 4. Display Result
        if result == 1:
            st.error("🚫 Spam")
        else:
            st.success("✅ Not Spam")

    st.write("</div>", unsafe_allow_html=True)

elif page == "About":
    st.write("<div class='main'>", unsafe_allow_html=True)
    st.title("About This App")
    st.write("""
    This app allows you to classify emails and SMS as spam or not spam using a machine learning model trained on text data.

    **Technologies Used:**
    - Streamlit for the UI
    - Scikit-learn for machine learning
    - Natural Language Processing (NLP) techniques like stemming and tokenization
    """)
    st.write("</div>", unsafe_allow_html=True)

elif page == "Contact":
    st.write("<div class='main'>", unsafe_allow_html=True)
    st.title("Contact Us")
    st.write("""
    If you have any questions or want to collaborate, feel free to reach out at:

    - **Email:** dhruvsarin21@gmail.com
    - **LinkedIn:** (https://www.linkedin.com/in/dhruv-sarin-b97666286/)
    """)

    st.write("</div>", unsafe_allow_html=True)
