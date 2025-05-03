from time import sleep
from gpiozero import Motor
from xeneibumper.sensor import Sensor
from xeneisensorml.model import Model

motor = [Motor(13, 19), Motor(12, 18)]
sensor_pins = [23, 24, 25, 8, 7, 1, 9, 11]
model = Model()
sensors = []
for pin_num in sensor_pins:
    sensor = Sensor(pin_num)
    sensors.append(sensor)
    model.add_sensor(sensor.get_state)

try:
    # initial state is go forward
    last_state = [1, 1]
    next_state = last_state
    while True:
        # Read the state of the switch
        model.feedback()
        model_state = model.trigger()
        # model state changes state unless don't care (3) is returned
        for i in [0, 1]:
            if model_state[i] in [0, 1, 2]:
                next_state[i] = model_state[i]
            else:
                next_state[i] = last_state[i]

        # update the motors.
        for i in [0, 1]:
            if next_state[i] == 0:
                motor[i].stop()
            elif next_state[i] == 1:
                motor[i].forward(speed=0.5)
            elif next_state[i] == 2:
                motor[i].backward(speed=0.5)

        # preserve the state
        last_state = next_state
        # sleep so we can wait for change to take effect.
        sleep(0.5)

except KeyboardInterrupt:
    pass
