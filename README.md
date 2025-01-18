# Meta LLaMA Chatbot
![Image](https://github.com/user-attachments/assets/83a75365-6f2d-4151-862c-696e2d65dfe4)

A simple chatbot powered by the `meta/meta-llama-3-8b-instruct` model from Replicate. This chatbot is built using Streamlit, which provides an interactive and user-friendly interface to communicate with the LLaMA model.

## Overview

This project allows users to interact with a chatbot powered by the `meta/meta-llama-3-8b-instruct` model via a web-based interface. The chatbot generates human-like responses to user inputs using the LLaMA model hosted on Replicate.

The app allows for real-time conversations, displaying both user and assistant messages in a visually appealing format. It also includes custom CSS for a polished chat interface with a sleek design.

## Features

- **Interactive Chat**: Users can send messages and receive responses from the chatbot.
- **User-Friendly Interface**: The Streamlit app provides a simple and clean design with custom styling for chat bubbles.
- **Powered by Meta LLaMA**: Leverages the `meta/meta-llama-3-8b-instruct` model from Replicate for generating responses.
- **Real-time Conversation History**: The chat history is maintained throughout the session, allowing users to see the entire conversation.

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/meta-llama-chatbot.git
cd meta-llama-chatbot
```

### 2. Install Dependencies

Make sure you have Python 3.7 or above installed. Then, install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set up Replicate API Token

To use the Replicate API, you need to set your Replicate API token. You can obtain an API token from [Replicate](https://replicate.com/account). Once you have the token, set it in your environment or replace `API_TOKEN` in the script.

For environment variable setup:

```bash
export REPLICATE_API_TOKEN="your-api-token"
```

### 4. Run the Streamlit App

After the installation, you can start the app with the following command:

```bash
streamlit run app.py
```

The app should now be accessible at `http://localhost:8501`.

---

## Usage

Once the app is running, open the web interface and you can start interacting with the chatbot by typing your messages in the text input box. The chatbot will respond with a coherent, AI-generated answer using the `meta/meta-llama-3-8b-instruct` model.

### Input Box:
- Type your query or message in the input box labeled "You:".
  
### Chat Interface:
- The conversation history will be displayed with user messages in a distinct style and assistant responses in a different style.

---

## Code Structure

Here’s a brief breakdown of the project structure:

```
/meta-llama-chatbot
├── app.py                   # Main Streamlit app file
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
└── .gitignore               # Git ignore file
```

### `app.py`

- The core application logic is implemented here. It handles user inputs, communicates with the Replicate API, and renders the chat interface.
- The `replicate` Python package is used to call the Meta LLaMA model for generating responses.

### `requirements.txt`

Lists all the Python dependencies required to run the application:

- `streamlit`
- `replicate`

### `README.md`

This file.

---

## Custom Styling

The app uses custom CSS to create a polished chat interface:

```html
<style>
    .user-msg {
        background-color: #D1F7FF;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        margin-left: 0;
        margin-right: auto;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .assistant-msg {
        background-color: #F4F6F9;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        margin-left: auto;
        margin-right: 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }
</style>
```

This provides a chat interface with rounded message bubbles and soft shadow effects.

---

## Contributing

If you would like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Ensure that you follow best practices and provide clear commit messages.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Meta** for developing the LLaMA model.
- **Replicate** for providing the model hosting platform.
- **Streamlit** for building the interactive web interface.
- Open-source libraries such as `spaCy`, `PyTorch`, and `Hugging Face` for NLP.
