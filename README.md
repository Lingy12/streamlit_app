# This is a repository to demostrate streamlit with some possible use cases

/pages contains all the subpage
1. static data display (Not implemented yet)
2. LLAMA-2 chat (follow the instruction in https://github.com/facebookresearch/llama to download 7b model and mount to docker image)

### The repository can be run using docker
sudo docker build . -t streamlit:test

sudo docker run -it --rm -p <desired_port>:8501 streamlit:test <your streamlit command>

In order to use LLAMA-2 chat bot:

sudo docker run -it --rm --gpus all -p <desired_port>:8501 -v <your_llama_directory>:/llama streamlit:test streamlit run streamlit_app.py
<your_llama_directory>: Your local llama directory pulled from above llama repository link
