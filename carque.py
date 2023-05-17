class Car():

    def __init__(self,model,year,doors,fuel):
        self.model=model
        self.year=year
        self.doors=doors
        self.fuel=fuel

    def view(self):
        print('model-',self.model,'\n','year-',self.year,'\n','doors-',self.doors,'\n','fuel-',self.fuel,'\n','speed-',self.speed,'\n','distance-',self.distance,'\n','time',self.time)

class Drive(Car):
    def __init__(self,model,year,doors,fuel,distance,time=0,speed=60):
        Car.__init__(self,model,year,doors,fuel)
        self.distance=distance
        self.speed=speed
        self.time=time

        self.time=self.distance/self.speed

car=Drive('tata',2020,4,'petrol',100)
car.view()