import matplotlib.pyplot as plt
from LinearVectorTransformations import DefaultLayout
from HorizontalVerticalGridFunctions import DefaultLayoutS
<<<<<<< HEAD
DLS = DefaultLayoutS
DL = DefaultLayout
=======


>>>>>>> 139da34931291fac260e091722e85d8b63d4ee49



class RunProgram:
    def SquareGrid():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACE = 1
<<<<<<< HEAD
=======
        DLS = DefaultLayoutS
>>>>>>> 139da34931291fac260e091722e85d8b63d4ee49
        DLS.MyGrid()
        DLS.VectorEditor(1, 1, VECTORS, SPACE)
        plt.show()

    def VectorTransformations():
        # Change these inputs (Vectors and Space)
        VECTORS = 10
        SPACING = 1
        Height = 1
        Width = 1
        DL = DefaultLayout(Height, Width, VECTORS, SPACING)
        DL.MyGrid()
        DL.BasisVectors()
        DL.VectorsGroupOne()
        DL.VectorGroupTwo()
        plt.show()
    VectorTransformations()
    #SquareGrid()

    VectorTransformations()
    #SquareGrid()


RunProgram()
