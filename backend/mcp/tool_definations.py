
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "create_task",
            "description": "Create a new task in the task manager. Use when the user wants to add a to-do, reminder, or action item.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title or description of the task"
                    }
                },
                "required": ["title"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_all_tasks",
            "description": "Retrieve all existing tasks from the task manager.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_event",
            "description": "Create a new calendar event. Use when the user wants to schedule a meeting, appointment, or event at a specific time.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title or name of the event"
                    },
                    "time": {
                        "type": "string",
                        "description": "The date and time of the event (e.g. 'tomorrow at 3pm', 'Monday 10am', '2024-12-25 09:00')"
                    }
                },
                "required": ["title", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_all_events",
            "description": "Retrieve all existing calendar events.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_note",
            "description": "Create a new note. Use when the user wants to save information, write something down, or record details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the note"
                    },
                    "content": {
                        "type": "string",
                        "description": "The body/content of the note"
                    }
                },
                "required": ["title"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_all_notes",
            "description": "Retrieve all existing notes.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_notes",
            "description": "Search notes by keyword in title or content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "The keyword to search for"
                    }
                },
                "required": ["keyword"]
            }
        }
    }
]