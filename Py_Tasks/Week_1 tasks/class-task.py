class Rectengular:
    def init(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calarea(self):
        self.area = self.length * self.breadth
        

    def show(self):
        print(f"The area of this rentangular is : {self.area}")    

rec1=Rectengular()   
rec1.init(3,4)
rec1.calarea()
rec1.show()     
