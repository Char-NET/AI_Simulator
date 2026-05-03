class DebateEngine:
    def __init__(self, agents):
        self.agents = agents
        self.history = []

    def run(self, topic, rounds=2):

        self.history = []

        # first message
        first = self.agents[0].respond(
            topic,
            "Start the debate naturally. Do NOT introduce yourself repeatedly."
        )

        self.history.append(first)

        for _ in range(rounds):
            for agent in self.agents:

                last_message = self.history[-1]

                context = f"""
Topic: {topic}

Last message:
{last_message}

Recent conversation:
{chr(10).join(self.history[-5:])}
"""

                reply = agent.respond(topic, context)

                self.history.append(reply)

        return self.history