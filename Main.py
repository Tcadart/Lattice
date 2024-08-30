import sys

from Lattice import *
import matplotlib.pyplot as plt
import math

# *******************************************************************************************************************
# *******************************************************************************************************************

# Variables

# *******************************************************************************************************************
# *******************************************************************************************************************
# Lattice properties
Radius = 0.1
cell_size = 1
cell_size_X = cell_size
cell_size_Y = cell_size
cell_size_Z = cell_size
number_cell = 1
number_cell_X = 2
number_cell_Y = 2
number_cell_Z = 2

Lattice_Type = 0
# -2 => Method random cell
# -1 => Full random
# 0 => BCC
# 1 => Octet
# 2 => OctetExt
# 3 => OctetInt
# 4 => BCCZ
# 5 => Cubic
# 6 => OctahedronZ
# 7 => OctahedronZcross
# 8 => Kelvin
# 9 => Cubic formulation 2 (centered)
# 10 => Cubic V3
# 11 => Cubic V4
# 12 => New lattice (non connu) GPT generated
# 13 => Diamond
# 14 => Auxetic

# Gradient on cell dimensions
GradDimRule = 'constant'
GradDimDirection = [1, 0, 1]
GradDimParameters = [1.5, 0.0, 1.5]  # Float
# Gradient on radius of beams
GradRadRule = 'constant'
GradRadDirection = [0, 0, 1]
GradRadParameters = [1.0, 0.0, 2.0]
# Gradient Rule
# - constant
# - linear
# - parabolic
# - sinusoide
# - exponential

Multimat = 0
# -1 => Full random
# 0 -> materiaux
# 1 -> multimat par couche
GradMaterialDirection = 3  # 1:X / 2:Y / 3:Z

MethodSim = 1
# 0 No modification
# 1 Node Modification

uncertaintyNode = 0

# *******************************************************************************************************************
# *******************************************************************************************************************

# Main

# *******************************************************************************************************************
# *******************************************************************************************************************
# Gradient properties
gradDimProperty = [GradDimRule, GradDimDirection, GradDimParameters]
gradRadiusProperty = [GradRadRule, GradRadDirection, GradRadParameters]
gradMatProperty = [Multimat, GradMaterialDirection]

erasedParts = [(30.0, 0.0, 0.0, 19.0, 50.0, 19.0)]

# #Generate data from lattice
lattice = Lattice(cell_size_X, cell_size_Y, cell_size_Z, number_cell_X, number_cell_Y, number_cell_Z, Lattice_Type,
                  Radius, gradRadiusProperty, gradDimProperty, gradMatProperty, MethodSim, uncertaintyNode,
                  erasedParts=None)

lattice.defineNodeIndexBoundary()

# AFAIRE Fonction pour déterminer les cells index dans la structure
lattice.applyBoundaryConditionsOnSurface([0], "Xmin", [-1, 0, 0, 0, 0, 0])
# lattice.applyBoundaryConditionsOnSurface([6], "Zmax", [0, 0, 0, 0, 0, 0])
lattice.fixDOFOnSurface([3], "Zmax", [0, 1, 2])


globalDisplacement = lattice.getDisplacementGlobal()
print(globalDisplacement)

for cell in lattice.cells:
    nodeInOrder = cell.getNodeOrderToSimulate()
    cell.setDisplacementAtBoundaryNodes(globalDisplacement)
    displacement = cell.getDisplacementAtBoundaryNodes(nodeInOrder)

# lattice.attractorLattice((40, 25, 0), alpha=0.005)
# hybridLatticeData = [0.01]
# lattice = Lattice.hybridgeometry(cell_size_X, cell_size_Y, cell_size_Z, MethodSim, uncertaintyNode,
#                                  hybridLatticeData, hybridGeomType=[0])

# lattice = Lattice.simpleLattice(cell_size_X,cell_size_Y,cell_size_Z, number_cell_X,number_cell_Y,number_cell_Z,
# Lattice_Type,Radius)
# display_only_cell_random()
lattice.visualizeLattice3D("Type", deformedForm=True)
