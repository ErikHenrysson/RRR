class my_target:
    '''
    Target, encapsulates a targets coordinates, speed, id and creation time.
    '''
    def __init__(self, x:float, y:float, z:float, vel:float, id:int, created_time:int):
        '''
        Constructs a new 'my_target' object.

        :param x: X coordinate of the target.
        :param y: Y coordinate of the target.
        :param z: Z coordinate of the target.
        :param vel: Speed of the target.
        :param id: Id of the target.
        :param created_time: Timestamp of the target.
        :return: Returns nothing.
        '''
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
        '''
        Prints the target to the console, mostly used for debugging.

        :return: Returns nothing.
        '''
        print("Target:", self.id," created at time:",self.created_time, "at (x, y, z) = (", self.x, ", ", self.y, ", ", self.z, ")\nTarget speed: ", self.vel, " m/s")

    def get_x(self) -> float:
        '''
        Function to retreive the X coordinate of the target.

        :return: X coordinate of the target.
        '''
        return self.x

    def get_y(self) -> float:
        '''
        Function to retreive the Y coordinate of the target.

        :return: Y coordinate of the target.
        '''
        return self.y

    def get_z(self) -> float:
        '''
        Function to retreive the Z coordinate of the target.

        :return: Z coordinate of the target.
        '''
        return self.z

    def get_vel(self) -> float:
        '''
        Function to retreive the speed of the target.

        :return: Speed of the target.
        '''
        return self.vel

    def get_id(self) -> int:
        '''
        Function to retreive the id of the target.

        :return: Id of the target.
        '''
        return self.id

    def get_created_time(self):
        '''
        Function to retreive the timestamp of the target.

        :return: Timestamp of the target.
        '''
        return self.created_time
    
    def set_x(self, x:float):
        '''
        Set the X coordinate of the target to the specified one.

        :param x: X coordinate to update to.
        :return: Returns nothing.
        '''
        self.x = x

    def set_y(self, y:float):
        '''
        Set the Y coordinate of the target to the specified one.

        :param y: Y coordinate to update to.
        :return: Returns nothing.
        '''
        self.y = y

    def set_z(self, z:float):
        '''
        Set the Z coordinate of the target to the specified one.

        :param z: Z coordinate to update to.
        :return: Returns nothing.
        '''
        self.z = z

    def set_vel(self, vel:float):
        '''
        Set the speed of the target to the specified one.

        :param vel: Speed to update to.
        :return: Returns nothing.
        '''
        self.vel = vel

    def set_id(self, id:float):
        '''
        Set the id of the target to the specified one.

        :param id: Id coordinate to update to.
        :return: Returns nothing.
        '''
        self.id = id

    def set_old_angle(self, angle:float):
        '''
        Sets the old angle of the target to the specified one.
        Used for presentation on a polar plot.

        :param angle: Angle to save.
        :return: Returns nothing.
        '''
        self.old_angle = angle

    def get_old_angle(self):
        '''
        Retreives the old angle of the target. 
        Used for presentation on a polar plot.

        :return: Returns the old angle.
        '''
        return self.old_angle
    
    def set_old_r(self, r:float):
        '''
        Sets the old length of the target to the specified one.
        Used for presentation on a polar plot.

        :param r: length to save.
        :return: Returns nothing.
        '''
        self.old_r = r

    def get_old_r(self):
        '''
        Retreives the old length of the target.
        Used for presentation on a polar plot.

        :return: Returns the old length.
        '''
        return self.old_r