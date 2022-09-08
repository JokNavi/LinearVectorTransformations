import numpy as np
import matplotlib.pyplot as plt

class DefaultLayout:
    
    def MyGrid():
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()
    def VectorEditor():
        VectorAmount = 9
        Height = 1
        Width = 1
        ModifierHeight = 0
        ModifierWidth = 0
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
                FinalHeight = Height * 16
                FinalWidth = Width * 16
                CreateVectorsX(Spacing, FinalHeight)
                CreateVectorsY(Spacing, FinalWidth)
                Spacing = Spacing + 2 
        SetVectors()
        BasisVectors(Height,Width)
       
   
    
