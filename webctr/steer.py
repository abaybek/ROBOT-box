from pyax12.connection import Connection
import pyax12
import math
import json

P_PRESENT_POSITION = 36
P_GOAL_POSITION = 30



def computeAngles(theta, V):
#compute angles 
#const platform params
	l = 102; L = 209; 
	#computed values
	if (theta!=0):
 		R= L / math.tan( theta )
 		thR = math.atan( L / (R-l/2) )
 		thL = math.atan( L / (R+l/2) )
 		radF=300/180*math.pi
 		pR = int( thR / radF  *1024 + 512)
 		pL = int( thL / radF  *1024 + 512)
 		print('R')
 		print(R)
	else: 
 		pR = int(512)
 		pL = int(512)
 		R = 1000000

	vR = int(V*(R-l/2)/R);
	vL = int(V*(R+l/2)/R);

	print('pr pl vR vL')
	print ([pR, pL, vR, vL])
	return [pR, pL, vR, vL]
	
def moveAngle(thetar, V, dir):
	if thetar <-75: thetar =-75;
	if thetar > 75: thetar = 75;

	theta = thetar/180*math.pi

	if V>0: dir=0;
	elif V<0: dir=1;

	V = abs(V);

	if V>200: V = 200;
	elif V<0: V = 0;


	serial_connection = Connection(port = '/dev/ttyUSB0', baudrate = 1000000)
	tp = computeAngles(theta, V); pR = tp[0]; pL = tp[1]; vR = tp[2]; vL = tp[3]
	serial_connection.goto(2, pR, speed = 250, degrees = False);
	serial_connection.goto(4, pL, speed = 250, degrees = False);

  #vR = 200 if vR>200 else vR
  #vR = 0 if vR<0 else vR
  #if vL>200:  vL = 200;
  #if vL<0:  vL=0;
  
	serial_connection.set_cw_angle_limit(1, 0); serial_connection.set_ccw_angle_limit(1, 0); #set to wheel mode - CW and CCW angles limits to zeros sets wheel mode
	serial_connection.write_data(1, 32, pyax12.utils.int_to_little_endian_bytes(vR+1024*dir));
	serial_connection.set_cw_angle_limit(3, 0); serial_connection.set_ccw_angle_limit(1, 0)
	serial_connection.write_data(3, 32, pyax12.utils.int_to_little_endian_bytes(vL+1024*(1-dir)));

	serial_connection.flush()
	serial_connection.close()
def readMotors():
	serial_connection = Connection(port = '/dev/ttyUSB0', baudrate = 1000000)

	t1 = serial_connection.get_control_table_tuple(1);
	t2 = serial_connection.get_control_table_tuple(2);
	t3 = serial_connection.get_control_table_tuple(3);
	t4 = serial_connection.get_control_table_tuple(4);

	return	json.dumps([t1,t2,t3,t4])


#import sys 
#print(sys.argv[1])
#moveAngle(int(sys.argv[1]))
