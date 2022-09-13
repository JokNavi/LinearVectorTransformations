import numpy as np
import matplotlib.pyplot as plt


class DefaultLayout:

    def __init__(self, Width, Height, Vectors, Spacing):
        self.XInputA = 0
        self.YInputA = Width
        self.XInputB = Height
        self.YInputB = 0
        self.Vectors = Vectors
        self.MaxXInput = Width * Vectors
        self.MaxYInput = Height * Vectors

    def MyGrid(self):
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()

        # Creates basis vectors acording to height and width (XInput,YInput)
    def BasisVectors(self):

        def BasisHorizontal():
            a = np.array([self.YInputA, 0])
            b = np.array([0, 0])
            plt.plot(a, b, color='r')

        def BasisVertical():
            a = np.array([0, 0])
            b = np.array([0, self.XInputB])
            plt.plot(a, b, color='r')

        BasisHorizontal()
        BasisVertical()

    def VectorsGroupOne(self):

        def DrawVector(YInputA, XInputA, YInputB, XInputB ):
            a = np.array([YInputA, XInputA])
            b = np.array([YInputB , XInputB])
            plt.plot(a, b, color='b')

        DrawVector(1,0,0,1)


            

        
                
