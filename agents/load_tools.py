from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI

# Initialize the language model
llm = ChatOpenAI(temperature=0)

# Load built-in langchain tools
tools = load_tools(["llm-math","wikipedia"], llm=llm)

# Initialize the agent.
agent= initialize_agent(
    tools, 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)
# CHAT_ZERO_SHOT_REACT_DESCRIPTION - This is optimized to work with chat models. 
# and react. React is a prompting strategy that elicits better thoughts from 
# a language model.

agent("What is the 25% of 300?")

question = "Tom M. Mitchell is an American computer scientist \
and the Founders University Professor at Carnegie Mellon University (CMU)\
what book did he write?"
result = agent(question) 