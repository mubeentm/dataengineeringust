class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calcu(self):
            print("Area : ",self.length*self.width)
            print("Perimeter : ",2*(self.length+self.width))

val=Rectangle(10,20)
val.calcu()