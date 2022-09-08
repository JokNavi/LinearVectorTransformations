import matplotlib.pyplot as plt
from MainProgram.LinearVectorTransformations import DefaultLayout
DL = DefaultLayout


class RunProgram:
    def SquareGrid():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACE = 1
        DL.MyGrid()
        DL.VectorEditor(1, 1, VECTORS, SPACE)
        plt.show()

    def VectorTransformations():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACE = 1
        DL.MyGrid()
        DL.VectorEditor(1, 1, VECTORS, SPACE)
        plt.show()


RunProgram()
