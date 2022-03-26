import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.linear_model import LinearRegression

cases_data = pd.read_csv("src\model\Ydata - united_states_covid19_cases_deaths_and_testing_by_state (2).csv")
# Percent Positive Last 7 Days
PositiveSD = cases_data[['State/Territory', '% Positive Last 7 Days']]
PositiveSD = PositiveSD.rename(columns={'% Positive Last 7 Days' : 'PositiveLSD'})
PositiveSD = PositiveSD[PositiveSD.PositiveLSD.notnull()]
wastewater_data = pd.read_csv("src\model\NWSS_Public_SARS-CoV-2_Wastewater_Data - NWSS_Public_SARS-CoV-2_Wastewater_Data.csv")
filtered_wastewater = wastewater_data[(wastewater_data['date_start'] > '2022-03-00')]
filtered_wastewater = filtered_wastewater[['wwtp_jurisdiction', 'ptc_15d']] #'date_start', 'date_end'
filtered_wastewater = filtered_wastewater[filtered_wastewater.ptc_15d.notnull()]
filtered_wastewater = filtered_wastewater.groupby('wwtp_jurisdiction').mean().reset_index()
filtered_wastewater = filtered_wastewater.rename(columns={'wwtp_jurisdiction' : 'State/Territory'})
df = pd.merge(PositiveSD,filtered_wastewater,on="State/Territory")
df = pd.read_csv("src\model\out.csv")
X = df["ptc_15d"].to_numpy().reshape(-1,1)
y = df["PositiveLSD"].to_numpy()
model = LinearRegression()
model.fit(X, y)
r_sq = model.score(X, y)
intercept = model.intercept_
slope = model.coef_
