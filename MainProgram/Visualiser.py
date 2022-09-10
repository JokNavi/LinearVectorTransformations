import matplotlib.pyplot as plt
from LinearVectorTransformations import DefaultLayout
from HorizontalVerticalGridFunctions import DefaultLayoutS
DLS = DefaultLayoutS
DL = DefaultLayout


class RunProgram:
    def SquareGrid():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACE = 1
        DLS.MyGrid()
        DLS.VectorEditor(1, 1, VECTORS, SPACE)
        plt.show()

    def VectorTransformations():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACE = 1
        DL.MyGrid()
        DL.VectorEditor(1, 1, VECTORS, SPACE)
        plt.show()

    VectorTransformations()
    #SquareGrid()


RunProgram()
