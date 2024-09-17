import joblib

class EducationalChatbot:
    def __init__(self):
        self.nlu_model = joblib.load("/Users/krohann/Desktop/educational-chatbot/models/nlu_model/nlu_model.pkl")
        self.dialogue_model = joblib.load("/Users/krohann/Desktop/educational-chatbot/models/dialogue_model/dialogue_model.pkl")

    def respond(self, text):
        intent = self.nlu_model.predict([text])[0]
        response = self.dialogue_model.get(intent, ["Sorry, I don't understand that."])[0]
        return response

if __name__ == "__main__":
    bot = EducationalChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Bot:", bot.respond(user_input))
