#!/usr/bin/env python
import sys
import os
from datetime import datetime

# Add the src directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from twin_lite.crew import TwinLite

def display_welcome(current_date):
    """Display a friendly welcome message"""
    print("\n" + "="*60)
    print("🎓 Welcome to MIT AI Studio Class Schedule Assistant!")
    print("="*60)
    print("\nHello! I'm your personal AI assistant for MIT AI Studio Fall 2025.")
    print("I'm here to help you navigate your course schedule, research topics,")
    print("prepare for classes, and track your assignments.")
    print("\nI was created by Atahan Afsar, a fellow student who understands the")
    print("challenges of keeping up with this exciting but intensive course!")
    print("="*60)
    print(f"\n📅 Today's Date: {current_date}")
    print("-"*60)
    print("\nHow can I help you today?")

def display_menu():
    """Display the main menu options"""
    print("\n1. 📚 Get next class briefing")
    print("2. 🔍 Research a specific topic")
    print("3. 📝 Generate weekly preparation plan")
    print("4. 📋 Track assignments (Tech/Analyst)")
    print("5. 🚀 Run all tasks")
    print("6. 👋 Exit\n")

def display_goodbye():
    """Display a friendly goodbye message"""
    print("\n" + "="*60)
    print("👋 Thank you for using MIT AI Studio Class Schedule Assistant!")
    print("\nGood luck with your studies! Remember:")
    print("• Stay curious and keep learning")
    print("• Don't hesitate to experiment with AI agents")
    print("• Prepare well for Demo Day!")
    print("\nSee you next time! 🎓")
    print("="*60 + "\n")

def run_task(choice, current_date, schedule_path, preferences_path):
    """Run a specific task based on user choice"""
    inputs = {
        'current_date': current_date,
        'schedule_path': schedule_path,
        'preferences_path': preferences_path
    }

    if choice == '1':
        print("\n📚 Fetching next class information...\n")
        crew = TwinLite().crew()
        crew.tasks = [crew.tasks[0]]  # Only run next_class_briefing task

    elif choice == '2':
        topic = input("\nEnter the topic to research (e.g., 'Agentic Web', 'AI Agents'): ").strip()
        if not topic:
            topic = "AI Agents"
        inputs['topic'] = topic
        print(f"\n🔍 Researching: {topic}...\n")
        crew = TwinLite().crew()
        crew.tasks = [crew.tasks[1]]  # Only run topic_primer task

    elif choice == '3':
        print("\n📝 Creating weekly preparation plan...\n")
        crew = TwinLite().crew()
        crew.tasks = [crew.tasks[2]]  # Only run weekly_preparation task

    elif choice == '4':
        track = input("\nWhich track? (Tech/Analyst): ").strip().title()
        if track not in ['Tech', 'Analyst']:
            track = 'Tech'
        inputs['track'] = track
        print(f"\n📋 Tracking {track} Track assignments...\n")
        crew = TwinLite().crew()
        crew.tasks = [crew.tasks[3]]  # Only run assignment_tracker task

    elif choice == '5':
        topic = input("\nEnter a topic to research (or press Enter for 'AI Agents'): ").strip()
        if not topic:
            topic = "AI Agents"
        track = input("Which track for assignments? (Tech/Analyst): ").strip().title()
        if track not in ['Tech', 'Analyst']:
            track = 'Tech'
        inputs['topic'] = topic
        inputs['track'] = track
        print("\n🚀 Running all tasks...\n")
        crew = TwinLite().crew()

    else:
        return False  # Invalid choice

    # Run the crew
    try:
        result = crew.kickoff(inputs=inputs)
        print("\n" + "="*60)
        print("✅ Task completed successfully!")
        print("="*60)
        print("\nResults have been saved to: ./twin_lite/answers/")

        # Display the result
        if result:
            print("\n📊 Output Preview:")
            print("-"*60)
            # Show first 500 characters of the result
            result_str = str(result)
            if len(result_str) > 500:
                print(result_str[:500] + "...\n[Output truncated. Check output files for full results]")
            else:
                print(result_str)
        return True

    except Exception as e:
        print(f"\n❌ Error running the crew: {e}")
        import traceback
        traceback.print_exc()
        return False

def run():
    """
    Run the MIT AI Studio Class Schedule Assistant crew with interactive loop.
    """
    # Get current date for context
    current_date = datetime.now().strftime("%m/%d/%Y")

    # Get absolute paths
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    schedule_path = os.path.join(base_path, "data", "schedule.csv")
    preferences_path = os.path.join(base_path, "knowledge", "user_preference.txt")

    # Display welcome message
    display_welcome(current_date)

    # Main interaction loop
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == '6':
            # Exit option
            display_goodbye()
            break
        elif choice in ['1', '2', '3', '4', '5']:
            # Run the selected task
            success = run_task(choice, current_date, schedule_path, preferences_path)

            if success:
                # Ask if user wants to continue
                print("\n" + "-"*60)
                print("\n🤔 Is there anything else I can help you with?")
                #continue_choice = input("\nPress Enter to continue or type 'exit' to quit: ").strip().lower()
                #if continue_choice == 'exit':
                #    display_goodbye()
                #    break
        else:
            print("\n❌ Invalid choice. Please select a number between 1 and 6.")

def train():
    """
    Train the crew for a given number of iterations.
    """
    print("\n" + "="*60)
    print("🎓 Training Mode - MIT AI Studio Assistant")
    print("="*60 + "\n")

    try:
        n_iterations = int(input("Enter the number of training iterations: "))

        current_date = datetime.now().strftime("%m/%d/%Y")
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        schedule_path = os.path.join(base_path, "data", "schedule.csv")
        preferences_path = os.path.join(base_path, "knowledge", "user_preference.txt")

        inputs = {
            'current_date': current_date,
            'schedule_path': schedule_path,
            'preferences_path': preferences_path,
            'topic': 'AI Agents',
            'track': 'Tech'
        }

        print(f"\n🔄 Training for {n_iterations} iterations...")
        TwinLite().crew().train(n_iterations=n_iterations, inputs=inputs)
        print("\n✅ Training completed!")

    except Exception as e:
        print(f"\n❌ An error occurred during training: {e}")
        import traceback
        traceback.print_exc()

def replay():
    """
    Replay the crew execution from a specific task.
    """
    print("\n" + "="*60)
    print("🔄 Replay Mode - MIT AI Studio Assistant")
    print("="*60 + "\n")

    try:
        task_id = input("Enter the task ID to replay from: ")

        current_date = datetime.now().strftime("%m/%d/%Y")
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        schedule_path = os.path.join(base_path, "data", "schedule.csv")
        preferences_path = os.path.join(base_path, "knowledge", "user_preference.txt")

        inputs = {
            'current_date': current_date,
            'schedule_path': schedule_path,
            'preferences_path': preferences_path,
            'topic': 'AI Agents',
            'track': 'Tech'
        }

        print(f"\n▶️ Replaying from task {task_id}...")
        TwinLite().crew().replay(task_id=task_id, inputs=inputs)
        print("\n✅ Replay completed!")

    except Exception as e:
        print(f"\n❌ An error occurred during replay: {e}")
        import traceback
        traceback.print_exc()

def test():
    """
    Test the crew with different scenarios.
    """
    print("\n" + "="*60)
    print("🧪 Test Mode - MIT AI Studio Assistant")
    print("="*60 + "\n")

    current_date = datetime.now().strftime("%m/%d/%Y")
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    schedule_path = os.path.join(base_path, "data", "schedule.csv")
    preferences_path = os.path.join(base_path, "knowledge", "user_preference.txt")

    inputs = {
        'current_date': current_date,
        'schedule_path': schedule_path,
        'preferences_path': preferences_path,
        'topic': 'Multimodal AI',
        'track': 'Tech'
    }

    try:
        print("🔬 Running test with sample inputs...")
        print(f"   - Current Date: {current_date}")
        print(f"   - Topic: Multimodal AI")
        print(f"   - Track: Tech\n")

        # Test with just the first task
        crew = TwinLite().crew()
        crew.tasks = [crew.tasks[0]]  # Only test next_class_briefing
        result = crew.test(inputs=inputs)

        print("\n✅ Test completed successfully!")
        print("\n📊 Test Results:")
        print("-"*60)
        print(str(result)[:500] + "..." if len(str(result)) > 500 else str(result))

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "train":
            train()
        elif command == "replay":
            replay()
        elif command == "test":
            test()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: run, train, replay, test")
    else:
        run()