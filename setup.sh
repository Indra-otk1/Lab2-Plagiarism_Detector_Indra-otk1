#!/bin/bash
# setup.sh - create folders and the setup log

# Use '>>' to append the log start time
echo "---- Setup started on the $(date) ----" >> setup.log

# Create the required directories. The -p flag ensures they are created if they don't exist,
# and suppresses errors if they already do.
mkdir -p essays reports

# Check if the directories were created successfully and log the result
if [ $? -eq 0 ]; then
    echo "Successfully created directories: essays, reports" >> setup.log
else
    echo "Error: Failed to create one or more directories." >> setup.log
fi

# Final completion message
echo "Setup complete!" >> setup.log
echo "---- End of log ----" >> setup.log

# Output the success message to the console
echo "Setup successfully completed! Directories created: essays and reports. Check setup.log for details."
