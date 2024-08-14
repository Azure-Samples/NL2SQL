import streamlit as st  
from src.api.api_client import APIClient
import os

def table_to_markdown(table):
    if not table:
        return ""
    
    headers = table[0].keys()
    table_md = "| " + " | ".join(headers) + " |\n"
    table_md += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in table:
        table_md += "| " + " | ".join(str(value) for value in row.values()) + " |\n"
    return table_md


# Initialize the API client
api_client = APIClient(os.environ.get("API_URL"), os.environ.get("API_KEY"))


# Custom CSS to match the style  
st.set_page_config(page_title="DBCopilot", page_icon="📊")
st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)
st.title("DBCopilot")  
st.subheader("DBCopilot, your copilot for structured databases.")

# Create a clickable text to show additional questions. Make them two
# columns to make it look better.
# should hide if clicked again

# Initialize session state for button click if not already initialized
if 'show_questions' not in st.session_state:
    st.session_state.show_questions = False

# Toggle the state when the button is clicked
if st.button("📊[Click to show suggested questions](#)"):
    st.session_state.show_questions = not st.session_state.show_questions

# Show or hide the questions based on the state
if st.session_state.show_questions:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("1. Who are my top 3 suppliers for the uBEs category?")
    with col2:
        st.markdown("2. Who are my top 3 suppliers for the uBEs category?")


# Initialize session state messages if not already initialized
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Chat-like interface for user question  
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        query, table = api_client.parse_response(msg["content"]) 
        with st.chat_message("assistant"):
            st.html("<span class='chat-assistant'></span>")
            st.code(query, language='sql')

        with st.chat_message("assistant"):
            st.html("<span class='chat-assistant'></span>")
            if table:
                table_md = table_to_markdown(table)
                st.markdown(table_md)

#  Gwet user query and get response from the API
user_query = st.chat_input(placeholder="Ask me anything!")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):
        response = api_client.get_response(user_query, chat_history=st.session_state.messages) 
        st.session_state.messages.append({"role": "assistant", "content": response["content"]})
        query, table = api_client.parse_response(response["content"]) 
        st.html("<span class='chat-assistant'></span>")
        st.code(query, language='sql')

    with st.chat_message("assistant"):
        st.html("<span class='chat-assistant'></span>")
        if table:
            table_md = table_to_markdown(table)
            st.markdown(table_md)
     