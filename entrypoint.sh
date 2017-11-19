#!/bin/bash

# Exit for non-null responses
set -e 

# Set production environment
export DEBUG=

# Execute the process
python manage.py runserver