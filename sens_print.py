from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()
  t2 = sense.get_temperature_from_pressure()
  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  t2 = round(t2, 1)
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temp1: " + str(t) + " Temp2: " + str(t2) +  " Pressure: " + str(p) + " Humidity: " + str(h)
  
  # Display the scrolling message
  #sense.show_message(message, scroll_speed=0.05)
  print(message)
  sleep(1)
