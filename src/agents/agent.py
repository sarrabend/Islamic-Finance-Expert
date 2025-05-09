from agno.agent import Agent
from agno.team import Team
from agno.tools.reasoning import ReasoningTools
from agno.tools.duckduckgo import DuckDuckGoTools

from src.config.prompts import AGENT_INSTRUCTION, REVIEW_AGENT_INSTRUCTION, JUSTIFY_AGENT_INSTRUCTION, UPDATE_AGENT_INSTRUCTION, TRANSLATE_AGENT_INSTRUCTION, VALIDATE_AGENT_INSTRUCTION

from src.agents import gpt
from api.pydantic_models import Answer
from src.tools.agent import tool_name


review_agent = Agent(
	name="review_agent",
	model=gpt,
	instructions=REVIEW_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[tool_name, ReasoningTools()],
	structured_outputs=True
)

justify_agent = Agent(
	name="justify_agent",
	model=gpt,
	instructions=JUSTIFY_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[tool_name, ReasoningTools()],
	structured_outputs=True
)


update_agent = Agent(
	name="update_agent",
	model=gpt,
	instructions=UPDATE_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[tool_name, ReasoningTools()],
	structured_outputs=True
)


translate_agent = Agent(
	name="translate_agent",
	model=gpt,
	instructions=TRANSLATE_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[tool_name, ReasoningTools()],
	structured_outputs=True
)

validate_agent = Agent(
	name="validate_agent",
	model=gpt,
	instructions=VALIDATE_AGENT_INSTRUCTION,
	response_model=Answer,
	tools=[tool_name, ReasoningTools()],
	structured_outputs=True
)

agent = Agent(
	name="agent",
	model=gpt,
	instructions=AGENT_INSTRUCTION,
	response_model=Answer,
    tools=[tool_name, ReasoningTools()],
    structured_outputs=True
)