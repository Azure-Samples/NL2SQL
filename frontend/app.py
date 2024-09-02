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


# Queries to show when the user clicks the button
suggested_queries = [
    "Give me the seller name with the best sales performance",
    "Which product had the most revenue?",
]


# Initialize the API client
api_client = APIClient(os.environ.get("API_URL"), os.environ.get("API_KEY"))
api_client = APIClient("http://localhost:8080/score", "")

# Custom CSS to match the style
st.set_page_config(page_title="DBCopilot", page_icon="📊")
st.markdown("<style>" + open("./frontend/styles.css").read() + "</style>", unsafe_allow_html=True)
st.title("DBCopilot")
st.subheader("DBCopilot, your copilot for structured databases.")

# Create a clickable text to show additional questions. Make them two
# columns to make it look better.
# should hide if clicked again

# Initialize session state for button click if not already initialized
if "show_questions" not in st.session_state:
    st.session_state.show_questions = False

# Toggle the state when the button is clicked
if st.button("📊[Click to show suggested questions](#)"):
    st.session_state.show_questions = not st.session_state.show_questions

# Initialize the custom query
custom_query = None

# Show or hide the questions based on the state
if st.session_state.show_questions:
    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            suggested_queries[0],
            kwargs={"clicked_button_ix": 1},
            use_container_width=True,
        ):
            custom_query = suggested_queries[0]
    with col2:
        if st.button(
            suggested_queries[1],
            kwargs={"clicked_button_ix": 2},
            use_container_width=True,
        ):
            custom_query = suggested_queries[1]


# Initialize session state messages if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat-like interface for user question
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        query = msg["content"].get("query")
        table = msg["content"].get("table")

        with st.chat_message("assistant"):
            st.html("<span class='chat-assistant'></span>")
            st.code(query, language="sql")

        with st.chat_message("assistant"):
            st.html("<span class='chat-assistant'></span>")
            if table:
                st.markdown(table, unsafe_allow_html=True)

#  Gwet user query and get response from the API
user_query = st.chat_input(placeholder="Ask me anything!")

if user_query or custom_query:
    query_input = user_query or custom_query
    st.session_state.messages.append({"role": "user", "content": query_input})
    with st.chat_message("user"):
        st.write(query_input)

    with st.chat_message("assistant"):
        query, table = api_client.get_response_formatted(
            query_input, chat_history=st.session_state.messages
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": {"query": query, "table": table}}
        )
        st.html("<span class='chat-assistant'></span>")
        st.code(query, language="sql")

    with st.chat_message("assistant"):
        st.html("<span class='chat-assistant'></span>")
        if table:
            st.markdown(table, unsafe_allow_html=True)
