import streamlit as st
from utils import write_message
# tag::import_agent[]
# end::import_agent[]

# tag::setup[]
# Page Config
st.set_page_config("AW lek")
# end::setup[]

# tag::session[]
# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Vad kan jag hjälpa dig med?"},
    ]
# end::session[]

# tag::submit[]
# Submit handler
def handle_submit(message):
    """
    Submit handler: calls on route_response_rag to get a response from cqa_deluxe.
    """

    # Handle the response
    with st.spinner('Laddar svar...'):
        # Call the agent
        #write response here
        write_message('assistant', response)
        
# end::submit[]

def handle_feedback():
    return

# tag::chat[]
# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("Vad undrar du över?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    handle_submit(prompt)
# end::chat[]