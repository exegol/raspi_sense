from sense_hat import SenseHat
import sys
from time import sleep

sense = SenseHat()
sense.clear((0,0,0))
for i in range(9,-1,-1):
	#print(i)
	sense.show_letter(str(i))
	sleep(1)
sense.clear((255,0,0))
sleep(3)
sense.clear((0,0,0))



