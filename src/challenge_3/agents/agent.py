import os 

from agno.agent import Agent
from agno.team import Team
from agno.tools.reasoning import ReasoningTools
from agno.tools.duckduckgo import DuckDuckGoTools

from src.config import PROJECT_PATH
from src.config.prompts import AGENT_INSTRUCTION, ANALYZE_AGENT_INSTRUCTION, JUSTIFY_AGENT_INSTRUCTION, UPDATE_AGENT_INSTRUCTION, TRANSLATE_AGENT_INSTRUCTION, VALIDATE_AGENT_INSTRUCTION
from src.challenge_3.tools.utils import read_file
from src.challenge_3.agents import gpt
# from .utils import extract_response_from_agent
from api.pydantic_models import Answer
from src.challenge_3.tools.agent import  list_collections, get_standards, retrieval_tool


analyze_agent = Agent(
	name="analyze_agent",
	model=gpt,
    description="AAOIFI Standards Analysis Specialist, takes the standard name and code as input",
	instructions=ANALYZE_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[retrieval_tool, ReasoningTools() , DuckDuckGoTools()],
	structured_outputs=True
)

justify_agent = Agent(
	name="justify_agent",
	model=gpt,
	instructions=JUSTIFY_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[retrieval_tool, ReasoningTools() , DuckDuckGoTools()],
	structured_outputs=True
)


update_agent = Agent(
	name="update_agent",
	model=gpt,
    description="AAOIFI Standards Enhancement Specialist, takes the standard name and code as input",
	instructions=UPDATE_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[retrieval_tool, ReasoningTools() , DuckDuckGoTools()],
	structured_outputs=True
)


translate_agent = Agent(
	name="translate_agent",
	model=gpt,
    context={"glossary": read_file(os.path.join(PROJECT_PATH, "dataset", "glossary.csv"))},
    description="Translates text from Arabic to English and vice versa, takes the text to be translated as input",
	instructions=TRANSLATE_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[retrieval_tool, ReasoningTools(), DuckDuckGoTools()],
	structured_outputs=True
)

validate_agent = Agent(
	name="validate_agent",
	model=gpt,
    description="Validates the finacial accounting standard based on shariah standards, takes the standard name and code as input", 
	instructions=VALIDATE_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[retrieval_tool, ReasoningTools(), DuckDuckGoTools()],
	structured_outputs=True
)

agent = Agent(
	name="Orchestrator",
	model=gpt,
    team=[analyze_agent, update_agent, translate_agent, validate_agent, justify_agent],
	instructions=AGENT_INSTRUCTION,
    structured_outputs=True,
	response_model=Answer,
    tools=[list_collections, ReasoningTools()], 
    show_tool_calls=True,
)


if __name__ == "__main__":

    # Run the agent with a sample query
    response = agent.run("We want to make some updates on the Financial Accounting Standard N.32 (Ijarah) in order to improve its usefulness while following the islamic finances standards", debug=True)
    # print(response)
    print(response)