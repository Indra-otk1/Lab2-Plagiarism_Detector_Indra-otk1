#!/bin/bash
# setup.sh - create folders and the setup log

echo "---- Setup started on the $(date) ----" >> setup.log

mkdir -p essays reports

echo "successfully created directories: essays, reports" >> setup.log
echo "Setup complete!" >> setup.log
echo "---- End of log ----" >> setup.log
echo "Setup successfully completed!"
