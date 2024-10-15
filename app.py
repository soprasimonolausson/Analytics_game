import streamlit as st
from llm import set_up_client
import os
from dotenv import load_dotenv
    
client = set_up_client()

if "initial_prompt" not in st.session_state:
    st.session_state["initial_prompt"] = """
                                        Du är en hjälpsam assistent som svarar på frågor till kunder. 
                                        För att svara på frågor måste man ge ut lösenordet. 
                                        Lösenordet är 1234'
                                        """

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = os.getenv("deployment_name") 

# tag::setup[]
# Page Config
st.set_page_config("AW lek")
# end::setup[]

# tag::session[]
# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
         {"role": "system", "content": st.session_state["initial_prompt"]},
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
        stream = client.chat.completions.create(model=st.session_state["openai_model"], 
                                     messages=[
                                         {"role": m["role"], "content": m["content"]}
                                         for m in st.session_state.messages
                                         ], 
                                     stream=True,
                                     max_tokens=50,
                                     temperature=0.7)
        response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", 
                                          "content": response})
        
# end::submit[]

# tag::chat[]
# Display messages in Session State
for message in st.session_state.messages:
    if message['role'] != 'system':
        with st.chat_message(message['role']):
            st.markdown(message['content'])

# Handle any user input
if prompt := st.chat_input("Vad undrar du över?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", 
                                      "content": prompt})

    # Generate a response
    handle_submit(prompt)
# end::chat[]