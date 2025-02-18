#!/bin/bash

# Install necessary dependencies
pip install -r requirements.txt

# Set up the database
python setup_db.py

# Export environment variables
export $(grep -v '^#' .env | xargs)

# Run initial migration (if applicable)
python migrate.py

# Start the application
python app.py
