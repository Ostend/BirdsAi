#! /bin/bash
PWD=$(pwd)
echo "This is your current path ${PWD}"
PYTHON=$(which python)
FOLDER="app-back/app_flask"
BOLD=$(tput bold)
GREEN=`tput setaf 2`
RED=`tput setaf 1`
if [ -x "${PYTHON}" ]
then
    echo "$(which python)"
    echo "you have python!"
else
    echo "${RED}no python detected. Install python to run."
fi
#install depedencies
if grep "$FOLDER" <<< "$PWD"
then
    echo ">>preparing to install VENV and FLASK..."
    python3 -m venv venv
    echo ">>activating environment..."
    source venv/bin/activate
    echo ">>installing Flask..."
    pip install Flask
    echo ">>installing dependencies..."
    pip install pandas
    pip install geopandas
    deactivate
    echo "Successful!"
    echo "	to start the Flask server follow these commands:"
    echo "	${GREEN}source /venv/bin/activate"
    echo "	export FLASK_APP=app.py;export FLASK_ENV=development;flaskrun"
else
    echo "${RED}not in correct directory. Make sure you are in the python folder of the birdsAI project."
fi

