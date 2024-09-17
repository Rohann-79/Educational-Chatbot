function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    let userMessage = document.createElement("p");
    userMessage.textContent = "You: " + userInput;
    chatBox.appendChild(userMessage);

    fetch("/get_response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = document.createElement("p");
        botMessage.textContent = "Bot: " + data.response;
        chatBox.appendChild(botMessage);
    });

    document.getElementById("user-input").value = "";
}
