#!/usr/bin/python
import os, sys
import ctypes
from movement import *
from constants import *
from effectors import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def main():

	#GET SET UP IN START BOX
	KIPR.enable_servos()
	KIPR.create_connect()
	KIPR.create_full()
	KIPR.set_servo_position(ARM, ARM_START)
	while not KIPR.a_button():
		pass
	print "GO!"
	KIPR.msleep(1000)
        
	#START DOMINATING THE WORLD!!!
	KIPR.set_servo_position(ARM, ARM_BOTGUY)
	forward(250,300) #First Forward
	drive_to_black(250)
	KIPR.msleep(200)
	forward(200, 200) #Second Forward
	CW(250, 83)
	drive_to_bump(50)
	print "found the bump!!"
	backward(250, 650) #Botguy Backwards
	close_claw()
	drive_to_bump(100)
	backward(250, 160)
	CW(100, 130)
	backward(200, 405)
	arm_drop()
	open_claw() #DROP BOTGUY!!!


        
	KIPR.set_servo_position(ARM, ARM_BOTGUY)
	KIPR.msleep(2000)  # BOTGUY SCORED!!!

#get cubes
	forward(250, 250)
	CW(100, 90)
	backward(50,320)
	forward(250, 455)
	CW(100, 195) #Turn to first green cube
	arm_cube()
	KIPR.msleep(1000)
	backward(200, 160) #drive to green cube
	close_claw()
	drive_to_bump(250)
	backward(200, 90)
	arm_score_cube()
	CW(150, 107) #Turn to lazy susan
	backward(200, 425)
	open_claw()
	KIPR.set_servo_position(ARM, ARM_BOTGUY)
#get 2nd cube
	forward(200, 350)
	CCW(150, 75)
	back_to_black(250)
	KIPR.msleep(1000)
	arm_cube()
	backward(200, 240)
	close_claw()
	drive_to_black(250)
	forward(250, 200)
	arm_score_cube()
	CW(150, 94)
	backward(200, 327)
	open_claw()
	KIPR.msleep(1000)
	arm_botguy()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
