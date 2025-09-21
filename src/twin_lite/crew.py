from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import FileReadTool, SerperDevTool, WebsiteSearchTool
from datetime import datetime
from typing import List
import os

@CrewBase
class TwinLite():
    """MIT AI Studio Class Schedule Assistant"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # File paths
    def __init__(self):
        # Get the absolute path to the project root (digital-twin-lite directory)
        self.base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.schedule_path = os.path.join(self.base_path, "data", "schedule.csv")
        self.preferences_path = os.path.join(self.base_path, "knowledge", "user_preference.txt")

    @agent
    def schedule_navigator(self) -> Agent:
        """Agent responsible for navigating the course schedule"""
        # Initialize tools for schedule navigation
        file_tool = FileReadTool(file_path=self.schedule_path)

        return Agent(
            config=self.agents_config['schedule_navigator'],
            tools=[file_tool],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def topic_researcher(self) -> Agent:
        """Agent responsible for researching topics and speakers"""
        # Initialize research tools
        search_tool = SerperDevTool()
        web_tool = WebsiteSearchTool()

        return Agent(
            config=self.agents_config['topic_researcher'],
            tools=[search_tool, web_tool],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def study_coordinator(self) -> Agent:
        """Agent responsible for creating study plans and tracking preparation"""
        # Initialize tools for study coordination
        preferences_file_tool = FileReadTool(file_path=self.preferences_path)
        schedule_file_tool = FileReadTool(file_path=self.schedule_path)

        return Agent(
            config=self.agents_config['study_coordinator'],
            tools=[preferences_file_tool, schedule_file_tool],
            verbose=True,
            allow_delegation=False
        )

    @task
    def next_class_briefing(self) -> Task:
        """Task to get information about the next upcoming class"""
        return Task(
            config=self.tasks_config['next_class_briefing'],
            output_file='answers/next_class.md'
        )

    @task
    def topic_primer(self) -> Task:
        """Task to research and create a primer on a specific topic"""
        return Task(
            config=self.tasks_config['topic_primer'],
            output_file='answers/topic_primer.md'
        )

    @task
    def weekly_preparation(self) -> Task:
        """Task to create a weekly preparation plan"""
        return Task(
            config=self.tasks_config['weekly_preparation'],
            output_file='answers/weekly_plan.md'
        )

    @task
    def assignment_tracker(self) -> Task:
        """Task to track all assignments for a specific track"""
        return Task(
            config=self.tasks_config['assignment_tracker'],
            output_file='answers/assignments.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MIT AI Studio Class Schedule Assistant crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            embedder={
                "provider": "openai",
                "config": {
                    "model": "text-embedding-3-small"
                }
            }
        )