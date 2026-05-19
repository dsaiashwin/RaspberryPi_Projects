import RPi.GPIO as GPIO
import telepot
import time
from telepot.loop import MessageLoop

# use channel numbers on the Broadcom SOC
GPIO.setmode(GPIO.BCM)

LED_PIN = 19
GPIO.setup(LED_PIN, GPIO.OUT)

bot = telepot.Bot('579430837:AAEG-ll76_EnQ2XBQqaN3B4wQpptpCB5PY0')

def turnOn(chatId):
    GPIO.output(LED_PIN, True)
    bot.sendMessage(chatId, 'The led is ON now!')

def turnOff(chatId):
    GPIO.output(LED_PIN, False)
    bot.sendMessage(chatId, 'The led is OFF now!')

def handleCommand(msg):
    contentType, chatType, chatId = telepot.glance(msg) # extract “headline info”
    print(contentType, chatType, chatId)

    if contentType != 'text':
        return # nothing to do

    message = msg['text']

    if not message.startswith('!'):
        return # not a command
    
    command = message[1:].lower() # remove ! from the command name
    if command == 'on':
        turnOn(chatId)
    elif command == 'off':
        turnOff(chatId)

if __name__ == '__main__':
    try:
        MessageLoop(bot, handleCommand).run_as_thread()

        while 1:
            # just don't finish the program
            time.sleep(10)
        # close execution by pressing CTRL + C
    except KeyboardInterrupt:
        print("Intrerrupted by user")
        pass
    finally:
        print("Program stopped")
        GPIO.cleanup()
