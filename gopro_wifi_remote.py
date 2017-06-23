#!/usr/bin/env python

########################################
# GoPro HERO4 WiFi Remote              #
# Version 0.10 Date: 2016-01-31        #
# By: PORNPASOK SOOKYEN (Ton)		   #
# http://ton.packetlove.com/blog/	   #
# FB: pornpasok                        #
# E-Mail: ton350d@gmail.com            #
# Thanks: GoPro API					   #
# https://github.com/KonradIT          #
# /goprowifihack/blob/master/HERO4.md  #
########################################

import sys, tty, termios, urllib2

def getch():
  import sys, tty, termios
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch

def gp_fetch_url(gp_url):
	req = urllib2.Request(gp_url)
	response = urllib2.urlopen(req)
	gp_json = response.read()
	#print(gp_json)
	return gp_json


#gp_url = 'http://ton.packetlove.com'
#print(gp_fetch_url(gp_url))

gp_mode_url = [
'http://10.5.5.9/gp/gpControl/command/mode?p=0', 
'http://10.5.5.9/gp/gpControl/command/mode?p=1', 
'http://10.5.5.9/gp/gpControl/command/mode?p=2'
]

gp_mode = ['Video',
'Photo',
'MultiShot'
]

gp_trigger_url = [
'http://10.5.5.9/gp/gpControl/command/shutter?p=0',
'http://10.5.5.9/gp/gpControl/command/shutter?p=1'
]

# Init to Video Mode
#print(gp_fetch_url(gp_mode_url[0]))

i = 0
tm = 3 # Total Mode
m = 0 # Default Video Mode
t = 0
while True:
    #gp_mode = raw_input("Please enter 'GP Mode':")
    #print("\nPress Any Key '" + getch() + "'\n")
    chkey = getch()
    print(t)
    if (chkey == 'q' and t == 0):
    	print(gp_fetch_url(gp_trigger_url[0])) # Stop Video Mode
    	print("Exit")
    	break

    elif (chkey != ' ' and t == 0):
    	i = i+1
    	m = i%tm
    	print(i)
    	print ("Mode : %d" % m)
    	print ("Mode: "+gp_mode[m])
    	print(gp_mode_url[m])
    	print(gp_fetch_url(gp_mode_url[m]))

    # Trigger
    elif chkey == ' ':
    	# Photo & MultiShot Mode
    	if m != 0:
    		print(gp_trigger_url[1])
    		print(gp_fetch_url(gp_trigger_url[1]))
    	else:
    		t = t+1
    		print(t)
    		if t%2 == 1:
    			print(gp_trigger_url[1])
    			print(gp_fetch_url(gp_trigger_url[1]))
    		else:
    			print(gp_trigger_url[0])
    			print(gp_fetch_url(gp_trigger_url[0]))
    			t = 0 # Reset Trigger Video Mode


 


