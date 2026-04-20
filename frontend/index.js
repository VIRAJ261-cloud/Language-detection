const button = document.getElementById("predictBtn");
const textInput = document.getElementById("textInput");
const result = document.getElementById("result");

button.addEventListener("click", async () => {
  const text = textInput.value;

  if (text.trim() === "") {
    result.innerText = "Please enter some text.";
    return;
  }

  try {
    // Change URL to your FastAPI endpoint
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        text: text,
      }),
    });

    const data = await response.json();

    result.innerText = "Prediction: " + data.Language;
  } catch (error) {
    result.innerText = "Error connecting to server.";

    console.error(error);
  }
});
