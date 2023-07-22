# This is a repository to demostrate streamlit with some possible use cases

/pages contains all the subpage
/data contains the static data csv
data_vis.py is the entry point


### The repository can be run using docker
sudo docker build . -t streamlit:test

sudo docker run -it --rm -p <desired_port>:8501 streamlit:test <your streamlit command>
