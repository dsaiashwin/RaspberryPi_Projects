from gpiozero import LED 
from espeak import espeak
from time import sleep
import os
led = LED(17)
led.on()
os.system ("espeak “Led is turned on" 2>/dev/null") 
espeak.synth(“LED is turned on")
sleep(1)
led.off()
os.system ("espeak “Led is turned off" 2>/dev/null")
espeak.synth(“LED is turned off")
sleep(1)

	
