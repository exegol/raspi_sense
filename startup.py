from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.show_message("startup", text_colour=(0,255,0))

sense.set_pixel(7,7,(0,255,0))
