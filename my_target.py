class my_target:
    def __init__(self, x:float, y:float, z:float, vel:float, id:int):
        self.x = x
        self.y = y
        self.z = z
        self.vel = vel
        self.id = id
        #self.print_target()

    def print_target(self):
        print("Target", self.id,"at (x, y, z) = (", self.x, ", ", self.y, ", ", self.z, ")\nTarget speed: ", self.vel, " m/s")

    def get_x(self) -> float:
        return self.x
    def get_y(self) -> float:
        return self.y
    def get_z(self) -> float:
        return self.z
    def get_vel(self) -> float:
        return self.vel
    def get_id(self) -> int:
        return self.id
    def set_x(self, x:float):
        self.x = x
    def set_x(self, y:float):
        self.y = y
    def set_x(self, z:float):
        self.z = z
    def set_x(self, vel:float):
        self.vel = vel
    def set_x(self, id:float):
        self.id = id