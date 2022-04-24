#!/usr/bin/python
import os, sys
import ctypes
from movement import *
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
    
def close_claw():
	KIPR.cmpc(CLAW)
	KIPR.mav(CLAW,-1500)  #original value was 1100
	while KIPR.gmpc(CLAW) >-CLAW_TICKS:
		pass
        
	KIPR.mav(CLAW,0)
	KIPR.cmpc(CLAW)
            
def open_claw():
	KIPR.cmpc(CLAW)
	KIPR.mav(CLAW,1500)
	while KIPR.gmpc(CLAW) < CLAW_TICKS:
		pass
        
	KIPR.mav(CLAW,0)
	KIPR.cmpc(CLAW)   
            
def arm_drop():
	KIPR.set_servo_position(ARM, ARM_DROP)
	KIPR.msleep(500)
        
def arm_shake():
	KIPR.set_servo_position(ARM, ARM_SHAKE)
        
def arm_cube():
	KIPR.set_servo_position(ARM, ARM_CUBES)
        
def arm_score_cube():
	KIPR.set_servo_position(ARM, ARM_SCORE_CUBE)
        
def arm_botguy():
	KIPR.set_servo_position(ARM, ARM_BOTGUY)
        
def arm_drop_cube():
	KIPR.set_servo_position(ARM, ARM_DROP_CUBE)