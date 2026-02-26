class Gripper:
    def __init__(self):
        self.__pressure = 0
        self.__max_pressure = 100
    def apply_pressure(self, amount):
        if 0<=amount <= self.__max_pressure:
            self.__pressure = amount
        else:
            print("Safety Limit Exceeded!")
    def getstatus(self):
        return self.__pressure