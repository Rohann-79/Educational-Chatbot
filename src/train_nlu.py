import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

def load_data(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
    return data

def prepare_data(data):
    X = []
    y = []
    for intent in data['intents']:
        for pattern in intent['patterns']:
            X.append(pattern)  # Append each pattern as a single string
            y.append(intent['tag'])
    return X, y

def train_nlu(data):
    X, y = prepare_data(data)
    
    # Ensure that X is a list of strings
    print(f"Sample X data: {X[:5]}")  # Print the first 5 samples to verify
    print(f"Sample y data: {y[:5]}")  # Print the first 5 labels to verify

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])

    model.fit(X_train, y_train)
    joblib.dump(model, "/Users/krohann/Desktop/educational-chatbot/models/nlu_model/nlu_model.pkl")

    print(f"Model trained with {model.score(X_test, y_test) * 100:.2f}% accuracy")

if __name__ == "__main__":
    data = load_data("/Users/krohann/Desktop/educational-chatbot/data/intents.json")
    train_nlu(data)
