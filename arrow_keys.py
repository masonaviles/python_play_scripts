import time
import random
from pynput.keyboard import Key, Controller

keyboard = Controller()  # Create the controller

arrows = [Key.down, Key.left, Key.right, Key.up]
repeat_delay = random.uniform(1, 300)
random_number_of_presses = random.randint(1, 10)

# start_time = time.time()
# seconds = 54000 # 15 hours

while True:
    for x in range(0, random_number_of_presses):
        delay = random.uniform(1, 3)
        random_arrow = random.choice(arrows)
        keyboard.press(random_arrow)
        keyboard.release(random_arrow)
        time.sleep(delay)   
    time.sleep(repeat_delay)
