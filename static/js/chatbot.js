document.addEventListener("DOMContentLoaded", function () {
    let chatbotButton = document.querySelector(".chatbot-button");
    let chatbotBox = document.querySelector(".chatbot-box");
    let chatbotMessages = document.querySelector(".chatbot-messages");
    let chatbotInput = document.getElementById("chatbot-input");
    let closeChat = document.getElementById("close-chat");

    chatbotButton.addEventListener("click", () => chatbotBox.classList.toggle("active"));
    closeChat.addEventListener("click", () => chatbotBox.classList.remove("active"));

    chatbotInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            let userMessage = chatbotInput.value.trim();
            if (userMessage) {
                addMessage("user", userMessage);
                chatbotInput.value = "";

                
                fetch("/chatbot", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message: userMessage })
                })
                .then(response => response.json())
                .then(data => {
                    addMessage("bot", data.response);
                })
                .catch(error => {
                    console.error("Error:", error);
                    addMessage("bot", "❌ Error: Unable to fetch response.");
                });
            }
        }
    });

    function addMessage(sender, message) {
        let messageElement = document.createElement("p");
        messageElement.classList.add(sender === "user" ? "user-message" : "bot-message");
        messageElement.innerHTML = message;
        chatbotMessages.appendChild(messageElement);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }
});
