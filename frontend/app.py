import streamlit as st  

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
        st.markdown("1. What is the average salary of employees?")
    with col2:
        st.markdown("2. How many employees are there in each department?")


# Initialize session state messages if not already initialized
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Chat-like interface for user question  
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask me anything!")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("Question"):
        response = ""
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)