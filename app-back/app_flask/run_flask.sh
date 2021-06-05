#! /bin/bash
PWD=$(pwd)
FOLDER="/python"

if grep "$FOLDER" <<< "$PWD"
then 
    echo "starting up venv..."
    source venv/bin/activate
    echo "starting up server.."
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
else
    echo "wrong folder. Are you in the birds_ai/pyhton folder?"
    echo "here is your current folder: ${PWD}"
fi
