from sense_hat import SenseHat
import os
import time

sense = SenseHat()
sense.set_rotation(180)
pressed = False
while True:
	for event in sense.stick.get_events():
		if event.direction == 'middle' and event.action == 'released':
			pressed = True
	if pressed:
		break
	time.sleep(0.5)

sense.show_message("shutdown", text_colour=(255,0,0))

os.system('shutdown -P 0')
