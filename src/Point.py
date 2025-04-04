import random
from typing import List, Tuple


class Point:
    """
    Represents a point in 3D space with additional attributes for simulation.
    """

    def __init__(self, x: float, y: float, z: float, nodeUncertaintySD: float = 0.0) -> None:
        """
        Initialize a Point object.

        Args:
            x (float): X-coordinate of the point.
            y (float): Y-coordinate of the point.
            z (float): Z-coordinate of the point.
            nodeUncertaintySD (float, optional): Standard deviation for adding uncertainty to node coordinates. Defaults to 0.0.
        """
        self.x = float(x) + random.gauss(0, nodeUncertaintySD)
        self.y = float(y) + random.gauss(0, nodeUncertaintySD)
        self.z = float(z) + random.gauss(0, nodeUncertaintySD)
        self.index = None # Global index of the point
        self.tag = None # Global boundary tag
        self.localTag = [] # Cell local boundary tag
        self.indexBoundary = None # Global index for boundary cell
        self.displacementValue= [0.0] * 6  # Displacement vector of 6 DOF (Degrees of Freedom).
        self.reactionForceValue = [0.0] * 6  # Reaction force vector of 6 DOF.
        self.appliedForce = [0.0] * 6  # Applied force vector of 6 DOF.
        self.fixedDOF = [0] * 6  # Fixed DOF vector (0: free, 1: fixed).
        self.globalFreeDOFIndex = [None] * 6  # Global free DOF index.
        self.nodeMod = False

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Point) and self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __sub__(self, other: 'Point') -> List[float]:
        return [self.x - other.x, self.y - other.y, self.z - other.z]

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z}, Index:{self.index})"

    def movePoint(self, xNew: float, yNew: float, zNew: float) -> None:
        """
        Move the point to new coordinates.

        Args:
            xNew (float): New X-coordinate.
            yNew (float): New Y-coordinate.
            zNew (float): New Z-coordinate.
        """
        self.x, self.y, self.z = xNew, yNew, zNew

    def getPos(self) -> Tuple[float, float, float]:
        """
        Retrieve the current position of the point.

        Returns:
            Tuple[float, float, float]: (x, y, z) coordinates of the point.
        """
        return self.x, self.y, self.z

    def setIndex(self, index: int) -> None:
        """
        Set the index of the point.

        Args:
            index (int): Index to assign.
        """
        self.index = index

    def getData(self) -> List[float]:
        """
        Retrieve point data for exporting.

        Returns:
            List[float]: [index, x, y, z] of the point.
        """
        return [self.index, self.x, self.y, self.z]


    def tagPoint(self, boundaryBoxDomain) -> List[int]:
        """
        Generate standardized tags for the point based on its position.

        Parameters
        ----------
        boundaryBoxDomain : List[float]
            Boundary box domain containing [xMin, xMax, yMin, yMax, zMin, zMax].

        Returns
        -------
        List[int]
            List of tags associated with the point.
        """
        if len(boundaryBoxDomain) != 6:
            raise ValueError("Boundary box domain must contain 6 values.")
        xMin, xMax, yMin, yMax, zMin, zMax = boundaryBoxDomain

        tag: List[int] = []
        # Faces
        if self.x == xMin and (yMin < self.y < yMax) and (
                zMin < self.z < zMax):
            tag.append(12)  # Face 1
        elif self.x == xMax and (yMin < self.y < yMax) and (
                zMin < self.z < zMax):
            tag.append(13)  # Face 2
        elif (xMin < self.x < xMax) and self.y == yMin and (
                zMin < self.z < zMax):
            tag.append(11)  # Face 3
        elif (xMin < self.x < xMax) and self.y == yMax and (
                zMin < self.z < zMax):
            tag.append(14)  # Face 4
        elif (xMin < self.x < xMax) and (
                yMin < self.y < yMax) and self.z == zMin:
            tag.append(10)  # Face 5
        elif (xMin < self.x < xMax) and (
                yMin < self.y < yMax) and self.z == zMax:
            tag.append(15)  # Face 6

        # Edge
        if self.x == xMin and self.y == yMin and (zMin < self.z < zMax):
            tag.append(102)  # Edge 0
        elif (xMin < self.x < xMax) and self.y == yMin and self.z == zMin:
            tag.append(100)  # Edge 1
        elif self.x == xMax and self.y == yMin and (zMin < self.z < zMax):
            tag.append(104)  # Edge 2
        elif (xMin < self.x < xMax) and self.y == yMin and self.z == zMax:
            tag.append(108)  # Edge 3
        elif self.x == xMin and (yMin < self.y < yMax) and self.z == zMin:
            tag.append(101)  # Edge 4
        elif self.x == xMax and (yMin < self.y < yMax) and self.z == zMin:
            tag.append(103)  # Edge 5
        elif self.x == xMin and self.y == yMax and (zMin < self.z < zMax):
            tag.append(106)  # Edge 6
        elif (xMin < self.x < xMax) and self.y == yMax and self.z == zMin:
            tag.append(105)  # Edge 7
        elif self.x == xMax and self.y == yMax and (zMin < self.z < zMax):
            tag.append(107)  # Edge 8
        elif (xMin < self.x < xMax) and self.y == yMax and self.z == zMax:
            tag.append(111)  # Edge 9
        elif self.x == xMin and (yMin < self.y < yMax) and self.z == zMax:
            tag.append(109)  # Edge 10
        elif self.x == xMax and (yMin < self.y < yMax) and self.z == zMax:
            tag.append(110)  # Edge 11

        # Corner
        if self.x == xMin and self.y == yMin and self.z == zMin:
            tag.append(1000)  # Corner 0
        elif self.x == xMax and self.y == yMin and self.z == zMin:
            tag.append(1001)  # Corner 1
        elif self.x == xMin and self.y == yMax and self.z == zMin:
            tag.append(1002)  # Corner 2
        elif self.x == xMax and self.y == yMax and self.z == zMin:
            tag.append(1003)  # Corner 3
        elif self.x == xMin and self.y == yMin and self.z == zMax:
            tag.append(1004)  # Corner 4
        elif self.x == xMax and self.y == yMin and self.z == zMax:
            tag.append(1005)  # Corner 5
        elif self.x == xMin and self.y == yMax and self.z == zMax:
            tag.append(1006)  # Corner 6
        elif self.x == xMax and self.y == yMax and self.z == zMax:
            tag.append(1007)  # Corner 7
        return tag

    def setTag(self, tag: List[int]) -> None:
        """
        Assign tags to the point.

        Args:
            tag (List[int]): Tags to assign.
        """
        self.tag = tag

    def setDisplacementValue(self, displacementValue: float, DOF: int) -> None:
        """
        Assign displacement value to a specific degree of freedom.

        Args:
            displacementValue (float): Displacement value.
            DOF (int): Degree of freedom (0 to 5).
        """
        self.displacementValue[DOF] = displacementValue

    def setDisplacementVector(self, displacementVector: List[float]) -> None:
        """
        Assign displacement values to the point.

        Args:
            displacementVector (List[float]): Displacement values for all DOF.
        """
        self.displacementValue = displacementVector

    def setForceValue(self, forceValue: float, DOF: int) -> None:
        """
        Assign force value to a specific degree of freedom.

        Args:
            forceValue (float): Force value.
            DOF (int): Degree of freedom (0 to 5).
        """
        self.appliedForce[DOF] = forceValue

    def setAppliedForce(self, appliedForce: List[float], DOF:list[int]) -> None:
        """
        Assign applied force to the point.

        Parameters
        ----------
        appliedForce : List[float]
            Applied force values for each DOF.
        DOF : list[int]
            List of DOF to assign (0: x, 1: y, 2: z, 3: Rx, 4: Ry, 5: Rz).
        """
        if len(DOF) != len(appliedForce):
            raise ValueError("Length of DOF and appliedForce must be equal.")
        for i in range(len(DOF)):
            self.appliedForce[DOF[i]] = appliedForce[i]

    def getAppliedForce(self) -> List[float]:
        """
        Retrieve the applied force values.

        Returns:
            List[float]: Applied force values for all DOF.
        """
        return self.appliedForce

    def getDisplacementValue(self) -> List[float]:
        """
        Retrieve the displacement values of the point.

        Returns:
            List[float]: Displacement values for all DOF.
        """
        return self.displacementValue

    def initializeReactionForce(self) -> None:
        """
        Reset the reaction force vector to zero.
        """
        self.reactionForceValue = [0.0] * 6

    def setReactionForce(self, reactionForce: List[float]) -> None:
        """
        Assign reaction force to the point.

        Args:
            reactionForce (List[float]): Reaction force values for each DOF.
        """
        for i in range(len(self.reactionForceValue)):
            self.reactionForceValue[i] += reactionForce[i]

    def getReactionForce(self) -> List[float]:
        """
        Retrieve the reaction force values.

        Returns:
            List[float]: Reaction force values for all DOF.
        """
        return self.reactionForceValue

    def setIndexBoundary(self, index: int) -> None:
        """
        Assign a boundary index to the point.

        Args:
            index (int): Boundary index to assign.
        """
        self.indexBoundary = index

    def getIndexBoundary(self) -> int:
        """
        Retrieve the boundary index of the point.

        Returns:
            int: Boundary index.
        """
        return self.indexBoundary

    def getDeformedPos(self) -> Tuple[float, float, float]:
        """
        Retrieve the deformed position of the point.

        Returns:
            Tuple[float, float, float]: (x, y, z) coordinates including displacements.
        """
        return (self.x + self.displacementValue[0],
                self.y + self.displacementValue[1],
                self.z + self.displacementValue[2])

    def fixDOF(self, DOF: List[int]) -> None:
        """
        Fix specific degrees of freedom for the point.

        Args:
            DOF (List[int]): List of DOF to fix (0: x, 1: y, 2: z, 3: Rx, 4: Ry, 5: Rz).
        """
        for i in DOF:
            self.fixedDOF[i] = 1

    def initializeDisplacementToZero(self) -> None:
        """
        Reset displacement values to zero for all DOF.
        """
        self.displacementValue = [0.0] * 6

    def calculatePointEnergy(self) -> float:
        """
        Calculate the internal energy of the point.

        Returns:
            float: Internal energy based on displacement and reaction forces.
        """
        return sum([self.displacementValue[i] * self.reactionForceValue[i] for i in range(6)])

    def setLocalTag(self, localTag: List[int]) -> None:
        """
        Assign local tags to the point.

        Parameters
        ----------
        localTag : List[int]
            Local tags to assign.
        """
        if not isinstance(localTag, list):
            raise ValueError("Local tag must be a list.")
        self.localTag = localTag

    def setNodeMod(self, nodeMod: bool) -> None:
        """
        Assign node modification status.

        Parameters
        ----------
        nodeMod : bool
            Node modification status.
        """
        self.nodeMod = nodeMod

