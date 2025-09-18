# MIT AI Studio Class Schedule Assistant

**Atahan Afsar, Tech track**

A multi-agent CrewAI system that helps MIT AI Studio Fall 2025 students manage their course schedule, research topics, and track assignments.

## Features

- 📚 **Next Class Briefing**: Get details about upcoming classes, speakers, and homework
- 🔍 **Topic Research**: Research class topics with primers and background information
- 📝 **Weekly Planning**: Generate personalized preparation plans for the week ahead
- 📋 **Assignment Tracking**: Track Tech/Analyst track homework and deadlines
- 🤖 **Student Persona**: Agents embody a helpful fellow student perspective

## Setup

### Prerequisites
- Python 3.11+
- OpenAI API key (for CrewAI agents)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aafsar/digital-twin-lite.git
cd twin_lite
```

2. Install dependencies using uv:
- If `uv` is not already installed, see here for installation steps: https://docs.astral.sh/uv/getting-started/installation/
- Then, run the following command:
```bash
uv sync
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY="your-api-key-here"
# Optional: For web research
export SERPER_API_KEY="your-serper-key"
```

## Usage

### Interactive Mode (Default)
```bash
uv run twin_lite
```

The assistant will greet you and present options:
1. Get next class briefing
2. Research a specific topic
3. Generate weekly preparation plan
4. Track assignments (Tech/Analyst)
5. Run all tasks
6. Exit

### Command-Line Modes
```bash
# Training mode
uv run twin_lite train

# Test mode
uv run twin_lite test

# Replay mode
uv run twin_lite replay
```

### Output Files
All generated content is saved to `./twin_lite/answers/`:
- `next_class.md` - Next class briefing
- `topic_primer.md` - Topic research results
- `weekly_plan.md` - Weekly preparation plan
- `assignments.md` - Assignment tracking

## Project Structure
```
twin_lite/
├── src/twin_lite/
│   ├── config/
│   │   ├── agents.yaml    # Agent definitions
│   │   └── tasks.yaml      # Task configurations
│   ├── crew.py            # Crew orchestration
│   └── main.py            # Entry point
├── knowledge/
│   └── user_preference.txt # User preferences
├── answers/               # Generated outputs
└── data/
    └── schedule.csv       # Course schedule data
```

## Agents

1. **Schedule Navigator**: Expert in course timeline and scheduling
2. **Topic Researcher**: Researches class topics and speakers
3. **Study Coordinator**: Creates personalized study plans

## Customization

Edit `knowledge/user_preference.txt` to personalize:
- Your track (Tech/Analyst)
- Learning style preferences
- Study schedule
- Areas of interest

## Notes

- The system uses the current date to identify upcoming classes
- Memory persists between tasks for context retention
- All agents use FileReadTool to access schedule data
- Web research requires Serper API key

## Learning outcomes
It was a fun exercise. One thing that did not work for me is the CSVSearchTool, which kept giving me errors. CrewAI's website notes that it is still an experimental tool. Thus I switched to File Reader Tool.

## Author

Created by Atahan Afsar for MIT AI Studio Fall 2025