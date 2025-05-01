from bitmap import BitMap


class SensorNeuron:
    """A neuron that follows a sensor trigger"""

    @classmethod
    def empty_bitmap(cls):
        return BitMap(0x10)

    @classmethod
    def full_bitmap(cls):
        result = SensorNeuron.empty_bitmap()
        for i in range(0x10):
            result.set(i)
        return result

    def __init__(self, state_func):
        self.options = SensorNeuron.full_bitmap()
        self.last_state = False
        self.state_func = state_func

    def trigger(self):
        self.last_state = self.state_func()
        if self.last_state:
            return self.options
        return DONT_CARE

    def feedback(self, last_selection):
        if self.last_state and self.state_func():
            print("Updating neuron")
            self.options.reset(last_selection)
        else:
            print("No neuron update")

    def get_model(self):
        return self.options

    def reset(self, bitmap_string):
        self.options = BitMap.fromstring(bitmap_string)


DONT_CARE = SensorNeuron.full_bitmap()
