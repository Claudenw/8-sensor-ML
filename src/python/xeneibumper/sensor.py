from gpiozero import Button
import time


class Sensor:

    def __init__(self, pin):
        self.pin = pin
        self.button = Button(pin, pull_up=False)

    def get_state(self):
        return self.button.value


def main():
    sensor = Sensor(24)

    while True:
        print("pin " + str(sensor.pin))
        if sensor.get_state():
            print("input is HIGH")
        else:
            print("input is LOW")
        time.sleep(1)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
