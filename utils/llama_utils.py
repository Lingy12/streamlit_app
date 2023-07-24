import json
from typing import List
import streamlit as st
import json
import re
import subprocess
import os
from glob import glob

def save_character(messages: List[dict], name:str):
    """
    Save current system setting as configuration
    """
    sys_conf = list(filter(lambda x: x['role'] == 'system', messages)) 

    with open(f'/app/llama_sys_conf/{name}.json', 'w') as f:
        json.dump(sys_conf, f)
    print(f'Saved characteristic {name}')

def load_character(name: str):
    """
    Load existing character from saved.
    """
    with open(f'/app/llama_sys_conf/{name}.json', 'r') as f:
        conf = json.load(f)
    return conf

def list_character(): 
    saved_char =  list(map(lambda x: os.path.splitext(x)[0], os.listdir('/app/llama_sys_conf/')))
    print(saved_char)
    return saved_char

def handle_sys_cmd(prompt, messages):
    sys_cmd = prompt[9:]
    with st.chat_message("system"):
        st.markdown(sys_cmd)
    messages.append({"role": "system", "content": sys_cmd})
    print('system cmd appened')

def handle_usr_prompt(prompt, messages, max_seq_len):
    print("Handling user prompt")
    with st.chat_message("user"):
        st.markdown(prompt)
    messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
    # Change to calling llama
        message_placeholder = st.empty()
        message_placeholder.markdown(" " + "▌")
        result = subprocess.Popen(["torchrun", "--nproc_per_node", "1", "inference.py", 
                               "--ckpt_dir", "/llama/llama-2-7b-chat/", "--tokenizer_path", "/llama/tokenizer.model",
                               "--max_seq_len", str(max_seq_len), "--max_batch_size", "1", 
                               "--dialog", json.dumps(st.session_state.messages)], stdout=subprocess.PIPE)
        stdout, err = result.communicate()
        print(stdout, err)
        target = re.findall(r"\{(.*?)\}", stdout.decode())
        print(target[-1])
        response = json.loads("{" + target[-1] + "}")['content']
        message_placeholder.markdown(response)
    messages.append({"role": "assistant", "content": response})

