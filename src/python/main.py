from time import sleep
from gpiozero import Motor
from xeneibumper.sensor import Sensor
from xeneisensorml.model import Model

motor_pins = [[19, 13], [12, 18]]
motor = [Motor(motor_pins[0]), Motor(motor_pins[1])]

sensor_pins = [23, 24, 25, 8, 7, 1, 9, 11]
model = Model()
sensors = []
for pin_num in sensor_pins:
    sensor = Sensor(pin_num)
    sensors.append(sensor)
    model.add_sensor(sensor.get_state)

try:
    while True:
        # Read the state of the switch
        model.feedback()
        motor_state = model.trigger()
        for i in [0, 1]:
            if motor_state[i] == 0:
                motor[i].stop()
            elif motor_state[i] == 1:
                motor[i].forward(speed=3)
            elif motor_state[i] == 2:
                motor[i].backward(speed=3)
            else:
                motor[i].stop()
        sleep(0.5)

except KeyboardInterrupt:
    pass
