import random

from xeneisensorml.sensor_neuron import DONT_CARE, SensorNeuron


class SensorLayer:

    def __init__(self):
        random.seed()
        self.neurons = []
        self.last_result = SensorNeuron.full_bitmap()
        self.last_answer = random.randrange(0, self.last_result.size())

    def add_neuron(self, sensor_neuron):
        self.neurons.append(sensor_neuron)

    def reset_neuron(self, idx, bitmap_string):
        self.neurons[idx].reset(bitmap_string)

    def trigger(self):
        result = SensorNeuron.full_bitmap()
        for neuron in self.neurons:
            bitmap = neuron.trigger()
            for i in result.nonzero():
                if not bitmap.test(i):
                    result.reset(i)
        candidates = result.nonzero()
        if candidates == self.last_result.nonzero():
            return self.last_answer;

        idx = random.randrange(0, len(candidates))
        self.last_answer = candidates[idx]
        return self.last_answer

    def feedback(self, last_selection):
        for neuron in self.neurons:
            neuron.feedback(last_selection)

    def get_model(self):
        result = []
        for neuron in self.neurons:
            result.append(neuron.get_model())
        return result
