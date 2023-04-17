class my_target:
    def __init__(self, x:float, y:float, z:float, vel:float, id:int, created_time:int):
        self.x = x
        self.y = y
        self.z = z
        self.vel = vel
        self.id = id
        self.created_time = created_time
        self.old_angle = 0
        self.old_r = 0
        #self.print_target()

    def print_target(self):
        print("Target:", self.id," created at time:",self.created_time, "at (x, y, z) = (", self.x, ", ", self.y, ", ", self.z, ")\nTarget speed: ", self.vel, " m/s")

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
    def get_created_time(self):
        return self.created_time
    
    def set_x(self, x:float):
        self.x = x
    def set_y(self, y:float):
        self.y = y
    def set_z(self, z:float):
        self.z = z
    def set_vel(self, vel:float):
        self.vel = vel
    def set_id(self, id:float):
        self.id = id

    def set_old_angle(self, angle:float):
        self.old_angle = angle
    def get_old_angle(self):
        return self.old_angle
    
    def set_old_r(self, r:float):
        self.old_r = r
    def get_old_r(self):
        return self.old_r