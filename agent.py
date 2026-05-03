class Agent:
    def __init__(self, name, role, llm):
        self.name = name
        self.role = role
        self.llm = llm
        self.memory = []

    def respond(self, topic, context):

        prompt = f"""
You are {self.name}, a {self.role}.

TOPIC:
{topic}

CONVERSATION CONTEXT:
{context}

INSTRUCTIONS:
- Respond directly to the last speaker
- Do NOT restart or repeat the topic
- Stay in character
"""

        reply = self.llm(prompt)

        formatted = f"{self.name} ({self.role}): {reply}"
        self.memory.append(formatted)

        return formatted