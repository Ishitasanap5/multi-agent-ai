
import dateparser
from agents.task_agent import TaskAgent
from agents.calendar_agent import CalendarAgent
from agents.notes_agent import NotesAgent


class MCPToolExecutor:
    """
    Executes tool calls dispatched by the LLM via the orchestrator.
    Acts as the MCP server — receives (tool_name, args) and returns results.
    """

    def __init__(self):
        # Agents are registered here — the executor owns them
        self._task_agent = TaskAgent()
        self._calendar_agent = CalendarAgent()
        self._notes_agent = NotesAgent()

        # Dispatch table: tool_name → handler method
        # Adding a new tool = adding one line here + schema in tool_definitions.py
        self._dispatch = {
            "create_task":    self._create_task,
            "get_all_tasks":  self._get_all_tasks,
            "create_event":   self._create_event,
            "get_all_events": self._get_all_events,
            "create_note":    self._create_note,
            "get_all_notes":  self._get_all_notes,
            "search_notes":   self._search_notes,
        }

    def execute(self, tool_name: str, tool_args: dict) -> dict:
        """
        Main entry point. Called by the orchestrator for every tool_call
        the LLM returns.

        Returns a result dict always — never raises, so the orchestrator
        can continue processing remaining tool calls even if one fails.
        """
        handler = self._dispatch.get(tool_name)
        if not handler:
            return {"error": f"Unknown tool: '{tool_name}'"}
        try:
            return handler(**tool_args)
        except TypeError as e:
            # Catches wrong/missing arguments from the LLM
            return {"error": f"Bad arguments for tool '{tool_name}': {str(e)}"}
        except Exception as e:
            return {"error": f"Tool '{tool_name}' failed: {str(e)}"}

    # ── Task handlers ────────────────────────────────────────────────────────

    def _create_task(self, title: str) -> dict:
        return self._task_agent.create_task(title)

    def _get_all_tasks(self) -> dict:
        tasks = self._task_agent.get_all_tasks()
        return {"agent": "TaskAgent", "action": "get_all_tasks", "data": tasks}

    # ── Calendar handlers ────────────────────────────────────────────────────

    def _create_event(self, title: str, time: str) -> dict:
        # Parse natural language time before passing to agent
        parsed = dateparser.parse(time)
        formatted_time = parsed.strftime("%Y-%m-%d %H:%M") if parsed else "Not specified"
        return self._calendar_agent.create_event(title, formatted_time)

    def _get_all_events(self) -> dict:
        events = self._calendar_agent.get_all_events()
        return {"agent": "CalendarAgent", "action": "get_all_events", "data": events}

    # ── Notes handlers ───────────────────────────────────────────────────────

    def _create_note(self, title: str, content: str = "") -> dict:
        return self._notes_agent.create_note(title, content)

    def _get_all_notes(self) -> dict:
        notes = self._notes_agent.get_all_notes()
        return {"agent": "NotesAgent", "action": "get_all_notes", "data": notes}

    def _search_notes(self, keyword: str) -> dict:
        results = self._notes_agent.search_notes(keyword)
        return {"agent": "NotesAgent", "action": "search_notes", "data": results}