import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data=pd.read_csv("full_data.csv")
location=covid_data.iloc[0:,1]
my_columns=[True,False,True,False,True,False]
print (covid_data.loc[location=="India",my_columns])
india_new_cases=covid_data.loc[location=="India","new_cases"]
india_total_cases=covid_data.loc[location=="India","total_cases"]
india_dates=covid_data.loc[location=="India","date"]
plt.plot(india_dates,india_new_cases,'b+')
plt.xticks(india_dates.iloc[0:len(india_dates):4],rotation=-90)
plt.show()
