import replicate
import streamlit as st

# Set your Replicate API token

client = replicate.Client(api_token=API_TOKEN)

st.title("Meta LLaMA Chatbot")
st.write("A chatbot powered by the `meta/meta-llama-3-8b-instruct` model from Replicate.")

# Custom CSS for a professional chat interface
st.markdown("""
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
""", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    # First append the user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.spinner("Generating response..."):
        try:
            prompt_template = (
                "You are a helpful assistant.\n"
                "User: {user_input}\n"
                "Assistant:"
            )
            prompt = prompt_template.format(user_input=user_input)
            output = client.run(
                "meta/meta-llama-3-8b-instruct",
                input={
                    "prompt": prompt,
                    "top_p": 0.95,
                    "temperature": 0.7,
                    "length_penalty": 1,
                    "max_new_tokens": 150,
                    "stop_sequences": "<|end_of_text|>,<|eot_id|>",
                },
            )
            # Combine the fragments into a single coherent response
            response_text = ''.join(output).strip() if isinstance(output, list) else "No response generated."
            # Then append the assistant's response
            st.session_state.chat_history.append({"role": "assistant", "content": response_text})
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display chat history with custom styles
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="user-msg">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-msg">{message["content"]}</div>', unsafe_allow_html=True)
