## All Data results, visualizations, and csv files can be found here. 
# Data Science- a look into time series

**Stephanie Mennear
July 11th 2021**

> [Prodes dataset](https://data.globalforestwatch.org/datasets/gfw::prodes-deforestation-in-amazonia/about) </br>

The prodes dataset offers insight into the deforestation rates of the Legal Amazonia in Brazil. It logs datapoints from all nine countries in which the amazon forest resides. The data points are generated from satelite images, spanning from the years 2008 to 2019.

While exploring the dataset, I observed a pattern of time and forest loss. I decided then to explore the path of time series predictions.

**Hypothesis**: Deforestation rates, that are measured in areakm, grow yearly.

> Follow up questions: Discover the method of rate- linear, exponential..etc. If pattern in rate of deforestaion is confirmed, can I create a model that predicts the future rate of deforestation?
> <br>

##### Version 1:

> Data prep:

To test the reate of deforestation yearly, the prodes dataset was processed in preperation for a time series.

Due to the nature of the weather and cloud coverage over the Amazon rainforest, satelite images of deforestaion are not recorded consitently, i.e. many dates are missing due to unsuable satelite images.

<!--Becuase of the rainy seasons in the Amazon, the Prodes imaging data was sporatically taken from the months of Aug-Nov from years 2008-2019 for 9 unique states in Brazil. A time series forecast would not be possible with the current state of the dataset. -->

Because the clouds obstruct the image of the satellite data, there are no consistent patterns for date ranges that the data is collected.

From observing the dataset, most of the satellite images are taken from August - September, which are the months of the year that the Amazon is not mostly covered by clouds. It is during this time, that the satellite images can be taken for evaluation.

To prepare for forecasting, the dataset is sperated into the unique states and organized and seperated by year into new dataframes. The dates are reindexed as a date time index.

Each respective new dataframe is then reformated to cover the span of a year, without losing or adding any values to the origional data.

The intention is to look at data from a yearly perspective. Thus, the method of preparing the data and the reason the data should not be used for any other purpose as it could give the user false information.
<br>

### Methods:

_below all of the data, unless otherwise stated, is using the singular state of Amazonas_
**Testing for white noise, stationary, non-stationary**

- The first step to visualize the type of time series data is to use the `seasonal_decompose` method from `statsmodels`.

  - Multiplicative:
    ![multiplicativesd](https://user-images.githubusercontent.com/60686512/125081562-7110b980-e0c6-11eb-8f9e-1676cf91948a.png)
  - Additive:
    ![additivesd](https://user-images.githubusercontent.com/60686512/125081698-96052c80-e0c6-11eb-8fc7-7da0b485ba1f.png)

  * The above figure uses seasonal_decompose to visualize if there are any trends in the time series. Specifically, this is using the data for the state of Amazonas, years from 2008-2019.
    Observing data from the seasonal_decompose method, there is reason to beleive there are no trends and in addition that the time series could be white noise. <br>

- The next step is to look at the **autocorrelation** of the datapoints. Auto correlation results can show whether the data is positivly, negativly, or independant of itself (i.e time vs areakm)

  ![autocorrelation](https://user-images.githubusercontent.com/60686512/125081757-a61d0c00-e0c6-11eb-9b6c-a91a2bff85e7.png)

  - The above `lag_plot` verifies whether a time series is random. Based on the visualization, it provides more confimation that time series could be white noise.

- Next is to look at the `acf_plot`
- 
 ![autocorrelationa](https://user-images.githubusercontent.com/60686512/125081805-b634eb80-e0c6-11eb-820c-9cec38332b9e.png)

  - The above plot visualizes whether the data has correlation; do variables act independently of one another. As with the `lag_plot`, this plot confirms that there is no correlation as well as no seasonality.
    Simarlary, the pacf plot resembles the acf plot.
    <br>

- As a last method to understand the data, the Augmended Dickey-Fuller (ADF) Test was applied. This is to understand further if the time series is stationary or non stationary. By doing this, it will further confirm that the dataset is sationary, and possibly white noise. The results of the ADF test for the time series are:

        Augmented Dickey-Fuller Test:
        ADF test stats           -1.756014e+01
        p-value                   4.100536e-30
        number of lags used       5.400000e+01
        number of observations    3.939200e+04
        critical value (1%)      -3.430516e+00
        critical value (5%)      -2.861613e+00
        critical value (10%)     -2.566809e+00
        Strong evidence against null hypthesis.
        Reject null hypothesis.
        Data has no unit root and is stationary

##### At this point, the data set is not ideal for time series forecasting.

#### Version 2:

> Data prep:

After looking at the satellite images, I came to the discovery that the areakm data points detailed the measurment of deforestation from the previous year. Therefore, after the data is cleaned, the cummulative sum is the value the time series forecast model will use.

To adjust the methods to test the hypothesis, instead of using the data points of the areakm recorded each year, the cummulative sum is calculated and added to the dataframe.

From here, I repeated all the above steps, but with cummulative sum instead of independent data points.

- Plot of cummulative areakm values (y) and time (x):
- 
  ![amlineplot](https://user-images.githubusercontent.com/60686512/125081837-c3ea7100-e0c6-11eb-8e53-8b8876f88993.png)

  - Visualized here is a better look at the trends of deforestation.

- the `seasonal_decompose` visualizations using the time series.  
   ![ammonthsd](https://user-images.githubusercontent.com/60686512/125081886-d49ae700-e0c6-11eb-922a-2ca299eef93b.png)
  - Here it shows strong seasonality and clear trends. The residual is not as strong as in version 1.
- ADF results:
  > Augmented Dickey-Fuller Test:
  > ADF test stats -3.087875
  > p-value 0.027464
  > number of lags used 0.000000
  > number of observations 4382.000000
  > critical value (1%) -3.431843
  > critical value (5%) -2.862200
  > critical value (10%) -2.567121
  > Strong evidence against null hypthesis.
  > Reject null hypothesis.
  > Data has no unit root and is stationary

##### Before moving forward, and testing/refining models, I wanted to verify if the trends are similar in all states. Attempted models can be seen in the collab notebook under section "CUMMALATIVE SUM--> text train split". Please refer to this section to view failed attempts with ARIMA, SARIMA models.

As my method stands, I have seperated all the states into individual dataframes, to predict time series on each state. At this point, I did not think whether the states would have different trends or not. (As up to this point, I've only been using the dataframe for the state of Amazonas).

- Plotting the line plots of areakm cummulative sum vs time:
- 
  ![cumsumallStates](https://user-images.githubusercontent.com/60686512/125081932-debce580-e0c6-11eb-8fc5-186c33a367dd.png)
  
  - Shown here, all of the trends for the cummulative sum of area deforested from 2008-2019 = each state has different rates of deforestation. At this point, I realize that I would have to fit models to each individual state, or I would have to start over and user all states together. Due to time limitations, I decide to go for the latter.

##### Version 3:

> Data Prep:

To further adjust to the time series, I added all the states into one dataframe. To note, the cummulative areakm value is the value of measurement.

In order to prepare the dataset for the time series forecast model, the data must be prepared with a datetime index, as well as the data points to fit the date time index. Because of the inconsistant data points (due to cloud cover), the redisturbution method works as follows:

1. The data points for each specific state of each specific year are redistributed to fit 365 days.
2. The left over rows that did not fit into 365 days are summed, and divided amoung the 356 rows evenly. This means- each row value is added with the divided remaining value. This was to keep the integrity of the total amount of areakm that was deforested, and to prepare the dataset for yearly forecasting.
3. Due to the method that it was distubuted, no daily, or monthly trends should be observed. Only yearly.

Time series predictions:
The model that was the most successful is an exponential smoothing model that predicts rates until 2026.
I split the dataset (`df_y`) into test and train. For a recap, the dataset being used is the cummulative sum of areakm deforested of every state indexed by year. The time series starts from 2008 and ends at 2019.
Below is the model.

```bash
train_yearly = df_y.iloc[:9]
test_yearly = df_y.iloc[8:]
fitted_model = ExponentialSmoothing(train_yearly['cumsum'], trend='mul', seasonal_periods=1).fit()
test_predictions = fitted_model.forecast(10)
```

Visualized:

```bash
train_yearly['cumsum'].plot(figsize=(12,5), legend=True, label='Train')
test_yearly['cumsum'].plot(legend=True, label='Test')
test_predictions.plot(legend=True, label='Prediction')
plt.title('Predictions from 2017 - 2026 \nAreakm of total deforestation \n All 9 State of Legal Amazonia', fontsize=20)
plt.xlabel('Years', fontsize=12)
plt.ylabel('Areakm total deforestation', fontsize=12)
```

![ExponentionSmoothingForecastALLSTATES](https://user-images.githubusercontent.com/60686512/125075938-8c2bfb00-e0bf-11eb-8b4e-222d9f3f5687.PNG)

Based on patterns and observed trends from the last 12 years, it is projected\* that every year, 12 percent more of the current rainforest disappears due to farming. This means that if rates do not slow down, by 2026 we will see an increase of almost 200% the amount of deforestation rates that we currently see in 2020.

Accoring to `Philip Fearnside, a scientist at Brazil’s National Institute of Amazonian Research in Manaus*`, in and interview with [Sciencemag.org](https://www.sciencemag.org/news/2019/11/brazil-s-deforestation-exploding-and-2020-will-be-worse):

> "The deforestation rate in the following months exploded to levels far above those for the same months in the previous year [according to DETER data], reaching 222% above the 2018 value in August. This part of the Bolsonaro effect will only be reflected in the PRODES numbers that will be released a year from now."

\*quoted from the above article

### Visualizations

Independent of the timeseries data visualization, using the same Prodes dataset, I visualized the rates of deforestation by State, as discovered that each state is impacted differently.

- Using the areakm values (not the cumsum() values as in the time series method) the total amount of deofrested areakm for each state over the total years 2008-2019 are calculated.

```bash
state_area = df.groupby(by='STATE')['AREA_KM'].sum().sort_values(ascending=False).reset_index()
state_area = state_area.sort_values(by='AREA_KM', ascending=True)
```

Visualized:

![bargraph](https://user-images.githubusercontent.com/60686512/125077457-67d11e00-e0c1-11eb-83f6-780830074f86.png)

Some articles explaining the data:
[WWF on deforested states in Brazilian Amazon](https://www.wwf.org.co/en/?2342/Brazilian-Amazon-environmental-awareness-higher-in-deforested-areas)

> "Rondonia, the most deforested Amazonian state, has lost 31 percent of its forests and most of the remaining areas are degraded.
> This is similar to what happened in Pará, the second most deforested state in the Amazon region, with 18 percent of its forests having been lost."

##### An overall view:

Below is a visualization of every each state's areakm deforestation rates plotted from 2008 - 2019.

![areakm_trends_alltimes](https://user-images.githubusercontent.com/60686512/125079357-cac3b480-e0c3-11eb-9d28-782ba46c0655.png)

- From this visualization, 2008 is extremley high, while, for the most part, trends dip from 2009 - 2017.
- Discovering from research, Brazil saw a decline in deforestation rates from 2008 to around 2018.
  According to an article published November 2020 by [BBC](https://www.bbc.com/news/world-latin-america-55130304), in collaboration with Prodes data:
  > "Amazon deforestation highest since 2008"

Why? [BBC](https://www.bbc.com/news/world-latin-america-55130304) states:

> "Scientists say it has suffered losses at an accelerated rate since Jair Bolsonaro took office in January 2019.
> The Brazilian president has encouraged agriculture and mining activities in the world's largest rainforest."
