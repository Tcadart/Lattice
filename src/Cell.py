import numpy as np

from .Point import *
from .Beam import *
from .Geometry_Lattice import Lattice_geometry

from scipy.sparse import coo_matrix


class Cell(object):
    """
    Define Cell data for lattice structure
    """

    def __init__(self, posCell: list, initialCellSize: list, startCellPos: list, latticeType: list[int],
                 Radius: list[float], gradRadius: list, gradDim: list, gradMat: list, uncertaintyNode: float = 0.0):
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
        uncertaintyNode: float
            Standard deviation for adding uncertainty to node coordinates. Defaults to 0.0.
        """
        self.originalTags = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007,
                             10, 11, 12, 13, 14, 15,
                             100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
        self.centerPoint = None
        self._beamMaterial = None
        self.cellSize = None
        self.posCell = posCell
        self.coordinateCell = startCellPos
        self.beams = []
        self.index = None
        self.latticeType = latticeType
        self.radius = Radius
        self.matB = None  # B matrix (Coupling matrix)
        self.uncertaintyNode = uncertaintyNode

        idxCell = 0
        for idx, rad in enumerate(self.radius):
            if rad > 0.0:
                if idxCell == 0:
                    self.getBeamMaterial(gradMat)
                    beamRadius = self.getBeamRadius(gradRadius, rad)
                    self.getCellSize(initialCellSize, gradDim)
                    self.generateBeamsInCell(self.latticeType[idx], startCellPos, beamRadius, idx)
                    self.getCellCenter(startCellPos)
                else:
                    hybridRadius = self.getBeamRadius(gradRadius, rad)
                    self.generateBeamsInCell(self.latticeType[idx], startCellPos, hybridRadius, idx)
                idxCell += 1

    def generateBeamsInCell(self, latticeType: int, startCellPos: list, beamRadius: float, beamType: int = 0) -> None:
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
        pointDict = {}
        for line in Lattice_geometry(latticeType):
            x1, y1, z1, x2, y2, z2 = map(float, line)
            if (x1, y1, z1) in pointDict:
                point1 = pointDict[(x1, y1, z1)]
            else:
                point1 = Point(x1 * self.cellSize[0] + startCellPos[0], y1 * self.cellSize[1] + startCellPos[1],
                               z1 * self.cellSize[2] + startCellPos[2], self.uncertaintyNode)
                pointDict[(x1, y1, z1)] = point1
            if (x2, y2, z2) in pointDict:
                point2 = pointDict[(x2, y2, z2)]
            else:
                point2 = Point(x2 * self.cellSize[0] + startCellPos[0], y2 * self.cellSize[1] + startCellPos[1],
                               z2 * self.cellSize[2] + startCellPos[2], self.uncertaintyNode)
                pointDict[(x2, y2, z2)] = point2
            beam = Beam(point1, point2, beamRadius, self._beamMaterial, beamType)
            self.beams.append(beam)

    def getBeamMaterial(self, gradMat: list) -> None:
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

    def getBeamRadius(self, gradRadius: list, BaseRadius: float) -> float:
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
        beamRadius = (BaseRadius * gradRadius[self.posCell[0]][0] * gradRadius[self.posCell[1]][1] *
                      gradRadius[self.posCell[2]][2])
        return beamRadius

    def getCellSize(self, initialCellSize: list, gradDim: list) -> None:
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

    def getCellCenter(self, startCellPos: list) -> None:
        """
        Calculate the center point of the cell
        """
        self.centerPoint = [startCellPos[i] + self.cellSize[i] / 2 for i in range(3)]

    def getAllPoints(self) -> list:
        """
        Determine list of points in cell
        """
        pointList = []
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                if point not in pointList:
                    pointList.append(point)
        return pointList

    def removeBeam(self, beamToDelete: "Beam") -> None:
        """
        Removes a beam from the lattice

        Parameters:
        ------------
        beamToDelete: beam Object
            Beam to remove
        """
        try:
            self.beams.remove(beamToDelete)
        except ValueError:
            print("Beam not found in the list")

    def addBeam(self, beamToAdd: "Beam") -> None:
        """
        Adding beam to cell
        """
        if isinstance(beamToAdd, Beam):
            self.beams.append(beamToAdd)
        elif isinstance(beamToAdd, tuple):
            for beam in beamToAdd:
                self.beams.append(beam)
        else:
            raise ValueError("Invalid beam type")

    def setIndex(self, index: int) -> None:
        """
        Set cell index
        """
        self.index = index

    def getPointOnSurface(self, surfaceName: str) -> list:
        """
        Get the points on the surface specified in the global reference frame.

        Parameters:
        -----------
        surfaceName: str
            Name of the surface. Choose from 'Xmin', 'Xmax', 'Ymin', 'Ymax', 'Zmin', or 'Zmax'.

        Returns:
        --------
        list
           List of points on the specified surface.
        """
        surface_map = {
            "Xmin": self.coordinateCell[0],
            "Xmax": self.coordinateCell[0] + self.cellSize[0],
            "Ymin": self.coordinateCell[1],
            "Ymax": self.coordinateCell[1] + self.cellSize[1],
            "Zmin": self.coordinateCell[2],
            "Zmax": self.coordinateCell[2] + self.cellSize[2]
        }

        if surfaceName not in surface_map:
            raise ValueError(
                "Surface " + str(surfaceName) + " is not valid. Choose from 'Xmin', 'Xmax', 'Ymin', 'Ymax', 'Zmin', "
                                                "or 'Zmax'.")

        surface_value = surface_map[surfaceName]
        coord_index = {"Xmin": "x", "Xmax": "x", "Ymin": "y", "Ymax": "y", "Zmin": "z", "Zmax": "z"}

        return [point for beam in self.beams for point in [beam.point1, beam.point2] if
                getattr(point, coord_index[surfaceName]) == surface_value]

    def getRadius(self) -> list[float]:
        """
        Get the radius of the beam
        """
        return self.radius

    def getNodeOrderToSimulate(self) -> dict:
        """
        Get the order of nodes to simulate in the cell
        """
        tag_dict = {tag: None for tag in self.originalTags}
        for beam in self.beams:
            if beam.radius > 0:
                for point in [beam.point1, beam.point2]:
                    if point.indexBoundary is not None:
                        tag = point.tagPoint(self.coordinateCell[0], self.coordinateCell[0] + self.cellSize[0],
                                             self.coordinateCell[1], self.coordinateCell[1] + self.cellSize[1],
                                             self.coordinateCell[2], self.coordinateCell[2] + self.cellSize[2])
                        if tag:  # Ensure tags is not an empty list
                            tag = tag[0]  # Take the first tag from the list
                            if tag in self.originalTags:
                                tag_dict[tag] = point
                                if not point.localTag:
                                    point.localTag.append(tag)
        return tag_dict

    def setDisplacementAtBoundaryNodes(self, displacementArray: list, displacementIndex: list) -> None:
        """
        Set displacement at nodes.

        Parameters:
        ------------
        displacementArray: list or array-like
            Flattened array of displacement values.
        displacementIndex: array of int
            Boundary node index of each displacement value.
        """
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                if point.indexBoundary is not None and point.indexBoundary in displacementIndex:
                    index = displacementIndex.index(point.indexBoundary)
                    indexActual = 0
                    for i in range(6):
                        if point.fixedDOF[i] == 0:  # Filter out the fixed DOF
                            point.setDisplacementValue(displacementArray[index + indexActual], i)
                            indexActual += 1

    def getDisplacementAtNodes(self, nodeList: dict, printing: bool = False) -> list:
        """
        Get the displacement at nodes.

        Parameters:
        -----------
        nodeList: list of Point objects
            List of nodes to get the displacement.

        Returns:
        --------
        list
            A flattened list of displacement values.
        """
        displacementList = []
        for node in nodeList.values():
            if node:
                displacement = node.getDisplacementValue()
                displacementList.append(displacement)
                # if printing:
                #     if any(0 < abs(value) > 0.1 for value in displacementList[-1][:3]):
                #         print(Fore.RED + "Displacement exceeded 0.1" + Style.RESET_ALL)
                #         print(node, displacementList[-1])
                #     if any(0 < abs(value) > 0.01 for value in displacementList[-1][3:]):
                #         print(Fore.RED + "Rotation exceeded 0.01" + Style.RESET_ALL)
                #         print(node, displacementList[-1])
                #     print(node, node.getDisplacementValue())
        return displacementList

    def setReactionForceOnEachNodes(self, nodeList: dict, reactionForce: list) -> None:
        """
        Set reaction force on each nodes.

        Parameters:
        -----------
        nodeList: list of Point objects
            List of nodes to set the reaction force.
        reactionForce: list
            List of reaction force values.
        """
        tagAlreadySet = []
        tagList = list(nodeList.keys())
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                for tag, node in nodeList.items():
                    if node == point and tag not in tagAlreadySet:
                        point.setReactionForce(reactionForce[tagList.index(tag)])
                        tagAlreadySet.append(tag)
                        break

    def getNumberOfBoundaryNodes(self) -> int:
        """
        Get the number of boundary nodes in the cell
        """
        return len(
            [beam for beam in self.beams for point in [beam.point1, beam.point2] if point.indexBoundary is not None])

    def buildCouplingOperator(self, nbFreeDOF: int) -> None:
        """
        Build the coupling operator for the cell
        """
        originalTags = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 100, 101, 102, 103, 104, 105, 106, 107,
                        108, 109, 110, 111]
        data = []
        row, col = [], []
        listBndNodes = []
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                if point.indexBoundary is not None and point.indexBoundary not in listBndNodes:
                    localNodeIndex = originalTags.index(point.localTag[0])
                    listBndNodes.append(point.indexBoundary)
                    for i in range(6):
                        if point.fixedDOF[i] == 0:
                            data.append(1)
                            col.append(localNodeIndex * 6 + i)
                            row.append(point.globalFreeDOFIndex[i])
        nbBndDOFloc = len(listBndNodes) * 6
        shapeB = (nbFreeDOF, nbBndDOFloc)
        self.matB = coo_matrix((data, (row, col)), shape=shapeB)

    def buildPreconditioner(self, SchurMatrix: "coo_matrix") -> "coo_matrix":
        """
        Build the preconditioner part for the cell

        Parameters:
        -----------
        SchurMatrix: coo_matrix
            Schur matrix
        """
        return self.matB @ SchurMatrix @ self.matB.transpose()

    def getInternalEnergy(self) -> float:
        """
        Get the internal energy of the cell
        """
        internalEnergy = 0
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                if point.indexBoundary is not None:
                    pointEnergy = point.calculatePointEnergy()
                    # if pointEnergy < 0:
                    #     print("Negative energy", pointEnergy)
                    internalEnergy += pointEnergy
        return internalEnergy

    def getDisplacementData(self) -> list:
        """
        Build and return displacement data on cell for dataset generation
        """
        allBoundaryDisplacementData = []
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                if point.indexBoundary is not None:
                    allBoundaryDisplacementData.append(point.getDisplacementValue())
        return allBoundaryDisplacementData

    def changeBeamRadius(self, newRadius: list, gradRadius: list = None, penalizationCoeff: float = 1.5) -> None:
        """
        Change beam radius in the cell

        Parameters:
        -----------
        newRadius: list
            beam radius wanted to assign
        hybridData: list
            Hybrid data type
        gradRadius: list
            Gradient of the radius
        penalizationCoeff: float
        """
        assert len(newRadius) == len(self.radius), ("Length of new radius vector and already cell radius vector needs "
                                                    "to be equal ")
        beamRadius = []
        for rad in newRadius:
            beamRadius.append(self.getBeamRadius(gradRadius, rad))

        for beam in self.beams:
            if beam.modBeam:
                beam.setRadius(beamRadius[beam.type] * penalizationCoeff)
            else:
                beam.setRadius(beamRadius[beam.type])

        self.radius = newRadius

    def getVolumeCell(self) -> float:
        """
        Get the volume of the cell
        """
        return self.cellSize[0] * self.cellSize[1] * self.cellSize[2]

    def getRelativeDensity(self) -> float:
        """
        Get the relative density of the cell
        """
        volumeBeams = 0
        for beam in self.beams:
            volumeBeams += beam.getVolume()
        return volumeBeams / self.getVolumeCell()

    def getRelativeDensityGradient(self, relativeDensityPolyDeriv) -> float:
        """
        Get the gradient of the relative density

        Parameters:
        -----------
        relativeDensityPolyDeriv: list
            List of polynomial derivative functions

        Returns:
        --------
        deriv: float
            Derivative of the relative density
        """
        deriv = 0
        for idx, polyDeriv in enumerate(relativeDensityPolyDeriv):
            deriv += polyDeriv(self.radius[idx])
        return deriv

    def getNumberNodesAtBoundary(self):
        """
        Get the number of nodes at the boundary

        Returns:
        --------
        int
            Number of nodes at the boundary
        """
        counterNodes = 0
        nodeAlreadyCounted = []
        for beam in self.beams:
            for point in [beam.point1, beam.point2]:
                if point.indexBoundary is not None and point.indexBoundary not in nodeAlreadyCounted:
                    counterNodes += 1
                    nodeAlreadyCounted.append(point.indexBoundary)
        return counterNodes

    def getRGBcolorDependingOfRadius(self):
        return tuple(r / 0.1 for r in self.radius)
