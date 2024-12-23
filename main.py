from phi.agent import Agent
from phi.tools.github import GithubTools
import os
from datetime import datetime, timedelta
from phi.agent import RunResponse
from phi.utils.pprint import pprint_run_response
from model import model
from dotenv import load_dotenv
load_dotenv()

from agents import perplexity_agent, portfolio_analysis_agent

while True:
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye!")
        break

    try:
        # Get portfolio analysis response
        portfolio_analysis_response = portfolio_analysis_agent.portfolio_analysis(user_input)

        # Generate response from the perplexity agent
        response = perplexity_agent(user_input, portfolio_analysis_response)

        print("Agent:", response)

    except Exception as e:
        print(f"An error occurred: {e}")





# #from typing import Iterator

# # Run agent and return the response as a stream
# response_stream: Iterator[RunResponse] = agent.run("Your prompt here", stream=True)

# # Process the stream as needed
# for chunk in response_stream:
#     # Do something with each chunk
#     print(chunk.content)








