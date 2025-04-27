from random import randint

from SensorNeuron import DONT_CARE


class MotorLayer:
    def __init__(self, sensor_layer):
        self.sensor_layer = sensor_layer
        self.last_selection = DONT_CARE

    def trigger(self):
        mapped_result = self.sensor_layer.trigger()

        left_result = mapped_result & 0xC >> 2  # high 2 bits
        right_result = mapped_result & 0x3  # low 2 bits
        self.last_selection = (left_result << 2) | right_result

        return [left_result, right_result]

    def select(self, result):
        if result == 0x3:
            return randint(1, 2)
        return result

    def feedback(self):
        self.sensor_layer.feedback(self.last_selection)

    def get_model(self):
        return self.sensor_layer.get_model()

    def get_sensor_layer(self):
        return self.sensor_layer
