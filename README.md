# 🌸 Sahridaya Mental Wellness Chatbot 🌸

Welcome to the **Sahridaya Mental Wellness Chatbot** repository! This chatbot is designed with a focus on mental wellness and support, providing users with a comforting and responsive companion on their journey toward better mental health. 🌈✨

---

## 🔥 Key Features

- **Interactive UI** 🌐: The chatbot uses **Streamlit** to deliver a seamless web-based experience.
- **Natural Conversations** 💬: Built with **LangChain** and the **Groq language model**, Sahridaya can maintain meaningful and context-aware conversations.
- **Contextual Memory** 📜: The chatbot’s `ConversationBufferWindowMemory` feature helps it remember recent conversations, making responses more personalized.
- **Customizable Themes** 🎨: Styled with color themes and emojis for an inviting, user-friendly look.

---

## 🛠️ How It Works

1. **User Input**: Users enter their queries through a text input area, and responses are generated in real time.
2. **Language Model**: The chatbot uses a **Groq language model** to generate natural and contextually appropriate responses.
3. **Memory Management**: With **ConversationBufferWindowMemory**, Sahridaya remembers recent interactions, maintaining a smooth flow in ongoing conversations.
4. **Dynamic UI Updates**: Past interactions and new responses are seamlessly displayed in the chat window for easy reference and a consistent experience.

---

## 🤖 About the Model: Mistral (mixtral-8x7b-32768)

This model, based on Transformer architecture, is optimized to generate relevant and coherent responses:

- **Transformer-Based**: Uses self-attention mechanisms to understand context.
- **Decoder-Only**: Focuses on delivering coherent and context-sensitive text.
- **Efficient Memory Usage**: Capable of managing extended conversations with advanced memory management.
- **Adaptable Context**: Supports windowed memory, allowing it to retain essential parts of past interactions.

---

## 🎨 Customizable Sidebar

The chatbot UI includes a sidebar for easy adjustments:

- **Memory Length**: Users can adjust how many previous interactions the chatbot remembers, improving the chat’s relevance and continuity.

---

## 💻 Getting Started

To try out **Sahridaya**, simply clone this repository, install the required packages, and launch the chatbot using **Streamlit**.


## 🌈 Contributing

Contributions are welcome! If you have ideas to enhance Sahridaya or fix any bugs, feel free to fork the repository and submit a pull request.

```bash
# Clone the repository
git clone https://github.com/saisaranya2005/Sahridaya-Chatbot.git

# Navigate to the project directory
cd sahridaya-chatbot

# Install required packages
pip install -r requirements.txt

#Replace the groq api used with your own api key

# Run the chatbot
streamlit run app.py
