import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from bagpy  import bagreader
import math

#movbgfree=bagreader('/home/sriram/EECE5554/LAB2/src/data/moving free/2022-10-06-19-00-49.bag')
movbgoccl=bagreader('/home/sriram/EECE5554/LAB2/src/data/moving_occluded/2022-10-06-20-03-09.bag')

#movfree = movbgfree.message_by_topic('/gps')
movoccl = movbgoccl.message_by_topic('/gps')

df = pd.read_csv(movoccl)
#df = pd.read_csv(movfree)

x = df["UTM_northing"]
y = df["UTM_easting"]
x = df["UTM_northing"].values[:,np.newaxis]
y = df["UTM_easting"].values
x_values = x[0:] - x.min()
y_values = y[0:] - y.min()


#1st part
x_values_length = x_values[0:60]
y_values_length = y_values[0:60]

model = LinearRegression()
model.fit(x_values_length,y_values_length)

p_value = model.predict(x_values_length)
r_sq = model.score(x_values_length,y_values_length)
mse = mean_squared_error(y_values_length,p_value)
rmse = math.sqrt(mse)
print(rmse)
plt.xlabel('UTM northing')
plt.ylabel('UTM easting')
plt.scatter(x_values,y_values)
plt.plot(x_values_length,p_value)

#2nd part
x_values_breadth = x_values[60:71]
y_values_breadth = y_values[60:71]

model = LinearRegression()
model.fit(x_values_breadth,y_values_breadth)

p_value = model.predict(x_values_breadth)
r_sq = model.score(x_values_breadth,y_values_breadth)
mse = mean_squared_error(y_values_breadth,p_value)
rmse = math.sqrt(mse)
print(rmse)

plt.plot(x_values_breadth,p_value)

#3rd part
x_values_length1 = x_values[71:106]
y_values_length1 = y_values[71:106]

model = LinearRegression()
model.fit(x_values_length1,y_values_length1)

p_value = model.predict(x_values_length1)
r_sq = model.score(x_values_length1,y_values_length1)
mse = mean_squared_error(y_values_length1,p_value)
rmse = math.sqrt(mse)
print(rmse)
plt.scatter(x_values,y_values)
plt.plot(x_values_length1,p_value)


#2nd part
x_values_breadth = x_values[106:127]
y_values_breadth = y_values[106:127]

model = LinearRegression()
model.fit(x_values_breadth,y_values_breadth)

p_value = model.predict(x_values_breadth)
r_sq = model.score(x_values_breadth,y_values_breadth)
mse = mean_squared_error(y_values_breadth,p_value)
rmse = math.sqrt(mse)
print(rmse)

plt.plot(x_values_breadth,p_value)
plt.title("WALKING DATA OCCLUDED")




plt.show()

