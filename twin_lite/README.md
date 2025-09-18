# TwinLite Crew

Welcome to the TwinLite Crew project, powered by [documentation](https://docs.crewai.com). The goal is to design a simple CrewAI agent that embodies my skills, personality, or interests, like my “digital twin lite.”

# Overall Objectives of this project

- Design a digital twin by following these steps:
1. In code, define my agent’s role, goal, and tools (for example, can it search the web, summarize text, draft emails).
2. Give my agent a persona that reflects me: what tasks would it handle on my behalf?
3. Run the agent with a simple test prompt (for example, “introduce yourself to the class” or “explain my background in 3 sentences”).

Document what worked, what didn’t, and what you learned.

## Installation

This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

- Modify `src/twin_lite/config/agents.yaml` to define your agents
- Modify `src/twin_lite/config/tasks.yaml` to define your tasks
- Modify `src/twin_lite/crew.py` to add your own logic, tools and specific args
- Modify `src/twin_lite/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the twin-lite Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The twin-lite Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

Visit our 
