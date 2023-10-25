import bagpy
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, linspace
import matplotlib.pyplot as plt
from bagpy  import bagreader
import pandas as pd
import math  


movbgfree=bagreader('/home/sriram/EECE5554/LAB2/src/data/moving free/2022-10-06-19-00-49.bag')
statbgfree=bagreader('/home/sriram/EECE5554/LAB2/src/data/stationary free/2022-10-06-18-46-46.bag')
movbgoccl=bagreader('/home/sriram/EECE5554/LAB2/src/data/moving_occluded/2022-10-06-20-03-09.bag')
statbgoccl=bagreader('/home/sriram/EECE5554/LAB2/src/data/stationary_occluded/2022-10-06-19-48-32.bag')

movfree = movbgfree.message_by_topic('/gps')
statfree = statbgfree.message_by_topic('/gps')
movoccl = movbgoccl.message_by_topic('/gps')
statoccl = statbgoccl.message_by_topic('/gps')

df_movfree = pd.read_csv(movfree)
df_statfree = pd.read_csv(statfree)
df_movoccl = pd.read_csv(movoccl)
df_statoccl = pd.read_csv(statoccl)

df_statfree['UTM_northing_std']= df_statfree['UTM_northing']- df_statfree['UTM_northing'].min()
df_statfree['UTM_easting_std']= df_statfree['UTM_easting']- df_statfree['UTM_easting'].min()

df_statoccl['UTM_northing_std']= df_statoccl['UTM_northing']- df_statoccl['UTM_northing'].min()
df_statoccl['UTM_easting_std']= df_statoccl['UTM_easting']- df_statoccl['UTM_easting'].min()

df_movfree['UTM_northing_std']= df_movfree['UTM_northing']- df_movfree['UTM_northing'].min()
df_movfree['UTM_easting_std']= df_movfree['UTM_easting']- df_movfree['UTM_easting'].min()

df_movoccl['UTM_northing_std']= df_movoccl['UTM_northing']- df_movoccl['UTM_northing'].min()
df_movoccl['UTM_easting_std']= df_movoccl['UTM_easting']- df_movoccl['UTM_easting'].min()

#print(df_movfree['UTM_northing'].min())
#print(np.where( df_movfree['UTM_northing'] == df_movfree['UTM_northing'].min()))
#trueeasting=328121.11-df_statfree['UTM_easting'].min()
#truenorthing=4689434.40-df_statfree['UTM_northing'].min()

'''df_statfree[['UTM_easting_std','UTM_northing_std']].plot.scatter(x='UTM_easting_std',y='UTM_northing_std')
plt.xlabel("UTM_easting_std in metres")
plt.ylabel("UTM_northing_std in metres")


c=plt.Circle((0.012, 0.02), radius=0.024, color='red', alpha=.3)
plt.axis("equal")
angles = linspace(0 * pi, 2 * pi, 100 )
r=0.03
xs = r*cos(angles)
ys = r*sin(angles)
plt.gca().add_artist(c)
plt.show()
'''

df_statoccl[['UTM_easting_std','UTM_northing_std']].plot.scatter(x='UTM_easting_std',y='UTM_northing_std')
plt.xlabel("UTM_easting_std in metres")
plt.ylabel("UTM_northing_std in metres")

c=plt.Circle((3.8,2.3), radius=4.5, color='red', alpha=.2)
plt.axis("equal")
angles = linspace(0 * pi, 2 * pi, 100 )
plt.xlim(-2, 10)
plt.ylim(-2, 6.5)
plt.gca().add_artist(c)
plt.show()




df_movfree[['UTM_easting_std','UTM_northing_std']].plot.scatter(x='UTM_easting_std',y='UTM_northing_std')
plt.xlabel("UTM_easting_std in metres")
plt.ylabel("UTM_northing_std in metres")

#slope, intercept, r_value, p_value, std_err = linregress(df_movfree['UTM_easting_std'], df_movfree['UTM_northing_std'])
#plt.plot(df_movfree['UTM_easting_std'], df_movfree['UTM_northing_std'], label='',color='black')

df_movoccl[['UTM_easting_std', 'UTM_northing_std']].plot.scatter(x='UTM_easting_std',y='UTM_northing_std')
plt.xlabel("UTM_easting_std in metres")
plt.ylabel("UTM_northing_std in metres")

actual_utmN = pd.read_csv('/home/sriram/EECE5554/LAB2/src/data/UTMN.csv') 
utmN = actual_utmN['actUTMN']
predictedn=actual_utmN['UTM_northing']

utme = actual_utmN['actUTME']
predictede=actual_utmN['UTM_easting']


MSEN = np.square(np.subtract(utmN,predictedn)).mean()   
rsmeN = math.sqrt(MSEN)  
print("Root Mean Square Error:\n")  
print(rsmeN)

MSEE = np.square(np.subtract(utme,predictede)).mean()   
rsmee = math.sqrt(MSEE)  
print("Root Mean Square Error:\n")  
print(rsmee)
#stationary point latitude and logitude from google maps 42.33823011936888, -71.0864318171969 
#328121.11m east and UTM-northing as 4689434.40m

#plt.scatter( (df_statfree['UTM_northing_std'].min() + df_statfree['UTM_northing_std'].max())/2 , (df_statfree['UTM_easting_std'].min() + df_statfree['UTM_easting_std'].max())/2, s=10000 ,  facecolors='none', edgecolors='blue' ) 
#plt.xlim( df_statfree['UTM_northing_std'] , df_statfree['UTM_northing_std'])
#plt.ylim( df_statfree['UTM_easting_std'], df_statfree['UTM_easting_std'])
#plt.show()

'''fig, ax = bagpy.create_fig(1)
ax[0].scatter(x = 'Latitude_std', y = 'Longitude_std', data  = df_mov, s= 1, label = 'Latitude vs Longitude while walking')
ax[0].set(xlabel="Latitude_std",ylabel="Longitude_std")
'''

#plt.show()