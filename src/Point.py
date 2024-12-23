import random


class Point(object):
    """
    Point object represent a point by 3 coordinates x, y, z
    """

    def __init__(self, x, y, z, nodeUncertaintySD=0.0):
        """
        Create a point object

        Parameters:
        ------------
        x: float
            x coordinate of the point
        y: float
            y coordinate of the point
        z: float
            z coordinate of the point
        """
        self.x = float(x) + random.gauss(0, nodeUncertaintySD)
        self.y = float(y) + random.gauss(0, nodeUncertaintySD)
        self.z = float(z) + random.gauss(0, nodeUncertaintySD)
        self.index = None
        self.tag = []
        self.localTag = []
        self.indexBoundary = None
        self.displacementValue = [0, 0, 0, 0, 0, 0]  # Displacement vector of Dimension 6 to simulate lattice behavior
        self.reactionForceValue = [0, 0, 0, 0, 0,
                                   0]  # Reaction force vector of Dimension 6 to simulate lattice behavior
        self.fixedDOF = [0, 0, 0, 0, 0, 0]  # Fixed DOF vector of Dimension 6 (0: free, 1: fixed)
        self.globalFreeDOFIndex = [None] * 6  # Global free DOF index

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __sub__(self, other):
        return [self.x - other.x, self.y - other.y, self.z - other.z]

    def __repr__(self):
        return "Point({}, {}, {}, , Index:{})".format(self.x, self.y, self.z, self.index)

    def movePoint(self, xNew, yNew, zNew):
        """
        Move point at x, y, z
        """
        self.x = xNew
        self.y = yNew
        self.z = zNew

    def getPos(self):
        """
        Return list of node position
        """
        return self.x, self.y, self.z

    def setIndex(self, index):
        """
        Set node index
        """
        self.index = index

    def getData(self):
        """
        Return data structure to export lattice
        """
        return [self.index, self.x, self.y, self.z]

    def tagPoint(self, xMin, xMax, yMin, yMax, zMin, zMax):
        """
        Define standardized tags for a point
        link : https://docs.fenicsproject.org/basix/v0.2.0/index.html

        Parameter:
        ----------
        point: Point Object

        Return:
        --------
        tags: array of integer
            List of tags of the point
        """
        tag = []
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

    def setTag(self, tag):
        """
        Set tag to point
        """
        self.tag = tag

    def setDisplacementValue(self, displacementValue, DOF):
        """
        Apply displacementValue to node

        Parameters:
        ------------
        displacementValue: float
            Displacement value
        DOF: int
            Degree of freedom
        """
        self.displacementValue[DOF] = displacementValue

    def getDisplacementValue(self):
        """
        Return displacement value
        """
        return self.displacementValue

    def initializeReactionForce(self):
        """
        Initialize reaction force
        """
        self.reactionForceValue = [0, 0, 0, 0, 0, 0]

    def setReactionForce(self, reactionForce):
        """
        Set reaction force to node
        """
        for i in range(len(self.reactionForceValue)):
            self.reactionForceValue[i] += reactionForce[i]

    def getReactionForce(self):
        """
        Return reaction force
        """
        return self.reactionForceValue

    def setIndexBoundary(self, index):
        """
        Set tag to point
        """
        self.indexBoundary = index

    def getIndexBoundary(self):
        """
        Return tag
        """
        return self.indexBoundary

    def getDeformedPos(self):
        """
        Return list of node position
        """
        return self.x + self.displacementValue[0], self.y + self.displacementValue[1], self.z + self.displacementValue[
            2]

    def fixDOF(self, DOF):
        """
        Fix DOF
        """
        for i in DOF:
            self.fixedDOF[i] = 1

    def initializeDisplacementToZero(self):
        """
        Initialize displacement to zero
        """
        self.displacementValue = [0, 0, 0, 0, 0, 0]

    def calculatePointEnergy(self):
        """
        Calculate internal energy of the node
        """
        return sum([self.displacementValue[i] * self.reactionForceValue[i] for i in range(6)])
