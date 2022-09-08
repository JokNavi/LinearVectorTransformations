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
        Spacing = 2 
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
        BasisVectors(Height,Width)
        def SetVectors():
            for Vector in range(VectorAmount):
                FinalHeight = Height * 3
                FinalWidth = Width * 3
                x = np.array([0,0])
                y = np.array([0,0])
                plt.plot(x,y, color = 'b')
                Spacing = Spacing + 2 
        SetVectors()
       
   
    
