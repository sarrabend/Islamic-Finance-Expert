import os 
from agno.models.openai import OpenAIChat

from agno.agent import Agent
from agno.team import Team
from agno.tools.reasoning import ReasoningTools
from agno.tools.duckduckgo import DuckDuckGoTools

from src.config import PROJECT_PATH
from src.config.prompts import AGENT_INSTRUCTION, ANALYZE_AGENT_INSTRUCTION, FAS_AGENT_INSTRUCTION, SS_AGENT_INSTRUCTION
from src.challenge_3.tools.utils import read_file
# from .utils import extract_response_from_agent
from src.challenge_3.tools.agent import  list_collections, get_standards, retrieval_tool


gpt = OpenAIChat(
	id="gpt-4o",
	temperature=0.4,
)

AGENT_RESPONSE_KEYS = {
    "agent": ["answer"],
}


fs_agent = Agent(
	name="FAS Agent",
	model=gpt,
	instructions=FAS_AGENT_INSTRUCTION,
	structured_outputs=True,
	tools=[ReasoningTools()], 
	show_tool_calls=True,)


ss_agent = Agent(	
	name="SS Agent",
	model=gpt,
	instructions=SS_AGENT_INSTRUCTION,
	structured_outputs=True,
	tools=[ ReasoningTools()], 
	show_tool_calls=True,)


scanner = Agent(
    name="scanner",
    model=gpt,
    team=[fs_agent, ss_agent],
    instructions=ANALYZE_AGENT_INSTRUCTION,
	structured_outputs=True,
	tools=[ReasoningTools()], 
	show_tool_calls=True,)




# agent = Agent(
# 	name="Orchestrator",
# 	model=gpt,
#     team=[],
# 	instructions=AGENT_INSTRUCTION,
#     structured_outputs=True,
# 	response_model=Answer,
#     tools=[list_collections, ReasoningTools()], 
#     show_tool_calls=True,
# )




