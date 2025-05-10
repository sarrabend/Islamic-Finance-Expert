# Challenge 3 - Standard Enhancement Co-Pilot - Technical Specs and execution guide 

This module implements an AI-powered system for analyzing and reviewing and updating Islamic Finance standards, specifically focusing on AAOIFI (Accounting and Auditing Organization for Islamic Financial Institutions) standards.

## Overview

The system consists of multiple specialized agents that work together to:
- Analyze AAOIFI standards
- Update and enhance standards
- Translate between Arabic and English
- Validate standards against Shariah principles
- Justify changes and updates

![image.png](attachment:55975b93-39cd-4e68-b138-64c3f00e551f:image.png)

## Prerequisites

- Python 3.x
- Requirements specified in the project's requirements.txt

## Project Structure

```
challenge_3/
├── agents/
│   ├── agent.py      # Main agent definitions and orchestration
│   └── gpt.py        # GPT model configuration
├── tools/
│   ├── agent.py      # Custom tools for standard retrieval
│   └── utils.py      # Utility functions
└── docs.md           # This documentation file
```

## Available Agents

1. **Analyze Agent**
   - Specializes in AAOIFI Standards Analysis
   - Takes standard name and code as input
   - Provides detailed analysis of standards

2. **Update Agent**
   - Handles AAOIFI Standards Enhancement
   - Takes standard name and code as input
   - Suggests improvements while maintaining compliance

3. **Translate Agent**
   - Handles Arabic-English translation
   - Uses a glossary for accurate financial terminology
   - Takes text input for translation

4. **Validate Agent**
   - Validates financial accounting standards against Shariah principles
   - Takes standard name and code as input
   - Ensures compliance with Islamic finance requirements

5. **Justify Agent**
   - Provides justification for changes and updates (fatwah, AAOIFI)
   - Supports decision-making process

## How to Run

1. Ensure all dependencies are installed (you don't need to run it again if it was already done previously):
   ```bash
   pip install -r requirements.txt
   ```
2. Set your query: 
   # Example query
   response = agent.run("Your query here")
   ```

   ```

3. Run the main agent:
   ```python
   from src.challenge_3.agents.agent import agent



## Example Usage

```python
# Example query for updating a standard
query = "We want to make some updates on the Financial Accounting Standard N.32 (Ijarah) in order to improve its usefulness while following the islamic finances standards"
response = agent.run(query)
```

## Output

The system generates structured responses that include:
- Analysis of the standard
- Suggested updates
- Translations (if needed)
- Validation against Shariah principles
- Justification for changes

## Notes

- The system uses a combination of custom tools and reasoning capabilities
- DuckDuckGo integration is available for additional research
- The system maintains a glossary for accurate translation of financial terms
- All agents are orchestrated by a main agent that coordinates their responses

