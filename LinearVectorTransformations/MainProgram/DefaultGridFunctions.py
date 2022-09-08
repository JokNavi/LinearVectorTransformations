import numpy as np
import matplotlib.pyplot as plt

class DefaultLayout:
    
    def MyGrid():
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()
    def VectorEditor(Height, Width, Vectors, Space):
        VectorAmount = Vectors + 1
        def BasisVectors(XInput,YInput):
            def BasisX():
                x = np.array([0,0])
                y = np.array([XInput,0])
                plt.plot(x,y, color = 'r')
            def BasisY():
                x = np.array([0,YInput])
                y = np.array([0,0])
                plt.plot(x,y, color = 'r')
            BasisX()
            BasisY()
        def CreateVectorsX(Spacing, FinalHeight):
            x = np.array([Spacing,Spacing])
            y = np.array([FinalHeight,0])
            plt.plot(x,y, color = 'b')
        def CreateVectorsY(Spacing, FinalWidth):
            x = np.array([0,FinalWidth])
            y = np.array([Spacing,Spacing])
            plt.plot(x,y, color = 'b')
        def SetVectors():
            Spacing = 0
            for Vector in range(VectorAmount):
                FinalHeight = (Height * Vectors) * Space
                FinalWidth = (Width * Vectors)
                CreateVectorsX(Spacing, FinalHeight)
                CreateVectorsY(Spacing, FinalWidth)
                Spacing = Spacing + Space
        SetVectors()
        BasisVectors(Height,Width)
       
   
    
