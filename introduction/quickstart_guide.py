from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents.load_tools import get_all_tool_names
from langchain import ConversationChain

# Load environment variables
load_dotenv(find_dotenv())
print("Environment variables loaded.")
# --------------------------------------------------------------
# LLMs: Get predictions from a language model
"""
This is where the connection is made to the specific Model you want to interact with.

TLDR: Set up Model
"""
# --------------------------------------------------------------

# print("Getting predictions from a language model")
# llm = OpenAI(model_name='text-davinci-003')
# prompt = "Write a poem about python and ai"
# print(llm(prompt))


# --------------------------------------------------------------
# Prompt Templates: Manage prompts for LLMs
"""
This is where you design the prompts that you want to use to interact with the LLM.

TLDR: Set up Prompt
"""
# --------------------------------------------------------------

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}"
)


prompt.format(product="Smart Apps using Large Language Models (LLMs)")

# Output of print(prompt): input_variables=['product'] output_parser=None partial_variables={} template='What is a good name for a company that makes {product}' template_format='f-string' validate_template=True


# --------------------------------------------------------------
# Chains: Combine LLMs and prompts in multi-step workflows
"""
This is where you add extra steps for he LLM do do other stuff.

TLDR: Set up the chain of events
"""

# --------------------------------------------------------------

# llm = OpenAI()
# prompt = PromptTemplate(
#     input_variables=["product"],
#     template="What is a good name for a company that makes {product}"
# )
#
# chain = LLMChain(llm=llm, prompt=prompt)
# output = chain.run("AI Chatbots for Dental Offices")
# print(output)


# --------------------------------------------------------------
# Agents: Dynamically Call Chains Based on User Input

"""
Interacts with tools called agents that allow you to do specific things like write files

TLDR: Gets Agents that can do non-language stuff.
"""
# --------------------------------------------------------------

llm = OpenAI()
get_all_tool_names()
tools = load_tools(tool_names=['wikipedia', 'llm-math'], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run(
    "In what year was python released and who is the original creator? Multiply the year by 3"
)



# --------------------------------------------------------------
# Memory: Add State to Chains and Agents
# --------------------------------------------------------------

# llm = OpenAI()
# conversation = ConversationChain(llm=llm, verbose=True)
#
# output = conversation.predict(input="Hi there!")
# print(output)
#
# output = conversation.predict(
#     input="I'm doing well! Just having a conversation with an AI."
# )
# print(output)
