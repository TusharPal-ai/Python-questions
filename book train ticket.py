from random import randint


class train():
    def __init__(self, trainno, fro,to,):

        self.trainno=trainno
        self.fro=fro
        self.to=to
        

        print(f"The train no is {self.trainno} the from location is {self.fro} and the to location is {self.to} and its fair is {randint(100,3000)}")


t= train(1264,"uttar pradesh","gujrat")
   