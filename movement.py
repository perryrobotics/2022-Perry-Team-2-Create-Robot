#!/usr/bin/python
import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

BLACK_THRESH = 3800
LINE_SENSOR = 0
    
def forward (speed, mm):
    
	KIPR.set_create_distance(0)
	KIPR.create_drive_direct(speed, speed)
        
	while(KIPR.get_create_distance() < mm):
		pass
 	KIPR.create_drive_straight(0)
            
def backward(speed, mm):
    
	KIPR.set_create_distance(0)
	KIPR.create_drive_direct(-speed, -speed)
        
	while(KIPR.get_create_distance() > -mm):
		pass
 	KIPR.create_drive_straight(0)  
            
def CCW(speed, angle):
    
	KIPR.set_create_total_angle(0)
	KIPR.create_spin_CCW(speed)
	while(KIPR.get_create_total_angle() < angle):
		pass
 	KIPR.create_spin_CCW(0)

def CW(speed, angle):
    
	KIPR.set_create_total_angle(0)
	KIPR.create_spin_CW(speed)
	while(KIPR.get_create_total_angle() > -angle):
		pass
 	KIPR.create_spin_CW(0)
            
def drive_to_black(speed):
	KIPR.create_drive_direct(speed, speed)
        
	while( KIPR.analog(LINE_SENSOR) < BLACK_THRESH):
		pass
        
	KIPR.create_drive_direct(0,0)
           
def back_to_black(speed):
	KIPR.create_drive_direct(-speed, -speed)
        
	while( KIPR.analog(LINE_SENSOR) < BLACK_THRESH):
		pass
        
	KIPR.create_drive_direct(0,0)
            
def right_to_black(speed):
	KIPR.create_drive_direct(speed, -speed)
        
	while( KIPR.analog(LINE_SENSOR) < BLACK_THRESH):
		pass
        
	KIPR.create_drive_direct(0,0)
            
def left_to_black(speed):
	KIPR.create_drive_direct(-speed, speed)
        
	while( KIPR.analog(LINE_SENSOR) < BLACK_THRESH):
		pass
        
	KIPR.create_drive_direct(0,0)
            
def drive_to_bump(speed):
	KIPR.create_drive_straight(speed)
	while (KIPR.get_create_lbump() == 0) and (KIPR.get_create_rbump() == 0):
		pass
 	KIPR.create_drive_direct(0,0)