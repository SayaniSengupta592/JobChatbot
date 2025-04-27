function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    if (!userInput.trim()) return;

    displayMessage(userInput, "user");
    document.getElementById("userInput").value = "";

    // Show "Bot is typing..." indicator
    const typingIndicator = document.createElement("div");
    typingIndicator.id = "typingIndicator";
    typingIndicator.className = "bot-message";
    typingIndicator.textContent = "Bot is typing...";
    document.getElementById("chatbox").appendChild(typingIndicator);

    fetch("/get", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Remove typing indicator and show response
        const indicator = document.getElementById("typingIndicator");
        if (indicator) indicator.remove();
        displayMessage(data.reply, "bot");
    })
    .catch(error => {
        console.error("Error:", error);
        displayMessage("Sorry, I'm having trouble responding.", "bot");
    });
}

function displayMessage(message, sender) {
    const chatbox = document.getElementById("chatbox");
    const messageDiv = document.createElement("div");
    messageDiv.className = ${sender}-message;
    messageDiv.textContent = message;
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Allow sending messages with Enter key
document.getElementById("userInput").addEventListener("keyup", (e) => {
    if (e.key === "Enter") sendMessage();
})
