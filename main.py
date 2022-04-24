#!/usr/bin/python
import os, sys
import ctypes
from movement import *
from constants import *
from effectors import *
from wait_for_start import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def main():

	#GET SET UP IN START BOX
	KIPR.enable_servos()
	KIPR.create_connect()
	KIPR.create_full()
	KIPR.set_servo_position(ARM, ARM_START)
	"""
	while not KIPR.a_button():
		pass
	print "GO!"
	KIPR.msleep(1000)
  	"""
	if wait_for_start(5) == False:
		print("CALIBRATION ERROR!!!")
		return 1
            
	#START DOMINATING THE WORLD!!!
	KIPR.set_servo_position(ARM, ARM_BOTGUY)
	forward(250,300) #First Forward to get past black tape
	drive_to_black(300)
	KIPR.msleep(500)
	forward(200, 250) #Second Forward
	CW(250, 67)    #turn to botguy   #original value 70degrees
	drive_to_bump(100)
	print "found the bump!!"
	backward(250, 655) #Botguy Backwards
	close_claw()
	print "choking botguy"
	drive_to_bump(200)
	backward(250, 270)
	CW(100, 148) #turn to lazy susan original 115
	backward(200, 473)
	arm_drop()
	open_claw() #DROP BOTGUY!!!
	backward(200, 5)

	KIPR.msleep(500)  # BOTGUY SCORED!!!

#get cubes
	forward(250, 352)
	arm_botguy()
	CW(100, 68)
	backward(50,330)    #line up against pipes
	forward(250, 455)
	CW(100, 197) #Turn to first green cube
	arm_cube()
	KIPR.msleep(500)
	backward(200, 155) #drive to green cube
	close_claw()
	drive_to_bump(250)
	backward(200, 120)
	arm_score_cube()
	CW(150, 125) #Turn to lazy susan
	backward(200, 374)
	arm_drop_cube()
	open_claw()
	KIPR.set_servo_position(ARM, ARM_BOTGUY)
#get 2nd cube
	forward(200, 210)
	CCW(150, 92)  #turn to second cube
	back_to_black(250)
	KIPR.msleep(500)
	arm_cube()
	CCW(200, 11)    
	backward(200, 170)
	close_claw()  #get 2nd cube
	drive_to_black(250)
	forward(250, 400)
	arm_score_cube()
	CW(150, 121)
	backward(200, 140)
	arm_drop_cube()  # score second cube
	open_claw()
	KIPR.msleep(500)
	arm_botguy()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
