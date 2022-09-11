import numpy as np
import matplotlib.pyplot as plt


class DefaultLayout:

    def MyGrid():
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()

    # Creates the vectors in our program
    def VectorEditor(Height, Width, Vectors, Space):
        XInputHeight = Vectors
        YInputWidth = Vectors
        VectorAmount = Vectors + 1

        # Creates basis vectors acording to height and width (XInput,YInput)
        def BasisVectors(XInput, YInput):
            def BasisX():
                x = np.array([0, 0])
                y = np.array([XInputHeight, XInputHeight])
                plt.plot(x, y, color='r')

            def BasisY():
                x = np.array([0, YInputWidth])
                y = np.array([YInputWidth, 0])
                plt.plot(x, y, color='r')
            BasisX()
            BasisY()

        # Creates all the X vectors based on the Basis vector
        def CreateVectorsOne(Spacing, FinalHeight):
            x = np.array([0, 0])
            y = np.array([FinalHeight, FinalHeight])
            plt.plot(x, y, color='b')

        # Creates all the Y vectors based on the Basis vector
        def CreateVectorsTwo(Spacing, FinalWidth):
            x = np.array([FinalWidth, 0])
            y = np.array([0, FinalWidth])
            plt.plot(x, y, color='b')

        # Modifies the input values and calls the vector creating functions
        def SetVectors():
            Spacing = 0
            for Vector in range(VectorAmount):
                FinalHeight = (Height * Vectors) * Space
                FinalWidth = (Width * Vectors) * Space
                CreateVectorsOne(Spacing, FinalHeight)
                CreateVectorsTwo(Spacing, FinalWidth)
                Spacing = Spacing + Space
        #SetVectors()
        BasisVectors(Height, Width)
