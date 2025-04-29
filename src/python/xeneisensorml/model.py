from model_layer import MotorLayer
from sensor_layer import SensorLayer
from sensor_neuron import SensorNeuron


class Model:
    MOTOR_STATE = ["off", "fwd", "rev", "brake"]

    def __init__(self):
        self.sensor_layer = SensorLayer()
        self.motor_layer = MotorLayer(self.sensor_layer)

    def print_neurons(self):
        line = "Neurons: "
        for i in self.motor_layer.get_model():
            line += str(i) + " "
        print(line)

    def trigger(self):
        motor_states = self.motor_layer.trigger()
        print("Left motor: " + self.MOTOR_STATE[motor_states[0]])
        print("Right motor: " + self.MOTOR_STATE[motor_states[0]])
        self.print_neurons()
        return motor_states

    def feedback(self):
        self.motor_layer.feedback()
        print("Feedback")
        self.print_neurons()

    def add_sensor(self, state_func):
        self.sensor_layer.add_neuron(SensorNeuron(state_func))

    def write_model(self, file_name):
        with open(file_name, 'w', encoding="utf-8") as f:
            for i in self.motor_layer.get_model():
                f.write(str(i))
                f.write('\n')

    def read_model(self, file_name):
        with open(file_name, 'r', encoding="utf-8") as f:
            idx = 0
            bitmap = f.readline()
            while bitmap != '':
                self.motor_layer.get_sensor_layer().reset_neuron(idx, bitmap)
                idx += 1
