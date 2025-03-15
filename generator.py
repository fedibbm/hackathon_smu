import os
import subprocess
import logging

class SwarmLauncher:
    def __init__(self):
        self.agent_dir = "ai_agents"
        logging.basicConfig(level=logging.INFO)

    def execute_swarm(self):
        agents = ["Brainstormer.py", "Critic.py", "Refiner.py"]  # Order matters
        for agent in agents:
            if agent.endswith(".py"):
                logging.info(f"\n⚡ Launching {agent}")
                try:
                    subprocess.run(["python", f"{self.agent_dir}/{agent}"], check=True)
                except subprocess.CalledProcessError as e:
                    logging.error(f"Error executing {agent}: {e}")
                    return  # Stop if one agent fails

if __name__ == "__main__":
    SwarmLauncher().execute_swarm()

