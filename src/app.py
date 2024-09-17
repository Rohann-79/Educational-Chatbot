from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
bot = joblib.load("../models/dialogue_model/dialogue_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = bot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
