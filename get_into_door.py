import time
import random
from pynput.keyboard import Key, Controller

keyboard = Controller()  # Create the controller

# example:
# def type_string_with_delay(string):
#     for character in string:  # Loop over each character in the string
#         keyboard.type(character)  # Type the character
#         delay = random.uniform(0, 2)  # Generate a random number between 0 and 10
#         time.sleep(delay)  # Sleep for the amount of seconds generated

# type_string_with_delay("This is my string typed with a delay")

arrows = [Key.down, Key.left, Key.right, Key.up]
delay = random.uniform(0, 2)  # Generate a random number between 0 and 10

# start_time = time.time()
# seconds = 54000 # 15 hours

while True:

    keyboard.press(Key.x)
    keyboard.release()
    time.sleep(delay)
    
    time.sleep(1) # 30 secs

# current_time = time.time()
# elapsed_time = current_time - start_time
# if elapsed_time > seconds:
#     print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
#     break
