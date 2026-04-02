
class Memory:
    """
    Per-user conversation memory.
    Stores messages as {"role": "user"/"assistant", "content": "..."}
    keyed by user_id so multiple users don't share state.
    """

    def __init__(self):
        
        self._store: dict[str, list[dict]] = {}

    def get_history(self, user_id: str = "default") -> list[dict]:
        """Returns conversation history for a user as list of role/content dicts."""
        return self._store.get(user_id, [])

    def add(self, user_id: str, role: str, content: str):
        """
        Add a message to a user's history.
        role must be 'user' or 'assistant'.
        """
        if user_id not in self._store:
            self._store[user_id] = []
        self._store[user_id].append({"role": role, "content": content})

    def get_context_string(self, user_id: str = "default") -> str:
        """
        Returns a formatted string of conversation history for injecting
        into LLM prompts in the orchestrator.
        """
        history = self.get_history(user_id)
        if not history:
            return ""
        lines = [f"{msg['role'].capitalize()}: {msg['content']}" for msg in history]
        return "Previous conversation:\n" + "\n".join(lines) + "\n\n"

    def clear(self, user_id: str = "default"):
        """Clear memory for a specific user."""
        self._store[user_id] = []