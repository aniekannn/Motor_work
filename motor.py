set_speed
slow_donw

class Motor
    def __init__(self):
        self.speed = 0.5

    def set_speed(self, new_speed):
        self.speed = new_speed

    def speed_up(self):
        self.speed = 2*(self.speed)

    def slow_down(self):
        self.speed = 0.5*(self.speed)

class MotorControllerGroup
    def __init__(self):
        self.number =





