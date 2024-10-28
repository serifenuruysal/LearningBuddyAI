#!/bin/bash

# Navigate to the React frontend directory
cd /Users/nur/Workspace/learningBuddyAgentAI/frontend

# Clean the React app by removing the build folder
echo "Cleaning React app..."
rm -rf build/

# Restart the React app
echo "Starting React app..."
nohup npm start &

echo "React app has been restarted."

# Tail the React logs
echo "Tailing React logs..."
tail -f /Users/nur/Workspace/learningBuddyAgentAI/frontend/logs/react.log
