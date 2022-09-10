import numpy as np
import matplotlib.pyplot as plt


class DefaultLayout:

    def __init__(self, Height, Width):
        self.XInput = Width
        self.YInput = Height
        
    
    def MyGrid(self):
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()

    # Creates the vectors in our program
    def VectorEditor(self, Vectors, Space):
        VectorAmount = Vectors + 1

        # Creates basis vectors acording to height and width (XInput,YInput)
        def BasisVectors(self):
            
            def BasisX():
                x = np.array([0, 0])
                y = np.array([self.XInput, 0])
                plt.plot(x, y, color='r')

            def BasisY():
                x = np.array([0, self.YInput])
                y = np.array([0, 0])
                plt.plot(x, y, color='r')
            
            BasisX()
            BasisY()
             
        def VectorsTLBR(self):
            def TestVector():
                x = np.array([1, 0])
                y = np.array([0, 1])
                plt.plot(x, y, color='b')
            TestVector() 

        BasisVectors(self)
        VectorsTLBR(self)
