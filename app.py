import streamlit as st
import random
import json
import os
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

# Hard-coded API key
GROQ_API_KEY = 'REPLACE WITH YOUR OWN API'

# Setting up colors and emojis
EMOJIS = ["😊", "💬", "🌻", "💪", "💖", "🌈", "✨", "🌞", "🧘", "💭", "🌸", "🌿"]
HEADER_COLOR = "#ffb6c1"
BG_COLOR = "#000000"

# File path for chat history
CHAT_HISTORY_FILE = "chatfile.json"

# Load chat history from file
def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                # Return an empty list if the file is empty or contains invalid JSON
                return []
    return []

# Save chat history to file
def save_chat_history(chat_history):
    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(chat_history, file)

# Main function
def main():
    st.markdown(
        f"<h1 style='text-align: center; color: {HEADER_COLOR};'>🌸Sahridaya MentalWellness Chatbot🌸</h1>",
        unsafe_allow_html=True
    )

    st.markdown(f"<div style='background-color: {BG_COLOR}; padding: 15px; border-radius: 10px;'>"
                f"<p style='text-align: center; font-size: 20px;'>💖 Hi! I'm Sahridaya, here to help you on your wellness journey! 💖</p></div>",
                unsafe_allow_html=True)
    
    # Sidebar settings for user customization
    st.sidebar.title('Customize Your Chat ✨')
    model = st.sidebar.selectbox('Choose a model:', ['mixtral-8x7b-32768'])
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)
    
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    # Load chat history from file
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = load_chat_history()
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

    # Text area for user question
    user_question = st.text_area("💬 How can I assist you today?")

    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=model)
    conversation = ConversationChain(llm=groq_chat, memory=memory)

    # Processing user input
    if user_question:
        response = conversation(user_question)
        message = {'human': user_question, 'AI': response['response']}
        st.session_state.chat_history.append(message)
        save_chat_history(st.session_state.chat_history)  # Save chat history to file

        st.markdown(
            f"<div style='background-color: {BG_COLOR}; padding: 10px; border-radius: 10px; margin: 10px;'>"
            f"<p><strong>You {random.choice(EMOJIS)}:</strong> {user_question}</p>"
            f"<p><strong>Sahridaya {random.choice(EMOJIS)}:</strong> {response['response']}</p></div>",
            unsafe_allow_html=True
        )

    # Display previous conversation history
    st.markdown("<h3 style='color: #ffffff;'>Previous Conversations 🌸</h3>", unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        st.markdown(
            f"<div style='background-color: {BG_COLOR}; padding: 8px; border-radius: 8px; margin: 8px;'>"
            f"<p><strong>You {random.choice(EMOJIS)}:</strong> {message['human']}</p>"
            f"<p><strong>Sahridaya {random.choice(EMOJIS)}:</strong> {message['AI']}</p></div>",
            unsafe_allow_html=True
        )

# Run the main function
if __name__ == "__main__":
    main()
