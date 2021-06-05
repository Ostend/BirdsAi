# BirdsAi
An exploration of deforestation in Brazil. </br> 
This is a personal exploration of using data science and folium to create a React-Flask app. </br>
I am currently exploring the [Prodes dataset](https://data.globalforestwatch.org/datasets/gfw::prodes-deforestation-in-amazonia/about). </br>
![areakmState](https://user-images.githubusercontent.com/60686512/120898615-e3a3fa80-c62b-11eb-80c6-d9a5cd74638f.PNG)
Map represents the amount of areakm deforested per state in Legal Amazonia. Data collected from 2008-2019. Color scheme is Yellow to Red. 

## Installation
At the moment, this is not deployed. <br>
To install the Flask app on your local computer, navigate into the /app-back/app_flask directory. <br>
In this directory, there are two bash script files. 
To verify that python is on your local computer and to install the correct dependencies run these commands: <br>
```bash 
chmod +x install_FLASK.sh 
```
```bash 
./install_FLASK.sh 
```

***For a short cut to run the Flask server:*** <br>
run this command ***only once***: <br>
```bash
chmod +x run_flask.sh
``` 

Then, ***everytime*** you would like to start up the Flask server (as well as enter the virtual environment), run this commad:
```bash
./run_flask.sh
```

## Data
In the /Data directory, visualizations from the data explored in the Prodes dataset are provided. 
![ExponentionSmoothingForecastALLSTATES](https://user-images.githubusercontent.com/60686512/120893334-0aa20280-c613-11eb-9236-7fb660866744.PNG)
