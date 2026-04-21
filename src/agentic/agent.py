import time

from .tools import AVAILABLE_TOOLS
from .io_utils import format_output
from .router import route_command
from .activity_log import log_event

class SimpleAgent:
    def __init__(self, name="HelperBot"):
        self.name = name

    def execute_command(self, task: str, command: str, **kwargs):
        tool_name = route_command(command)
        return self.execute(task=task, tool_name=tool_name, **kwargs)

    def execute(self, task: str, tool_name: str, **kwargs):
        print(f"[{self.name}] Sto pensando al compito: {task}")
        
        if tool_name not in AVAILABLE_TOOLS:
            log_event("tool_unknown", agent_name=self.name, task=task, tool_name=tool_name)
            return "Mi dispiace, non so come usare questo strumento."

        tool = AVAILABLE_TOOLS[tool_name]
        start = time.perf_counter()
        log_event(
            "tool_start",
            agent_name=self.name,
            task=task,
            tool_name=tool_name,
            kwargs=kwargs,
        )
        try:
            result = tool(**kwargs)
        except Exception as e:
            elapsed_ms = int((time.perf_counter() - start) * 1000)
            log_event(
                "tool_error",
                agent_name=self.name,
                task=task,
                tool_name=tool_name,
                kwargs=kwargs,
                elapsed_ms=elapsed_ms,
                error_type=type(e).__name__,
                error=str(e),
            )
            raise

        elapsed_ms = int((time.perf_counter() - start) * 1000)
        log_event(
            "tool_ok",
            agent_name=self.name,
            task=task,
            tool_name=tool_name,
            elapsed_ms=elapsed_ms,
        )
        return format_output(result)

# Esempio di utilizzo:
# agent = SimpleAgent()
# agent.execute("Somma 5 e 10", "add_numbers", a=5, b=10)
