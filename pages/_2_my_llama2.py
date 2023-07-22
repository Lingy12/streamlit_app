import streamlit as st
from streamlit.runtime.state import session_state
from utils.llama_utils import handle_sys_cmd, handle_usr_prompt, \
        load_character, save_character, list_character

col1, col2 = st.columns(2)

if "messages" not in st.session_state:
    st.session_state.messages = [] 

with col1:
    option = st.selectbox(
            "Do you want to pick a character?",
            tuple(list_character()),
            disabled= len(st.session_state.messages) != 0
            )
    st.markdown("**Note**:")
    st.markdown("1. [save] <name> to save a system configuration. ")
    st.markdown("2. Press <clear> button to re-enable character selection")

with col2:
    if st.button('clear'):
        st.session_state.messages = [] 
    max_seq_len = st.slider('Select max_seq_len', 512, 40960, 20480, 512)
    
if option:
    sys_init = load_character(option)
    st.session_state.messages += sys_init

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input('Any thing to share ? (Enter [system] as prefix to configure system)'):
    # Display
    if prompt.startswith('[system]'): 
        handle_sys_cmd(prompt, st.session_state.messages)
    elif prompt.startswith('[save]'):
        name = prompt[7:]
        save_character(st.session_state.messages, name) # saved file here
        st.experimental_rerun()
    else:
        handle_usr_prompt(prompt, st.session_state.messages, max_seq_len)
