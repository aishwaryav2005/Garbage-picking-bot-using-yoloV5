import cv2
from robotic_arm import move_arm
from motor_control import move_robot
from video_stream import start_video_stream

def main():
    print("Starting Garbage Picking Robot...")
    start_video_stream()

    while True:
        command = input("Enter command (forward/backward/left/right/pick/exit): ").lower()
        if command in ["forward", "backward", "left", "right"]:
            move_robot(command)
        elif command == "pick":
            move_arm()
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
