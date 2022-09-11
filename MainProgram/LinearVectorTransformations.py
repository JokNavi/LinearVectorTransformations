import numpy as np
import matplotlib.pyplot as plt


class DefaultLayout:

    def __init__(self, Height, Width, Vectors, Spacing):
        self.XInput = Width
        self.YInput = Height

    def MyGrid(self):
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()

        # Creates basis vectors acording to height and width (XInput,YInput)
    def BasisVectors(self):

        def BasisHorizontal():
            a = np.array([self.YInput, 0])
            b = np.array([0, 0])
            plt.plot(a, b, color='r')

        def BasisVertical():
            a = np.array([0, 0])
            b = np.array([0, self.XInput])
            plt.plot(a, b, color='r')

        BasisHorizontal()
        BasisVertical()

    def VectorsGroupOne(self):

        def DrawVector(InputY, ZeroY, InputX, ZeroX):
            a = np.array([InputY, ZeroX])
            b = np.array([ZeroY, InputX])
            plt.plot(a, b, color='r')

        def RepeatVectorDraw():
            pass

        DrawVector(1, 0, 1, 0)
