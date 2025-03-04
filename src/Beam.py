from typing import List, Tuple
import math

import numpy as np
import trimesh


class Beam(object):
    """
    Class Beam represents a beam element in lattice structures.
    """

    def __init__(self, point1: 'Point', point2: 'Point', Radius: float, Material: int, Type: int) -> None:
        """
        Initialize a Beam object representing a beam element.

        Args:
            point1 (Point): First endpoint of the beam.
            point2 (Point): Second endpoint of the beam.
            Radius (float): Radius of the beam.
            Material (int): Material identifier of the beam.
            Type (int): Type of the beam (0: normal, 1: modified, 2: boundary beam).
        """
        self.point1: 'Point' = point1
        self.point2: 'Point' = point2
        self.radius: float = Radius
        self.material: int = Material
        self.type: int = Type
        self.index: int = None
        self.angle1: Tuple[float, float] = None
        self.angle2: Tuple[float, float] = None
        self.length: float = self.getLength()
        self.modBeam = False

    def __repr__(self) -> str:
        return f"Beam({self.point1}, {self.point2}, Radius:{self.radius}, Type:{self.type}, Index:{self.index})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Beam) and self.point1 == other.point1 and self.point2 == other.point2

    def __hash__(self) -> int:
        return hash((self.point1, self.point2))

    def getLength(self) -> float:
        """
        Calculate the length of the beam.

        Returns:
            float: Length of the beam.
        """
        x1, y1, z1 = self.point1.x, self.point1.y, self.point1.z
        x2, y2, z2 = self.point2.x, self.point2.y, self.point2.z
        length = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), 4)
        return length

    def getVolume(self) -> float:
        """
        Calculate the volume of the beam.

        Returns:
            float: Volume of the beam.
        """
        return math.pi * (self.radius ** 2) * self.length

    def changeBeamType(self, newType: int) -> None:
        """
        Change the type of the beam.

        Args:
            newType (int): New type to assign to the beam.
        """
        self.type = newType

    def getPointOnBeamFromDistance(self, distance: float, pointIndex: int) -> List[float]:
        """
        Calculate the coordinates of a point on the beam at a specific distance from an endpoint.

        Args:
            distance (float): Distance from the specified endpoint.
            pointIndex (int): Index of the endpoint (1 for point1, 2 for point2).

        Returns:
            List[float]: Coordinates [x, y, z] of the calculated point.

        Raises:
            ValueError: If the point index is not 1 or 2.
        """
        beam_length = self.getLength()
        if pointIndex == 1:
            start_point = self.point1
            end_point = self.point2
        elif pointIndex == 2:
            start_point = self.point2
            end_point = self.point1
        else:
            raise ValueError("Point must be 1 or 2.")

        direction_ratios = [
            (end_point.x - start_point.x) / beam_length,
            (end_point.y - start_point.y) / beam_length,
            (end_point.z - start_point.z) / beam_length,
        ]

        factors = [dr * distance for dr in direction_ratios]

        point_mod = [
            start_point.x + factors[0],
            start_point.y + factors[1],
            start_point.z + factors[2]
        ]

        return point_mod

    def isPointOnBeam(self, node: 'Point') -> bool:
        """
        Check if a given node lies on the beam.

        Args:
            node (Point): The point to check.

        Returns:
            bool: True if the node lies on the beam, False otherwise.
        """
        vector1 = (self.point2.x - self.point1.x, self.point2.y - self.point1.y, self.point2.z - self.point1.z)
        vector2 = (node.x - self.point1.x, node.y - self.point1.y, node.z - self.point1.z)

        if (node.x == self.point1.x and node.y == self.point1.y and node.z == self.point1.z) or (
                node.x == self.point2.x and node.y == self.point2.y and node.z == self.point2.z):
            return False
        cross_product = (
            vector1[1] * vector2[2] - vector1[2] * vector2[1],
            vector1[2] * vector2[0] - vector1[0] * vector2[2],
            vector1[0] * vector2[1] - vector1[1] * vector2[0]
        )

        if cross_product == (0, 0, 0):
            dot_product = (vector2[0] * vector1[0] + vector2[1] * vector1[1] + vector2[2] * vector1[2])
            vector1_length_squared = (vector1[0] ** 2 + vector1[1] ** 2 + vector1[2] ** 2)
            return 0 <= dot_product <= vector1_length_squared
        else:
            return False

    def setIndex(self, index: int) -> None:
        """
        Assign an index to the beam.

        Args:
            index (int): Index to assign.
        """
        self.index = index

    def getData(self) -> List[int]:
        """
        Retrieve beam data for exporting.

        Returns:
            List[int]: [beam_index, point1_index, point2_index, beam_type].
        """
        return [self.index, self.point1.index, self.point2.index, self.type]

    def setAngle(self, AngleData: Tuple[float, float, float, float]) -> None:
        """
        Assign angle data to the beam.

        Args:
            AngleData (Tuple[float, float, float, float]): Angle data as (radius1, angle1, radius2, angle2).
        """
        self.angle1 = AngleData[0:2]
        self.angle2 = AngleData[2:4]

    def getLengthMod(self) -> Tuple[float, float]:
        """
        Calculate the modification length for the penalization method.

        Returns:
            Tuple[float, float]: Length modifications for point1 and point2.
        """
        L1 = self.functionPenalizationLzone(self.angle1)
        L2 = self.functionPenalizationLzone(self.angle2)
        return L1, L2

    def functionPenalizationLzone(self, radiusAngleData: Tuple[float, float]) -> float:
        """
        Calculate the penalization length based on radius and angle data.

        Args:
            radiusAngleData (Tuple[float, float]): (radius, angle).

        Returns:
            float: Length of the penalization zone.
        """
        radius, angle = radiusAngleData
        if angle > 170:
            return 0.0000001
        return radius / math.tan(math.radians(angle) / 2)

    def setRadius(self, radius: float) -> None:
        """
        Set the radius of the beam.

        Args:
            radius (float): New radius to assign.
        """
        self.radius = radius

    def setBeamMod(self):
        self.modBeam = True

    def findIntersectionWithMesh(self, meshObject: 'Mesh') -> Tuple[float, float, float] | None:
        """
        Find the intersection point of the beam with a mesh.
        Returns the first intersection point if it exists, None otherwise.
        """
        ray_origin = np.array([self.point1.x, self.point1.y, self.point1.z])
        ray_direction = np.array([self.point2.x - self.point1.x,
                                  self.point2.y - self.point1.y,
                                  self.point2.z - self.point1.z])

        # Normalisation du vecteur directionnel
        norm = np.linalg.norm(ray_direction)
        if norm == 0:
            return None  # Évite les erreurs en cas de direction nulle
        ray_direction /= norm  # Normalisation

        # Création de l'intersecteur de rayons
        intersector = trimesh.ray.ray_pyembree.RayMeshIntersector(meshObject.mesh)

        # Recherche des intersections
        locations, _, _ = intersector.intersects_location(
            ray_origins=[ray_origin],
            ray_directions=[ray_direction]
        )

        if len(locations) > 0:
            return tuple(locations[0])  # Retourne la première intersection trouvée
        return None
