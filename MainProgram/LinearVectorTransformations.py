import numpy as np
import matplotlib.pyplot as plt


class DefaultLayout:

    def __init__(self, Height, Width, Vectors, Spacing):
        self.XInput = Width
        self.YInput = Height
        self.VectorAmount = Vectors - 1
        self.Spacing = Spacing

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

    def VectorsTLBR(self):
        EditedX = self.XInput
        EditedY = self.YInput

        def TestVector(XCoord, YCoord):
            y = np.array([XCoord, 0])
            x = np.array([0, YCoord])
            plt.plot(x, y, color='b')

        TestVector(EditedX, EditedY)
        for vector in range(self.VectorAmount):
            EditedY = EditedY + self.Spacing
            EditedX = EditedX + self.Spacing
            TestVector(EditedX, EditedY)
