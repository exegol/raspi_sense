from sense_hat import SenseHat
import sys
sense = SenseHat()

if len(sys.argv) != 4:
	sys.error("Arguments r g b missing")
else:
	sense.clear((int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
