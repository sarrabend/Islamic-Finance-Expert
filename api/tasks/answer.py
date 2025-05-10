from src.challenge_3.agents.utils import extract_response_from_agent
from src.challenge_3.agents.agent import agent
from api.pydantic_models import Answer

def answer(request: str) -> Answer:
    
    try:
        response = agent.run(
            request
        )
        result = response.content
        return Answer(extract_response_from_agent(result, "agent"))
            
    except Exception as e:
        return str(e)