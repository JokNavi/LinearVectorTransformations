import numpy as np
import matplotlib.pyplot as plt


class DefaultLayout:

    def __init__(self, Height, Width, Vectors, Spacing):
        self.XInput = Width
        self.YInput = Height
        self.VectorAmount = Vectors - 1
        self.Spacing = Spacing
        self.MaxCoordX = self.VectorAmount * self.XInput + 1
        self.MaxCoordY = self.VectorAmount * self.YInput + 1

    def MyGrid(self):
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()

        # Creates basis vectors acording to height and width (XInput,YInput)
    def BasisVectors(self):

        def BasisY():
            x = np.array([0, 0])
            y = np.array([self.XInput, 0])
            plt.plot(x, y, color='r')

        def BasisX():
            x = np.array([0, self.YInput])
            y = np.array([0, 0])
            plt.plot(x, y, color='r')

        BasisX()
        BasisY()

    def VectorsGroupOne(self):

        def TestVector(XCoord, YCoord, ZeroX, ZeroY):
            y = np.array([XCoord, ZeroY])
            x = np.array([ZeroX, YCoord])
            plt.plot(x, y, color='b')

        def PartOne():
            EditedX = self.XInput
            EditedY = self.YInput
            ZeroX = 0
            ZeroY = 0

            TestVector(EditedX, EditedY, ZeroX, ZeroY)
            for vector in range(self.VectorAmount):
                EditedY = EditedY + self.Spacing
                EditedX = EditedX + self.Spacing
                TestVector(EditedX, EditedY, ZeroX, ZeroY)

        def PartTwo():
            EditedY = self.YInput * (self.VectorAmount + 1)
            EditedX = self.XInput * (self.VectorAmount + 1)
            ZeroY = 0
            ZeroX = 0 

            for vector in range(self.VectorAmount):
                ZeroY = ZeroY + self.YInput
                ZeroX = ZeroX + self.XInput
                TestVector(EditedX, EditedY, ZeroX, ZeroY)

        PartTwo()
        PartOne()

    def VectorGroupTwo(self):

        def TestVector(cY, cX, ZeroForX, ZeroForY):
            y = np.array([ZeroForY, cY])
            x = np.array([ZeroForX, cX])
            plt.plot(x, y, color='b')

        def PartOne():
            XInput = self.XInput
            YInput = self.YInput
            MaxCoordX = self.MaxCoordX
            MaxCoordY = self.MaxCoordY
            ZeroForX = 0
            ZeroForY = 0
            Counter = self.VectorAmount

            TestVector(MaxCoordX, MaxCoordY, ZeroForX, ZeroForY)
            while Counter > 0:
                YInput = YInput + self.YInput
                #MaxCoordY = MaxCoordY - self.YInput
                TestVector(YInput, XInput, ZeroForX, ZeroForY)
                Counter = Counter - 1
        
        def PartTwo():
            cX = self.MaxCoordX
            cY = 0
            ZeroForX = 0
            ZeroForY = self.MaxCoordY
            Counter = self.VectorAmount 

            while Counter > 0:
                ZeroForX = ZeroForX + 1
                cY = cY #Remove later
                #cX = cX - 1
                #ZeroForY = ZeroForY #RL
                TestVector(cY, cX, ZeroForX, ZeroForY)
                Counter = Counter - 1
        #PartTwo()
        PartOne()
