import json
import joblib

def load_data(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
    return data

def train_dialogue(data):
    # Dummy model, replace with advanced dialogue model
    model = {intent['tag']: intent['responses'] for intent in data['intents']}
    joblib.dump(model, "/Users/krohann/Desktop/educational-chatbot/models/dialogue_model/dialogue_model.pkl")

if __name__ == "__main__":
    data = load_data("/Users/krohann/Desktop/educational-chatbot/data/intents.json")
    train_dialogue(data)
