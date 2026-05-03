class DebateEngine:
    def __init__(self, agents):
        self.agents = agents
        self.history = []

    def run(self, topic, rounds=2):

        self.history = []

 
        first = self.agents[0].respond(
            topic,
            f"""
Start the debate on: {topic}

Rules:
- Speak briefly (max 2 short paragraphs)
- Do NOT introduce yourself
- Make a clear opening argument
"""
        )

        self.history.append(first)

        for _ in range(rounds):
            for agent in self.agents:

                last_message = self.history[-1]

                context = f"""
TOPIC: {topic}

LAST MESSAGE:
{last_message}

RULES:
- Respond ONLY to the last message
- Do NOT repeat previous arguments
- Keep response under 120 words
- Push the debate forward
- Be direct and concise
"""

                reply = agent.respond(topic, context)

                self.history.append(reply)

        return self.history
