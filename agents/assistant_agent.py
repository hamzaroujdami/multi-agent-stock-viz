# agents/assistant_agent.py
import autogen
import subprocess

class AssistantAgent(autogen.AssistantAgent):
    def __init__(self, name="Assistant", **kwargs):
        super().__init__(name=name, **kwargs)
        self.execution_mode = "python"

    def execute_python_code(self, code):
        try:
            exec(code, globals())
        except ModuleNotFoundError as e:
            package_name = str(e).split("'")[1]
            print(f"Error: {package_name} is not installed. Installing...")
            subprocess.run(["pip", "install", package_name])
            exec(code, globals())
        except Exception as e:
            print(f"Execution Error: {e}")