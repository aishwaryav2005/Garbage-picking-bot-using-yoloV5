from gpiozero import Motor

# Define motors
motor_left = Motor(forward=17, backward=27)
motor_right = Motor(forward=22, backward=23)

def move_robot(direction):
    if direction == "forward":
        motor_left.forward()
        motor_right.forward()
    elif direction == "backward":
        motor_left.backward()
        motor_right.backward()
    elif direction == "left":
        motor_left.backward()
        motor_right.forward()
    elif direction == "right":
        motor_left.forward()
        motor_right.backward()
    else:
        print("Unknown direction!")
    
    # Stop motors after a short delay
    motor_left.stop()
    motor_right.stop()
