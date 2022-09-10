import matplotlib.pyplot as plt
from LinearVectorTransformations import DefaultLayout
from HorizontalVerticalGridFunctions import DefaultLayoutS




class RunProgram:
    def SquareGrid():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACE = 1

        DLS = DefaultLayoutS
        DLS.MyGrid()
        DLS.VectorEditor(1, 1, VECTORS, SPACE)
        plt.show()

    def VectorTransformations():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACE = 1
        DL = DefaultLayout(1, 1, VECTORS)
        DL.MyGrid()
        DL.BasisVectors()
        DL.VectorsTLBR()
        plt.show()

    VectorTransformations()
    # SquareGrid()


RunProgram()
