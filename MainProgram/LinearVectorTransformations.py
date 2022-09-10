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

        PartOne()

    def VectorGroupTwo(self):

        def TestVector(MaxCoordY, MaxCoordX, ZeroX, ZeroY):
            y = np.array([ZeroY, MaxCoordX])
            x = np.array([ZeroX, MaxCoordY])
            plt.plot(x, y, color='b')

        def PartOne():
            MaxCoordX = self.MaxCoordX
            MaxCoordY = self.MaxCoordY
            ZeroX = 0
            ZeroY = 0
            Counter = self.VectorAmount

            TestVector(MaxCoordX, MaxCoordY, ZeroX, ZeroY)
            while Counter > 0:
                #MaxCoordX = MaxCoordX - self.YInput
                MaxCoordY = MaxCoordY - self.YInput
                ZeroX = ZeroX + self.XInput
                TestVector(MaxCoordX, MaxCoordY, ZeroX, ZeroY)
                Counter = Counter - 1
        PartOne()
