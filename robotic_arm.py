import time
from gpiozero import Servo

# Define servos
servo_base = Servo(18)
servo_elbow = Servo(19)
servo_gripper = Servo(20)

def move_arm():
    print("Moving arm...")
    servo_base.mid()
    time.sleep(1)
    servo_elbow.min()
    time.sleep(1)
    servo_gripper.max()
    time.sleep(1)
    print("Garbage picked up!")
    servo_gripper.min()
