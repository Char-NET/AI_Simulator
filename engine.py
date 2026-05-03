class DebateEngine:
    def __init__(self, agents):
        self.agents = agents
        self.history = []

    def run(self, topic, rounds=2):

        self.history = []

     
        last_message = self.agents[0].respond(
            topic,
            f"""
Start the debate on: {topic}

Rules:
- Do NOT introduce yourself
- Make a short opening argument
- Stay concise
"""
        )

        self.history.append(last_message)

        
        for r in range(rounds):

            for i, agent in enumerate(self.agents):

                last_message = self.history[-1]

                context = f"""
TOPIC: {topic}

LAST MESSAGE:
{last_message}

RULES:
- Respond ONLY to the last speaker
- Do NOT repeat arguments
- Keep under 120 words
- Advance the discussion
"""

                reply = agent.respond(topic, context)

                self.history.append(reply)

        return self.history
