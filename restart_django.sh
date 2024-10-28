#!/bin/bash

# Kill any running Django server processes
echo "Killing Django server processes..."
pkill -f "manage.py runserver"

# Navigate to the Django project directory and restart the Django server
echo "Starting Django backend server..."
cd /Users/nur/Workspace/learningBuddyAgentAI/language_buddy
nohup python manage.py runserver 0.0.0.0:8000 &

echo "Django backend server has been restarted."

# Tail the Django logs
echo "Tailing Django logs..."
tail -f /Users/nur/Workspace/learningBuddyAgentAI/language_buddy/logs/django.log
