from phi.agent import Agent
from dotenv import load_dotenv
from phi.agent import Agent, RunResponse
from tools.perplexity_tool import PerplexitySearch
from model import model

load_dotenv()

perplexity_tool = PerplexitySearch(api_key="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")

def perplexity_agent(user_input, portfolio_data=""):  # Fixed spelling
    agent = Agent(
        instructions=[
            "You are a crypto conversation agent that is cool and talk with the user .",
            "if the user ask soomethind and u decide you dont know it call the perplexity_tool.perplexity_search",
            "if you think you should do a portfolio analysis do a portfolio analysis",
            "do not use the tool for something you know or can do or know  ",
            "sen the message to slack if user asks so if user does not specify send the message to channel #ai"
        ],
        tools=[perplexity_tool.perplexity_search],
        show_tool_calls=False,
        model=model,
        debug_mode=False,
    )

    prompt = f"Do this {user_input}. ignore the portfolio part if there is no data This is the portfolio data: {portfolio_data}"
    
    response: RunResponse = agent.run(prompt)  # Use the query parameter instead of hardcoded string
    return response.content

