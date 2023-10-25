import utm
import serial
import rospy
from std_msgs.msg import String
import sys


from gps_driver.msg import gps_msg
rospy.init_node('talker')
port= rospy.get_param("~port_number")

data= serial.Serial( port= port, baudrate=4800, timeout = 5)
pub= rospy.Publisher('gps',gps_msg,queue_size=10)

rate = rospy.Rate(10) 
#a = "GPS1_Frame"
DATA=gps_msg()


while 1:  
    line = data.readline()
    lne=line.decode('utf-8')
    splitline = lne.split(',')

    if (splitline[0] == '$GNGGA') :
        lat = splitline[2]
        lon = splitline[4]
        alti= splitline[8]

        DATA.Latitude= float(lat[ :2])+(float(lat[2: ])/60)
        DATA.Longitude= (float(lon[ :3])+(float(lon[3: ])/60))*-1
        
        lldata = utm.from_latlon(DATA.Latitude,DATA.Longitude)
        
        DATA.UTM_easting = lldata[1]
        DATA.UTM_northing= lldata[0] 
        DATA.Zone= lldata[2]
        DATA.Letter= lldata[3]
        DATA.FIX= int(splitline[6])
        DATA.Altitude= float(alti)
        ts=splitline[1]
        tssec=(float(ts[ :2])*3600)+(float(ts[2:4])*60)+float(ts[4:6])
        DATA.Header.stamp.secs=int(tssec)
        tsnsec=float(ts[6:])*10e9

        DATA.Header.stamp.nsecs=int(tsnsec)
        DATA.Header.frame_id = 'GPS1_Frame'
        
        
        #print('Time-stamp-secs',DATA.Header.stamp.secs,'Time-stamp-nano secs',DATA.Header.stamp.nsecs,'latitude:',DATA.Latitude,'longitude:',DATA.Longitude,'UTM-Easting',DATA.UTM_easting,'UTM-Northing',DATA.UTM_northing,'Altitude',DATA.Altitude,'Zone',DATA.Zone,'Zone Letter',DATA.Letter)
        pub.publish(DATA)
