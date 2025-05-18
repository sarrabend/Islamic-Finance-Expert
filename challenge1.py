import pandas as pd

from src.challenge_1.agent import accounting_assistant

if __name__ == "__main__":
	# Load the dataset
	user_input=""
	while True :
		# Get user input
		user_input = input("You: ")
		response = accounting_assistant.print_response(user_input, stream=True)
		if user_input.lower() == "exit" : 
			break



