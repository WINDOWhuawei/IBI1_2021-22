import numpy as np
import matplotlib.pyplot as plt
n=8
marks=[45,36,86,57,53,92,65,45]
#Import Rob's score into list marks
score=np.array(marks)
#Create an array named Score and import the data from marks
plt.boxplot(score,
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
#From the boxplot we can find that the mean value of marks is lower than 60.
#So it doesn't higher than the pass mark of 60%.

