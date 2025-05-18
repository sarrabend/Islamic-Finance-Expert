from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools

from src.config.prompts import ACCOUNTING_ASSISTANT_INSTRUCTION

from .tools import retrieval_tool


gpt = OpenAIChat(
	id="gpt-4o",
	temperature=0.4,
)

tools = [retrieval_tool]
# Define the tools for the anomaly detector agent

accounting_assistant = Agent(
	name="Accounting Assistant",
	model=gpt,
	add_context=True,
	instructions=ACCOUNTING_ASSISTANT_INSTRUCTION,
	tools=[retrieval_tool, ReasoningTools()], 
	show_tool_calls=True,
	add_history_to_messages=True,
	num_history_responses=5,
	markdown=True,
)