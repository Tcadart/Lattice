from src.settings import *
from src.Lattice import *

# Generate data from lattice
# if Lattice_Type != 1000:
#     lattice = Lattice(cell_size_X, cell_size_Y, cell_size_Z, number_cell_X, number_cell_Y, number_cell_Z, Lattice_Type,
#                       Radius, gradRadiusProperty, gradDimProperty, gradMatProperty, MethodSim, uncertaintyNodeSD)
# else:
#     lattice = Lattice.hybridgeometry(cell_size_X, cell_size_Y, cell_size_Z, MethodSim, uncertaintyNodeSD,
#                                      hybridLatticeData, hybridGeomType=[0, 16, 19])
    # lattice.changeCellRadiusProperties(3, [0.0, 0.1, 0.0])

lattice = Lattice(cell_size_X, cell_size_Y, cell_size_Z, number_cell_X, number_cell_Y, number_cell_Z, Lattice_Type,
                  Radius, gradRadiusProperty, gradDimProperty, gradMatProperty, MethodSim, uncertaintyNodeSD,
                  hybridLatticeData, hybridGeomType = [0, 16, 19], randomHybrid=False)
# lattice.changeCellRadiusProperties(0, [0.02, 0.01, 0.01])

# Définir une surface quadratique
surface_equation = lambda x, y: 3*math.sin(x)/2 + math.sin(y)/2

# Ajuster le lattice à cette surface
lattice.fitToSurface(equation=surface_equation)

lattice.saveJSONToGrasshopper("HybridRandom")

fig = lattice.visualizeLattice3D("Radius", deformedForm=True, plotCellIndex=False, voxelViz=False)
# fig.show()
