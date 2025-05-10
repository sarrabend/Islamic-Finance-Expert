# Islamic Finance Expert - AI-Powered Islamic Finance Compliance System

A hybrid AI + blockchain architecture for automated, explainable, and trust-based Islamic finance compliance. This project was developed for the IsDBI hackathon and implements multiple challenges focusing on different aspects of Islamic finance automation and compliance.

This repo contains the AI-side source code of the project described below.

## Project Overview

The system consists of four main components:

1. **Automated Financial Entries Calculation**
   - Reduces human intervention while maintaining expert oversight
   - Implements AI-driven calculation automation
   - Ensures accuracy and compliance in financial entries

2. **Shariah-Compliant Standards Projection**
   - Projects financial entries to nearest Shariah-compliant standards
   - Provides context-aware mapping
   - Ensures compliance with Islamic finance principles

3. **AAOIFI Standards Review & Update System**
   - Enables practitioners to review and validate AAOIFI standards
   - Suggests improvements while maintaining compliance
   - Implements multi-agent system for comprehensive analysis

4. **Conventional to Islamic Product Conversion**
   - Projects conventional contracts onto Islamic standards
   - Automates review process using advanced reasoning models
   - Integrates blockchain for trust and transparency
   - Enables broader usability of Islamic financial products

## Project Structure

```
Islamic-Finance-Expert/
├── challenge_1/          # Automated Financial Entries
├── challenge_2/          # Standards Projection
├── challenge_3/          # AAOIFI Standards Review
├── challenge_4/          # Product Conversion
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment tool (venv or conda)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Islamic-Finance-Expert.git
   cd Islamic-Finance-Expert
   ```

2. **Create and activate virtual environment**
   ```bash
   # Using venv
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Challenge-Specific Setup

### Challenge 1: Automated Financial Entries
```bash
cd challenge_1
# Follow instructions in challenge_1/README.md
```

### Challenge 2: Standards Projection
```bash
cd challenge_2
# Follow instructions in challenge_2/README.md
```

### Challenge 3: AAOIFI Standards Review
```bash
cd challenge_3
# Follow instructions in challenge_3/docs.md
```

### Challenge 4: Product Conversion
```bash
cd challenge_4
# Follow instructions in challenge_4/README.md
```

## Key Features

- **AI-Powered Analysis**: Utilizes advanced language models for Islamic finance analysis
- **Multi-Agent System**: Implements specialized agents for different aspects of Islamic finance
- **Blockchain Integration**: Ensures transparency and trust in financial operations
- **Shariah Compliance**: Built-in validation against Islamic finance principles
- **Bilingual Support**: Arabic-English translation capabilities
- **Standardized Output**: Consistent response format across all challenges

## Usage Examples

### Challenge 3 Example (AAOIFI Standards)
```python
from src.challenge_3.agents.agent import agent

query = "We want to make some updates on the Financial Accounting Standard N.32 (Ijarah)"
response = agent.run(query)
```

## Acknowledgments

- IsDBI Hackathon organizers
- AAOIFI for standards reference
- All contributors and participants
