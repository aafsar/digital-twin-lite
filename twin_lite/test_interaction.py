#!/usr/bin/env python
"""Test script to verify the interaction flow without running actual CrewAI tasks"""
import sys
import os
sys.path.insert(0, 'src')

from twin_lite.main import display_welcome, display_menu, display_goodbye
from datetime import datetime

# Test welcome message
print("=== Testing Welcome Message ===")
display_welcome()

# Test menu display
print("\n=== Testing Menu Display ===")
current_date = datetime.now().strftime("%m/%d/%Y")
display_menu(current_date)

# Test goodbye message
print("\n=== Testing Goodbye Message ===")
display_goodbye()

print("\n✅ All display functions working correctly!")