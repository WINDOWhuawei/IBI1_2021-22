import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("china_new_data.csv")
print (np.average(covid_data.iloc[0:,2]))
print (np.average(covid_data.iloc[0:,3]))
new_cases=np.array(covid_data.iloc[0:,2])
new_deaths=np.array(covid_data.iloc[0:,3])
plt.boxplot(new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
              )
plt.show()
plt.boxplot(new_deaths,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
             )
plt.show()
china_dates=covid_data.iloc[0:,0]
china_new_cases=covid_data.iloc[0:,2]
china_new_deaths=covid_data.iloc[0:,3]
plt.plot(china_dates,china_new_cases,'b+')
plt.plot(china_dates,china_new_deaths,'r+')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.show()
