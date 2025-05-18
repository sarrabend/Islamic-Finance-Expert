import pandas as pd

from src.challenge_3.agents.agent import scanner

if __name__ == "__main__":
	# Load the dataset
	user_input=""
	while True :
		# Get user input
		user_input = input("You: ")
		response = scanner.print_response(user_input, stream=True)
		if user_input.lower() == "exit" : 
			break



