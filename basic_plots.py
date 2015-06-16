
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt


# data is a pandas dataframe with column names: sym, size, total, etc

# below are plots for ... scatter, bar, and histogram plots



# the scatter plot
plt.scatter(data['size'], data['total'])

# limits
plt.ylim(0,12000)
plt.xlim(0,160)

# titles and labels
plt.title("Title of the Plot")
plt.ylabel("Y-axis of the Plot")
plt.xlabel("X-axis of the Plot")

plt.show()
plt.close()




# the x data
syms = data['sym']
xpos = [ i + 0.5 for i,element in enumerate(list(syms)) ]

# the bar plot
plt.bar(xpos, data['total'])

# the x ticks and rotation
plt.xticks( [i + 0.9 for i,element in enumerate(syms)], syms )
plt.setp(plt.xticks()[1], rotation=45)

# titles and labels
plt.title("Title of the Plot")
plt.ylabel("Y-axis of the Plot")
plt.xlabel("X-axis of the Plot")

plt.show()
plt.close()


print 'blaa'

# the histogram
plt.hist(grades, bins=10)
plt.axis([-5,105,0,5])

# titles and labels
plt.title("Title of the Plot")
plt.ylabel("Y-axis of the Plot")
plt.xlabel("X-axis of the Plot")

plt.show()
plt.close()