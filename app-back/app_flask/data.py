import pandas as pd

#corresponds to data/bargraph.png
#data from each state the total sum() of areakm deforested recorded. 
state = ['AP', 'TO', 'RR', 'AC', 'MT', 'PA', 'MA', 'AM', 'RO']
areakm = [14.846693, 207.443139, 2076.651661
, 2149.471324, 2434.997979, 4581.706136, 4881.302067
, 4965.805711, 8561.256673]
area_by_state = pd.DataFrame({'State': state, 'Area_km': areakm})

#corresponds to\data\ExponentionSmoothingForecastALLSTATES.PNG
#These are the results of the exponential smoothing model on the dataframe that was resampled yearly. It is all 9 states summed together. The prediction ranges from the years 2017-2026)
#The 2017 - 2019 will be taken out for WD team. Since they will also receive a dataframe of recorded past dates that includes 2008-2019
#Model is an exponential smoothing model
predicted_ESM_df=pd.read_csv('../../Data/BrazilESMy.csv', header=None)
predicted_ESM_df.drop(columns=predicted_ESM_df.columns[0], inplace=True)
#droping years 2017-2018, reseting index. 
predicted_ESM_df = predicted_ESM_df.iloc[4:]
predicted_ESM_df.reset_index(inplace=True)
predicted_ESM_df.drop(columns='index', inplace=True)


#Data from the PRODES dataset of recorded deforestation from years 2008-2019 for all 9 states in the Legal Amazonia. The areakm is a sum() of all states. 
recorded_areakm_df = pd.read_csv('../../Data/RecordedAreakm.csv', header=None)
recorded_areakm_df.drop(columns=recorded_areakm_df.columns[0], inplace=True)
#drop the header column
recorded_areakm_df = recorded_areakm_df.iloc[1:]


#combine the observed and predicted data together
frames = [recorded_areakm_df, predicted_ESM_df]
record_pred_df = recorded_areakm_df.append(predicted_ESM_df)
record_pred_df.reset_index(inplace=True)
record_pred_df.drop(columns='index', inplace=True)
record_pred_df.columns=['Year', 'Total_Area_km']
#print(record_pred_df)