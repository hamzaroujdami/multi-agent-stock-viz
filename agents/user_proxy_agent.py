# agents/user_proxy_agent.py
import autogen

class UserProxyAgent(autogen.UserProxyAgent):
    def __init__(self, name="UserProxy", **kwargs):
        super().__init__(name=name, **kwargs)