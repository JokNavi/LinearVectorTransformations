import matplotlib.pyplot as plt
from DefaultGridFunctions import DefaultLayout
DL = DefaultLayout
class RunProgram:
  VECTORS = 10
  SPACE = 1
  DL.MyGrid()
  DL.VectorEditor(1, 1, VECTORS, SPACE)
  plt.show()
RunProgram()