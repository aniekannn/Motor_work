from motor import Motor

class MotorController:

    def __init(self, list_of_motors: list[Motor]):
        self.motors = list_of_motors

    def set_speed(self, speed):
        for motor in self.motors:
            motor.set_speed(speed)

    def speedup(self):
        for whatever in self.motors:
            whatever.speedup()

    def slow_down(self):
        for ehh in self.motors:
            ehh.slow_down()

    def add_Motor(self, motor:Motor):
        self.motors.append(motor)