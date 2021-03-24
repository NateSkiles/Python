class Computer:
    brand = ''
    CPU = ''
    GPU = ''
    storage = ''
    RAM = ''

    def __init__(self, brand, CPU, GPU, storage, RAM):
        self.brand = brand
        self.CPU = CPU
        self.GPU = GPU
        self.storage = storage
        self.RAM = RAM

    def __repr__(self):
        return '\n'.join(['Brand: ' + self.brand, 'CPU: ' + self.CPU, 'GPU: ' + self.GPU, 'Storage: ' + self.storage,
                          'RAM: ' + self.RAM])


class mobilePhone(Computer):
    batterySize = ''
    screenSize = ''

    def __init__(self, batterySize, screenSize):
        self.batterySize = batterySize
        self.screenSize = screenSize


class gameConsole(Computer):
    numberOfControllers = 0
    color = ''

    def __init__(self, numberOfControllers, color):
        self.numberOfControllers = numberOfControllers
        self.color = color


# Create our computer object and print that object
config = Computer('Dell', '8700k', 'GTX 1080', '1TB', '8GB')
print(config)
