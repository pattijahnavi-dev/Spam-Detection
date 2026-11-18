import streamlit as st
import pickle
import os

# Page configuration
st.set_page_config(
    page_title="Spam Detection",
    page_icon="🛡️",
    layout="centered"
)

# Sunset Orange theme
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1b1020, #39202b);
    color: white;
}
h1, h2, h3 {
    color: #FF914D !important;
}
.stButton > button {
    background-color: #FF914D;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 12px 25px;
    font-weight: bold;
}
.stButton > button:hover {
    background-color: #FF6B35;
    color: white;
}
textarea {
    border: 2px solid #FF914D !important;
}
</style>
""", unsafe_allow_html=True)

# Load trained model
@st.cache_resource
def load_model():
    with open("spam_model.pkl", "rb") as f:
        return pickle.load(f)

st.title("🛡️ Spam Detection System")
st.write("Detect spam messages instantly using Machine Learning.")

try:
    model = load_model()

    message = st.text_area(
        "Enter your message",
        placeholder="Type or paste your message here..."
    )

    if st.button("Check Message"):
        if message.strip():
            prediction = model.predict([message])[0]

            if prediction == "spam":
                st.error("⚠️ SPAM MESSAGE DETECTED!")
            else:
                st.success("✅ THIS IS A SAFE MESSAGE!")

        else:
            st.warning("Please enter a message.")

except FileNotFoundError:
    st.error("Model file not found. Check model/spam_model.pkl in GitHub.")
except Exception as e:
    st.error(f"Application error: {e}")

st.markdown("---")
st.caption("Powered by Machine Learning | Spam Detection Project")
