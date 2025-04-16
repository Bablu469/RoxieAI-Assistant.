document.getElementById("send-btn").addEventListener("click", function() {
  const userInput = document.getElementById("user-input").value;
  if (userInput.trim()) {
      // Display user's message
      const userMessage = document.createElement("p");
      userMessage.textContent = `You: ${userInput}`;
      document.getElementById("chat-box").appendChild(userMessage);
      
      // Clear input
      document.getElementById("user-input").value = "";
      
      // Send message to Flask backend
      fetch("http://127.0.0.1:5000/ask", {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ message: userInput })
      })
      .then(response => response.json())
      .then(data => {
          const assistantMessage = document.createElement("p");
          assistantMessage.textContent = `Roxie: ${data.reply}`;
          document.getElementById("chat-box").appendChild(assistantMessage);
      })
      .catch(error => {
          console.error("Error:", error);
      });
  }
});
