from src.python.MotorLayer import MotorLayer
from src.python.SensorLayer import SensorLayer
from src.python.SensorNeuron import SensorNeuron


class Model:
    MOTOR_STATE = ["off", "fwd", "rev", "unknown"]

    def __init__(self):
        self.sensors = []
        sensor_layer = SensorLayer()
        for i in range(8):
            sensor = Sensor();
            self.sensors.append(sensor)
            sensor_layer.add_neuron(SensorNeuron(sensor.get_state))
        self.motor_layer = MotorLayer(sensor_layer)

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

    def feedback(self):
        self.motor_layer.feedback()
        print("Feedback")
        self.print_neurons()

    def set_sensor(self, idx, value):
        self.sensors[idx].set_state(value)

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


class Sensor:
    def __init__(self):
        self.state = False

    def set_state(self, state):
        self.state = state;

    def get_state(self):
        return self.state


def main():
    model = Model()
    model.set_sensor(0, True)
    model.set_sensor(5, True)
    for i in range(0, 10):
        model.trigger()
        model.feedback()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
