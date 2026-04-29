from gpiozero import LED       #importing LED from gpiozero library
from time import sleep         # calling time to provide delays in program
led = LED(21)                  #variable declaration 
led.on()                       #turn on led 
print(“led on”)                #printing the subject
sleep(1)                       #providing delay of one second
led.off()                      #turn off led 
print(“led off”)               #printing the data
sleep(1)                       #delay of one second

