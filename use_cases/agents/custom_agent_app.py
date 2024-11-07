from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI
from langchain.agents import tool
from datetime import date

# Initialize the language model
llm = ChatOpenAI(temperature=0)

# Load built-in langchain tools
tools = load_tools(["llm-math","wikipedia"], llm=llm)

@tool
def time(text: str) -> str:
    """Returns todays date, use this for any \
    questions related to knowing todays date. \
    The input should always be an empty string, \
    and this function will always return todays \
    date - any date mathematics should occur \
    outside this function."""
    return str(date.today())

# Initialize the agent.
agent= initialize_agent(
    tools + [time], 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)
# CHAT_ZERO_SHOT_REACT_DESCRIPTION - This is optimized to work with chat models. 
# and react. React is a prompting strategy that elicits better thoughts from 
# a language model.

# Call the agent
while True:
    try:
        query = input("Enter your query: ")
        if query == "exit":
            break
        result = agent(query) 
        print(result)
    except: 
        print("exception on external access")