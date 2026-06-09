# Import required libraries
from dotenv import load_dotenv
from itertools import zip_longest

import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# Load environment variables
load_dotenv()

# Set streamlit page configuration
st.set_page_config(page_title="SangamAI - Your Smart Assistant", page_icon="🤖")

# App title and subtitle
st.title("🤖 SangamAI")
st.caption("Your personal AI assistant — ask me anything!")

# Initialize session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI generated responses

if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store past user inputs

if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""  # Store the latest user input

# Initialize the ChatOpenAI model
chat = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo"
)


def build_message_list():
    """
    Build a list of messages including system, human and AI messages.
    """
    # System prompt — defines the chatbot's personality
    zipped_messages = [SystemMessage(
        content="""You are SangamAI, a friendly, smart, and helpful personal assistant created by Sangam Sharma.
        You can help with anything — answering questions, explaining concepts, giving advice, helping with writing,
        solving problems, and much more. Always respond in a clear, helpful, and friendly tone.
        If you don't know the answer to something, be honest and say so instead of making something up.
        Keep responses concise unless the user asks for more detail."""
    )]

    # Zip together the past and generated messages
    for human_msg, ai_msg in zip_longest(st.session_state['past'], st.session_state['generated']):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(content=human_msg))
        if ai_msg is not None:
            zipped_messages.append(AIMessage(content=ai_msg))

    return zipped_messages


def generate_response():
    """
    Generate AI response using the ChatOpenAI model.
    """
    zipped_messages = build_message_list()
    ai_response = chat(zipped_messages)
    return ai_response.content


# Define function to submit user input
def submit():
    st.session_state.entered_prompt = st.session_state.prompt_input
    st.session_state.prompt_input = ""


# Sidebar with info
with st.sidebar:
    st.markdown("## 💡 About SangamAI")
    st.markdown("A general-purpose AI assistant built with:")
    st.markdown("- 🧠 OpenAI GPT-3.5")
    st.markdown("- 🦜 LangChain")
    st.markdown("- ⚡ Streamlit")
    st.markdown("---")
    st.markdown("**Features:**")
    st.markdown("- Remembers conversation history")
    st.markdown("- Answers any question")
    st.markdown("- Friendly & concise responses")
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state['generated'] = []
        st.session_state['past'] = []
        st.session_state['entered_prompt'] = ""

# Chat input
st.text_input('You: ', key='prompt_input', on_change=submit, placeholder="Ask me anything...")

if st.session_state.entered_prompt != "":
    user_query = st.session_state.entered_prompt
    st.session_state.past.append(user_query)
    output = generate_response()
    st.session_state.generated.append(output)

# Display chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

# Footer
st.markdown("""
---
Made with ❤️ by **Sangam Sharma** | Powered by OpenAI & LangChain
""")
