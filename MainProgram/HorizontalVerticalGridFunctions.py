import numpy as np
import matplotlib.pyplot as plt


class DefaultLayoutS:

    def MyGrid():
        plt.title("Linear Vector Transformations")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.grid()

    # Creates the vectors in our program
    def VectorEditor(Height, Width, Vectors, Space):
        VectorAmount = Vectors + 1

        # Creates basis vectors acording to height and width (XInput,YInput)
        def BasisVectors(XInput, YInput):
            def BasisX():
                x = np.array([0, 0])
                y = np.array([XInput, 0])
                plt.plot(x, y, color='r')

            def BasisY():
                x = np.array([0, YInput])
                y = np.array([0, 0])
                plt.plot(x, y, color='r')
            BasisX()
            BasisY()

        # Creates all the X vectors based on the Basis vector
        def CreateVectorsX(Spacing, FinalHeight):
            x = np.array([Spacing, Spacing])
            y = np.array([FinalHeight, 0])
            plt.plot(x, y, color='b')

        # Creates all the Y vectors based on the Basis vector
        def CreateVectorsY(Spacing, FinalWidth):
            x = np.array([0, FinalWidth])
            y = np.array([Spacing, Spacing])
            plt.plot(x, y, color='b')

        # Modifies the input values and calls the vector creating functions
        def SetVectors():
            Spacing = 0
            for Vector in range(VectorAmount):
                FinalHeight = (Height * Vectors) * Space
                FinalWidth = (Width * Vectors)
                CreateVectorsX(Spacing, FinalHeight)
                CreateVectorsY(Spacing, FinalWidth)
                Spacing = Spacing + Space
        SetVectors()
        BasisVectors(Height, Width)
