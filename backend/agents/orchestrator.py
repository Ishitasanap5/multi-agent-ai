from groq import Groq
import os
import json
from dotenv import load_dotenv
import dateparser

from agents.task_agent import TaskAgent
from agents.calendar_agent import CalendarAgent

# Load env variables
load_dotenv(dotenv_path=".env")

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class Orchestrator:

    def __init__(self):
        self.task_agent = TaskAgent()
        self.calendar_agent = CalendarAgent()

    def handle_request(self, user_input: str):

        prompt = f"""
Extract structured data from user input.

Return JSON ONLY:
{{
  "action": "create_task OR create_event",
  "title": "...",
  "time": "..."
}}

Rules:
- If it's a task → action = create_task
- If it's a meeting/appointment/event → action = create_event
- Extract a short clean title
- Extract time if present, else return empty string ""

Input: {user_input}
"""

        try:
            # 🔥 Call LLM
            response = client.chat.completions.create(
                model=os.getenv("MODEL_NAME"),
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.choices[0].message.content
            print("🧠 RAW LLM:", content)

            # 🧹 Clean markdown JSON if present
            content = content.replace("```json", "").replace("```", "").strip()

            # 📦 Parse JSON
            data = json.loads(content)

            action = data.get("action", "").lower()
            title = data.get("title", user_input)
            raw_time = data.get("time", "")

            # 🕒 Convert natural language → datetime
            parsed_time = dateparser.parse(
                raw_time,
                settings={"PREFER_DATES_FROM": "future"}
            )

            if parsed_time:
                time = parsed_time.strftime("%Y-%m-%d %H:%M")
            else:
                time = "Not specified"

        except Exception as e:
            print("❌ LLM Error:", e)
            return {"error": "LLM failed or invalid JSON"}

        # 🚀 Route to agents
        if action == "create_event":
            return self.calendar_agent.create_event(title, time)

        elif action == "create_task":
            return self.task_agent.create_task(title)

        else:
            return {"message": "Could not understand"}