from Point import *
from Beam import *
import math
import random
from Geometry_Lattice import Lattice_geometry

import sys
if sys.version_info[0] == 3:
    from scipy.sparse import coo_matrix


class Cell(object):
    """
    Define Cell data for lattice structure
    """

    def __init__(self, posCell, initialCellSize, startCellPos, latticeType,
                 Radius, gradRadius, gradDim, gradMat):
        """
        Initialize a Cell with its dimensions and position

        Parameters:
        -----------
        posCell: list
            Position of the cell in the lattice
        initialCellSize: list
            Initial size of the cell
        startCellPos: list
            Position of the start of the cell
        latticeType: int
            Type of lattice geometry
        Radius: float
            Base radius of the beam
        gradRadius: list
            Gradient of the radius
        gradDim: list
            Gradient of the dimensions
        gradMat: list
            Gradient of the material
        """
        self.centerPoint = None
        self._beamMaterial = None
        self._beamRadius = None
        self.cellSize = None
        self.posCell = posCell
        self.coordinateCell = startCellPos
        self.beams = []
        self.index = None
        self.latticeType = latticeType
        self.hybridRadius = None
        self.matB = None  # B matrix (Coupling matrix)

        self.getBeamMaterial(gradMat)
        self.getBeamRadius(gradRadius, Radius)
        self.getCellSize(initialCellSize, gradDim)
        self.generateBeamsInCell(latticeType, startCellPos)
        self.getCellCenter(startCellPos)

    def generateBeamsInCell(self, latticeType, startCellPos, beamType=0):
        """
        Generate beams and nodes using a given lattice type and parameters.

        Parameters:
        -----------
        latticeType: int
            Type of lattice geometry
        startCellPos: list
            Position of the start of the cell
        beamType: int
            Type of beam
        """
        for line in Lattice_geometry(latticeType):
            x1, y1, z1, x2, y2, z2 = map(float, line)
            point1 = Point(x1 * self.cellSize[0] + startCellPos[0], y1 * self.cellSize[1] + startCellPos[1],
                           z1 * self.cellSize[2] + startCellPos[2])
            point2 = Point(x2 * self.cellSize[0] + startCellPos[0], y2 * self.cellSize[1] + startCellPos[1],
                           z2 * self.cellSize[2] + startCellPos[2])
            beam = Beam(point1, point2, self._beamRadius, self._beamMaterial, beamType)
            self.beams.append(beam)

    def getBeamMaterial(self, gradMat):
        """
        Get the material of the beam based on the gradient and position.

        Parameters:
        -----------
        gradMat: list
            Gradient of the material

        Returns:
        ---------
        materialType: int
            Material index of the beam
        """
        self._beamMaterial = gradMat[self.posCell[2]][self.posCell[1]][self.posCell[0]]

    def getBeamRadius(self, gradRadius, BaseRadius):
        """
        Calculate and return the beam radius

        Parameters:
        -----------
        gradRadius: list
            Gradient of the radius
        BaseRadius: float
            Base radius of the beam

        Returns:
        ---------
        actualBeamRadius: float
            Calculated beam radius
        """
        self._beamRadius = BaseRadius * gradRadius[self.posCell[0]][0] * gradRadius[self.posCell[1]][1] * \
                           gradRadius[self.posCell[2]][2]

    def getCellSize(self, initialCellSize, gradDim):
        """
        Calculate and return the cell size

        Parameters:
        -----------
        initialCellSize: 3-array
            Dimension of the initial cell without modification
        gradDim:

        Returns:
        ---------
        cellSize : float
            Calculated beam radius
        """
        self.cellSize = [initial_size * gradDim[pos][i] for i, (initial_size, pos) in
                         enumerate(zip(initialCellSize, self.posCell))]

    def getCellCenter(self, startCellPos):
        """
        Calculate the center point of the cell
        """
        self.centerPoint = [startCellPos[i] + self.cellSize[i] / 2 for i in range(3)]

    def getAllPoints(self):
        """
        Determine list of points in cell
        """
        pointList = []
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                if point not in pointList:
                    pointList.append(point)
        return pointList

    def removeBeam(self, beamToDelete):
        """
        Removes a beam from the lattice

        Parameters:
        ------------
        beamToDelete: beam Object
            Beam to remove
        """
        self.beams.remove(beamToDelete)


    def addBeam(self, beamToAdd):
        """
        Adding beam to cell
        """
        self.beams.append(beamToAdd)

    def setIndex(self, index):
        """
        Set cell index
        """
        self.index = index



    def add_point(self, point):
        x, y, z = map(float, point)
        point_obj = Point((x) * self.cellSizeX + self.x, (y) * self.cellSizeY + self.y,
                          (z) * self.cellSizeZ + self.z)
        self.nodes.append(point_obj)





    def defineHybridRadius(self, hybridRadius):
        """
        Define hybrid radius for the cell

        Parameters:
        -----------
        hybridRadius: list of float dim 3
            Hybrid radius of the cell
        """
        self.hybridRadius = hybridRadius

    def getHybridRadius(self):
        """
        Return hybrid radius of the cell
        """
        return self.hybridRadius




