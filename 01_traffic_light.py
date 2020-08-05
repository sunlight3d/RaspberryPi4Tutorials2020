import RPi.GPIO as GPIO
import time
from enum import Enum

LED_GREEN = 23
LED_YELLOW = 12 #GPIO12
LED_RED = 16
TOGGLE_BUTTON = 19
class State(Enum):
  START_TRAFFIC_LIGHT = 1
  STOP_TRAFFIC_LIGHT = 2
current_state = State.STOP_TRAFFIC_LIGHT
current_number = 0

def setup():
  GPIO.setmode(GPIO.BCM)  
  GPIO.setup(LED_RED, GPIO.OUT)
  GPIO.setup(LED_YELLOW, GPIO.OUT)
  GPIO.setup(LED_GREEN, GPIO.OUT)
  GPIO.setup(TOGGLE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def control_light_traffic(params):
  GPIO.output(LED_GREEN, 1)
  # import pdb
  # pdb.set_trace()
  time.sleep(params['delay_green'])
  sleep_and_print(params['delay_green'])  
  GPIO.output(LED_GREEN, 0)

  GPIO.output(LED_YELLOW, 1)
  sleep_and_print(params['delay_yellow'])  
  GPIO.output(LED_YELLOW, 0)

  GPIO.output(LED_RED, 1)
  sleep_and_print(params['delay_red'])  
  GPIO.output(LED_RED, 0)

  GPIO.output(LED_YELLOW, 1)  
  sleep_and_print(params['delay_yellow'])  
  GPIO.output(LED_YELLOW, 0)

def sleep_and_print(number_of_seconds):
  current_number = 0
  for i in range(1, number_of_seconds + 1):
    time.sleep(1)
    current_number = current_number + 1
    print('current_number = '+str(current_number))

def turn_off_all_lights():
  GPIO.output(LED_GREEN, 0)
  GPIO.output(LED_YELLOW, 0)
  GPIO.output(LED_RED, 0)

if __name__ == '__main__':
  setup()
  params = {
    'delay_red': 5,
    'delay_green': 6,
    'delay_yellow': 3
  }  
  while True:    
    try:
      control_light_traffic(params) #test mode
      # if GPIO.input(TOGGLE_BUTTON) == True:
      #   current_state = State.START_TRAFFIC_LIGHT if current_state == State.STOP_TRAFFIC_LIGHT else State.STOP_TRAFFIC_LIGHT
      #   if current_state == State.START_TRAFFIC_LIGHT:
      #     control_light_traffic(params)
      #   else:
      #     turn_off_all_lights()
    except KeyboardInterrupt:
      print("You've exited the program")
      GPIO.cleanup()          
  GPIO.cleanup()    
      