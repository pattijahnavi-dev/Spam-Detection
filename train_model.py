import os
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = [
    "Congratulations! You won a free prize. Claim now",
    "You have won a cash reward. Click here to claim",
    "URGENT! You have been selected for a free gift",
    "Win money now by clicking this link",
    "Free entry in our competition. Call now",
    "You won a lottery prize. Send your details",
    "Get a free voucher today",
    "Claim your bonus now",
    "Limited offer! You can win a free phone",
    "Congratulations, claim your reward immediately",
    "Hi, are we meeting today?",
    "Please submit your assignment tomorrow",
    "Can you call me when you are free?",
    "Your appointment is confirmed for 10 AM",
    "Don't forget to bring your notebook",
    "Happy birthday! Have a great day",
    "Please send me the project file",
    "I will reach home by evening",
    "Are you coming to college today?",
    "Your class starts at 9 AM tomorrow"
]
labels = ["spam"] * 10 + ["ham"] * 10

model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
    ("classifier", MultinomialNB())
])

model.fit(messages, labels)

os.makedirs("model", exist_ok=True)
with open("model/spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully.")
print("Saved as model/spam_model.pkl")
