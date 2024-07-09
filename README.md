# ResearchCrew

This project is an example using the CrewAI framework to automate the process of writing a Related Work section of an academic paper. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

## Setup
Python 3.10.14 is used in this project.
You can download necessary python packages using pip:

`pip install -r requirements.txt`

Create a .env file in the project and add LLM API keys. You can use .env_example as reference. 

Now the system uses OpenAI as an LLM. You can change it by adding the API key in .env and change the LLM by modifiying self.llm in agents.py.

## Usage
Run the following command on terminal, then you can use streamlit UI to access ResearchCrew!

`streamlit run main.py`

