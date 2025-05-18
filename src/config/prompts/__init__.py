import os
from .utils import load_prompt

# Define paths to the `.md` files
PROMPTS_DIR = os.path.dirname(__file__)
AGENT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "agent.md")
ANALYZE_AGENT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "analyze_agent_instruction.md")
JUSTIFY_AGENT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "justify_agent_instruction.md")
UPDATE_AGENT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "update_agent_instruction.md")
TRANSLATE_AGENT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "translate_agent_instruction.md")
VALIDATE_AGENT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "validate_agent_instruction.md")



# Load challenge 1 prompts
ACCOUNTING_ASSISTANT_INSTRUCTION = load_prompt(os.path.join(PROMPTS_DIR, "accounting_assistant_instruction.md"))
print(ACCOUNTING_ASSISTANT_INSTRUCTION)


# Load challenge 3 prompts

FAS_AGENT_INSTRUCTION = load_prompt(os.path.join(PROMPTS_DIR, "fas_agent_instruction.md"))
SS_AGENT_INSTRUCTION = load_prompt(os.path.join(PROMPTS_DIR, "ss_agent_instruction.md"))
AGENT_INSTRUCTION = load_prompt(AGENT_INSTRUCTION_PATH)
ANALYZE_AGENT_INSTRUCTION = load_prompt(ANALYZE_AGENT_INSTRUCTION_PATH)
JUSTIFY_AGENT_INSTRUCTION = load_prompt(JUSTIFY_AGENT_INSTRUCTION_PATH)
UPDATE_AGENT_INSTRUCTION = load_prompt(UPDATE_AGENT_INSTRUCTION_PATH)
TRANSLATE_AGENT_INSTRUCTION = load_prompt(TRANSLATE_AGENT_INSTRUCTION_PATH)
VALIDATE_AGENT_INSTRUCTION = load_prompt(VALIDATE_AGENT_INSTRUCTION_PATH)