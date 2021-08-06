from sense_hat import SenseHat
from time import sleep
import datetime

sense = SenseHat()
sense.set_rotation(180)
# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 127, 127)
yellow = (255, 255, 0)

tempcorrection = -8

loop = 0
while loop < 2:

  loop += 1
  # Take readings from all three sensors
  t = sense.get_temperature() + tempcorrection
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t1= round(t, 1)
  p1 = round(p, 1)
  h1 = round(h, 1)
  t = int(t)
  p = int(p)
  h = int(h)

  # Create the message
  # str() converts the value to a string so it can be concatenated
  msg_t = str(t) + "C"
  msg_h = str(h) + "%"
  msg_p = str(p) + "hPa"
  # Display the scrolling message
  sense.show_message(msg_t, scroll_speed=0.1, text_colour=red)
  sleep(2)
  sense.show_message(msg_h, scroll_speed=0.1, text_colour=blue)
  sleep(2)
  sense.show_message(msg_p, scroll_speed=0.1, text_colour=cyan)
  sleep(2)

time = str(datetime.datetime.now())
f = open("/home/pi/py/sense/data.csv", "a")
f.write(time + ";" + str(t1) + ";" + str(p1) + ";" + str(h1) + "\n")
f.close()
