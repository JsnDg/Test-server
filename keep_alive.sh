#!/bin/bash

# Name of the process to check
PROCESS_NAME=app.py

# Find the process by name and count the number of occurrences
PROCESS_COUNT=$(ps aux | grep $PROCESS_NAME | grep -v grep | wc -l)

# If the process is not running
if [ $PROCESS_COUNT -eq 0 ]; then
    # Navigate to your Flask app directory (update this path)
    cd /

    # Activate your virtual environment if you have one (optional)
    # source /path/to/venv/bin/activate

    # Start the Flask app
    python $PROCESS_NAME > /dev/null 2>&1 &
fi