import os

# get env variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Qdrant configuration
QDRANT_URL = "https://81aaa4fe-e254-402c-90b4-63fd0818740c.europe-west3-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.a8lASrU4g_Vm_rZcmkjucD0aP8eImmpgSIIBUzgp91o"
HF_TOKEN = os.getenv("HF_TOKEN")  # Add Hugging Face token

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
