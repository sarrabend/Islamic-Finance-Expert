from agno.models.openai import OpenAIChat
# from openai import OpenAI

# gpt = OpenAI()

gpt = OpenAIChat(
	id="gpt-4o",
	temperature=0.4,
)

AGENT_RESPONSE_KEYS = {
    "agent": ["answer"],
}
