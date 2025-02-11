# app.py
from agents.user_proxy_agent import UserProxyAgent
from agents.assistant_agent import AssistantAgent
from core.stock_data_handler import plot_stock_data

# Initialize Agents
user_agent = UserProxyAgent()
assistant_agent = AssistantAgent()

# Example interaction
user_request = "Plot a chart of META and TSLA stock price change YTD."
code_to_execute = "plot_stock_data(['META', 'TSLA'], metric='price')"
assistant_agent.execute_python_code(code_to_execute)