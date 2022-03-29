import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print (os.getcwd())
print (os.listdir())
covid_data = pd.read_csv("full_data.csv")
print (covid_data.head(5))
print (covid_data.info())
print (covid_data.describe())
#the mean of new cases is 194.546773, the standard deviation is 2083.395028
#the range of total cases is range from 0 to 777798
#print (covid_data.iloc[0,1])
#print (covid_data.iloc[2,0:5])
#print (covid_data.iloc[0:2,:])
#print (covid_data.iloc[0:10:2,0:5])
print (covid_data.iloc[10:21,0:3:2])
#my_columns = [True,True,False,True,False,False,False]
#it will warn you that my_columns length is not correct.
#print (covid_data.iloc[0:3,my_columns])
#print (covid_data.loc[2:4,"date"])
#my_columns = [False,True,False,False,True,False]
print (covid_data.loc[0:81,"total_cases"])
#for i in range (0,7995):
    #if covid_data.loc[i,"location"]=="Afghanistan":
       #print (covid_data.loc[i,"total_cases"])
location=covid_data.iloc[0:,1]
print (covid_data.loc[location=="Afghanistan","total_cases"])
