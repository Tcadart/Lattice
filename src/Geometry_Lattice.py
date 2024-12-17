import math
import random

# Define lattice geometries
angleGeom = 20  # Angle in degrees
hGeom = 0.35
valGeom = hGeom - math.tan(angleGeom * math.pi / 180) / 2

LATTICE_GEOMETRIES = {
    0: "BCC",
    1: "Octet",
    2: "OctetExt",
    3: "OctetInt",
    4: "BCCZ",
    5: "Cubic",
    6: "OctahedronZ",
    7: "OctahedronZcross",
    8: "Kelvin",
    9: "CubicV2",
    10: "CubicV3",
    11: "CubicV4",
    12: "Newlattice",
    13: "Diamond",
    14: "Auxetic",
    15: "HLattice",
    16: "Hybrid1",
    17: "Hybrid2",
    18: "Hybrid3",
    19: "Hybrid3_plus_bar",
}



BCC = [(0.0, 0.0, 0.0, 0.5, 0.5, 0.5),
       (0.5, 0.5, 0.5, 1.0, 1.0, 1.0),
       (0.5, 0.5, 0.5, 1.0, 1.0, 0.0),
       (0.5, 0.5, 0.5, 0.0, 0.0, 1.0),
       (0.5, 0.5, 0.5, 0.0, 1.0, 0.0),
       (0.5, 0.5, 0.5, 0.0, 1.0, 1.0),
       (1.0, 0.0, 1.0, 0.5, 0.5, 0.5),
       (0.5, 0.5, 0.5, 1.0, 0.0, 0.0)]
Octet = [(0.0, 0.0, 0.0, 0.5, 0.0, 0.5),
         (1.0, 0.0, 1.0, 0.5, 0.0, 0.5),
         (0.0, 0.0, 1.0, 0.5, 0.0, 0.5),
         (1.0, 0.0, 0.0, 0.5, 0.0, 0.5),
         (0.0, 0.0, 0.0, 0.0, 0.5, 0.5),
         (0.0, 1.0, 1.0, 0.0, 0.5, 0.5),
         (0.0, 0.0, 1.0, 0.0, 0.5, 0.5),
         (0.0, 1.0, 0.0, 0.0, 0.5, 0.5),
         (0.0, 0.0, 0.0, 0.5, 0.5, 0.0),
         (1.0, 1.0, 0.0, 0.5, 0.5, 0.0),
         (1.0, 0.0, 0.0, 0.5, 0.5, 0.0),
         (0.0, 1.0, 0.0, 0.5, 0.5, 0.0),
         (0.0, 0.0, 1.0, 0.5, 0.5, 1.0),
         (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
         (1.0, 0.0, 1.0, 0.5, 0.5, 1.0),
         (0.0, 1.0, 1.0, 0.5, 0.5, 1.0),
         (1.0, 0.5, 0.5, 1.0, 1.0, 1.0),
         (1.0, 0.0, 0.0, 1.0, 0.5, 0.5),
         (1.0, 0.5, 0.5, 1.0, 1.0, 0.0),
         (1.0, 0.0, 1.0, 1.0, 0.5, 0.5),
         (0.5, 1.0, 0.5, 1.0, 1.0, 1.0),
         (0.0, 1.0, 0.0, 0.5, 1.0, 0.5),
         (0.5, 1.0, 0.5, 1.0, 1.0, 0.0),
         (0.0, 1.0, 1.0, 0.5, 1.0, 0.5),
         (0.5, 0.0, 0.5, 0.5, 0.5, 0.0),
         (0.5, 0.0, 0.5, 0.0, 0.5, 0.5),
         (0.5, 0.0, 0.5, 1.0, 0.5, 0.5),
         (0.5, 0.0, 0.5, 0.5, 0.5, 1.0),
         (0.5, 1.0, 0.5, 0.5, 0.5, 0.0),
         (0.5, 1.0, 0.5, 0.0, 0.5, 0.5),
         (0.5, 1.0, 0.5, 1.0, 0.5, 0.5),
         (0.5, 1.0, 0.5, 0.5, 0.5, 1.0),
         (1.0, 0.5, 0.5, 0.5, 0.5, 0.0),
         (0.5, 0.5, 0.0, 0.0, 0.5, 0.5),
         (0.5, 0.5, 1.0, 0.0, 0.5, 0.5),
         (0.5, 0.5, 1.0, 1.0, 0.5, 0.5)]
OctetExt = [(0.0, 0.0, 0.0, 0.5, 0.0, 0.5),
            (1.0, 0.0, 1.0, 0.5, 0.0, 0.5),
            (0.0, 0.0, 1.0, 0.5, 0.0, 0.5),
            (1.0, 0.0, 0.0, 0.5, 0.0, 0.5),
            (0.0, 0.0, 0.0, 0.0, 0.5, 0.5),
            (0.0, 1.0, 1.0, 0.0, 0.5, 0.5),
            (0.0, 0.0, 1.0, 0.0, 0.5, 0.5),
            (0.0, 1.0, 0.0, 0.0, 0.5, 0.5),
            (0.0, 0.0, 0.0, 0.5, 0.5, 0.0),
            (1.0, 1.0, 0.0, 0.5, 0.5, 0.0),
            (1.0, 0.0, 0.0, 0.5, 0.5, 0.0),
            (0.0, 1.0, 0.0, 0.5, 0.5, 0.0),
            (0.0, 0.0, 1.0, 0.5, 0.5, 1.0),
            (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
            (1.0, 0.0, 1.0, 0.5, 0.5, 1.0),
            (0.0, 1.0, 1.0, 0.5, 0.5, 1.0),
            (1.0, 0.5, 0.5, 1.0, 1.0, 1.0),
            (1.0, 0.0, 0.0, 1.0, 0.5, 0.5),
            (1.0, 0.5, 0.5, 1.0, 1.0, 0.0),
            (1.0, 0.0, 1.0, 1.0, 0.5, 0.5),
            (0.5, 1.0, 0.5, 1.0, 1.0, 1.0),
            (0.0, 1.0, 0.0, 0.5, 1.0, 0.5),
            (0.5, 1.0, 0.5, 1.0, 1.0, 0.0),
            (0.0, 1.0, 1.0, 0.5, 1.0, 0.5)]
OctetInt = [(0.5, 0.0, 0.5, 0.5, 0.5, 0.0),
            (0.5, 0.0, 0.5, 0.0, 0.5, 0.5),
            (0.5, 0.0, 0.5, 1.0, 0.5, 0.5),
            (0.5, 0.0, 0.5, 0.5, 0.5, 1.0),
            (0.5, 1.0, 0.5, 0.5, 0.5, 0.0),
            (0.5, 1.0, 0.5, 0.0, 0.5, 0.5),
            (0.5, 1.0, 0.5, 1.0, 0.5, 0.5),
            (0.5, 1.0, 0.5, 0.5, 0.5, 1.0),
            (1.0, 0.5, 0.5, 0.5, 0.5, 0.0),
            (0.5, 0.5, 0.0, 0.0, 0.5, 0.5),
            (0.5, 0.5, 1.0, 0.0, 0.5, 0.5),
            (0.5, 0.5, 1.0, 1.0, 0.5, 0.5)]
BCCZ = [(0.5, 0.5, 0.5, 1.0, 1.0, 1.0),
        (0.0, 0.0, 0.0, 0.5, 0.5, 0.5),
        (0.5, 0.5, 0.5, 1.0, 1.0, 0.0),
        (0.0, 0.0, 1.0, 0.5, 0.5, 0.5),
        (0.5, 0.5, 0.5, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.0, 0.5, 0.5, 0.5),
        (0.5, 0.5, 0.5, 0.0, 1.0, 1.0),
        (1.0, 0.0, 0.0, 0.5, 0.5, 0.5),
        (0.5, 0.5, 0.0, 0.5, 0.5, 0.5),
        (0.5, 0.5, 0.5, 0.5, 0.5, 1.0)]
Cubic = [(0.0, 0.0, 0.0, 0.0, 0.0, 1.0),
         (1.0, 0.0, 0.0, 1.0, 0.0, 1.0),
         (0.0, 1.0, 0.0, 0.0, 1.0, 1.0),
         (1.0, 1.0, 0.0, 1.0, 1.0, 1.0),
         (0.0, 0.0, 0.0, 1.0, 0.0, 0.0),
         (0.0, 0.0, 0.0, 0.0, 1.0, 0.0),
         (1.0, 1.0, 0.0, 0.0, 1.0, 0.0),
         (1.0, 1.0, 0.0, 1.0, 0.0, 0.0),
         (0.0, 0.0, 1.0, 1.0, 0.0, 1.0),
         (0.0, 0.0, 1.0, 0.0, 1.0, 1.0),
         (1.0, 1.0, 1.0, 0.0, 1.0, 1.0),
         (1.0, 1.0, 1.0, 1.0, 0.0, 1.0)]
OctahedronZ = [(0.5, 0.0, 0.5, 0.5, 0.5, 0.0),
               (0.5, 0.0, 0.5, 0.0, 0.5, 0.5),
               (0.5, 0.0, 0.5, 1.0, 0.5, 0.5),
               (0.5, 0.0, 0.5, 0.5, 0.5, 1.0),
               (0.5, 1.0, 0.5, 0.5, 0.5, 0.0),
               (0.5, 1.0, 0.5, 0.0, 0.5, 0.5),
               (0.5, 1.0, 0.5, 1.0, 0.5, 0.5),
               (0.5, 1.0, 0.5, 0.5, 0.5, 1.0),
               (1.0, 0.5, 0.5, 0.5, 0.5, 0.0),
               (0.5, 0.5, 0.0, 0.0, 0.5, 0.5),
               (0.5, 0.5, 1.0, 0.0, 0.5, 0.5),
               (0.5, 0.5, 1.0, 1.0, 0.5, 0.5),
               (0.5, 0.5, 0.0, 0.5, 0.5, 1.0)]
OctahedronZcross = [(0.5, 0.0, 0.5, 0.5, 0.5, 0.0),
                    (0.5, 0.0, 0.5, 0.0, 0.5, 0.5),
                    (0.5, 0.0, 0.5, 1.0, 0.5, 0.5),
                    (0.5, 0.0, 0.5, 0.5, 0.5, 1.0),
                    (0.5, 1.0, 0.5, 0.5, 0.5, 0.0),
                    (0.5, 1.0, 0.5, 0.0, 0.5, 0.5),
                    (0.5, 1.0, 0.5, 1.0, 0.5, 0.5),
                    (0.5, 1.0, 0.5, 0.5, 0.5, 1.0),
                    (1.0, 0.5, 0.5, 0.5, 0.5, 0.0),
                    (0.5, 0.5, 0.0, 0.0, 0.5, 0.5),
                    (0.5, 0.5, 1.0, 0.0, 0.5, 0.5),
                    (0.5, 0.5, 1.0, 1.0, 0.5, 0.5),
                    (0.5, 0.5, 0.0, 0.5, 0.5, 0.5),
                    (0.5, 0.5, 1.0, 0.5, 0.5, 0.5),
                    (0.5, 0.0, 0.5, 0.5, 0.5, 0.5),
                    (0.0, 0.5, 0.5, 0.5, 0.5, 0.5),
                    (1.0, 0.5, 0.5, 0.5, 0.5, 0.5),
                    (0.5, 1.0, 0.5, 0.5, 0.5, 0.5)]
Kelvin = [(0.5, 0.25, 0, 0.25, 0.5, 0),
          (0.5, 0.25, 0, 0.75, 0.5, 0),
          (0.5, 0.75, 0, 0.25, 0.5, 0),
          (0.5, 0.75, 0, 0.75, 0.5, 0),
          (0.5, 0.25, 1, 0.25, 0.5, 1),
          (0.5, 0.25, 1, 0.75, 0.5, 1),
          (0.5, 0.75, 1, 0.25, 0.5, 1),
          (0.5, 0.75, 1, 0.75, 0.5, 1),
          (0.5, 0, 0.25, 0.25, 0, 0.5),
          (0.5, 0, 0.25, 0.75, 0, 0.5),
          (0.5, 0, 0.75, 0.25, 0, 0.5),
          (0.5, 0, 0.75, 0.75, 0, 0.5),
          (0.5, 1, 0.25, 0.25, 1, 0.5),
          (0.5, 1, 0.25, 0.75, 1, 0.5),
          (0.5, 1, 0.75, 0.25, 1, 0.5),
          (0.5, 1, 0.75, 0.75, 1, 0.5),
          (0, 0.5, 0.25, 0, 0.25, 0.5),
          (0, 0.5, 0.25, 0, 0.75, 0.5),
          (0, 0.5, 0.75, 0, 0.25, 0.5),
          (0, 0.5, 0.75, 0, 0.75, 0.5),
          (1, 0.5, 0.25, 1, 0.25, 0.5),
          (1, 0.5, 0.25, 1, 0.75, 0.5),
          (1, 0.5, 0.75, 1, 0.25, 0.5),
          (1, 0.5, 0.75, 1, 0.75, 0.5),
          (0.5, 0.25, 0, 0.5, 0, 0.25),
          (0.25, 0.5, 0, 0, 0.5, 0.25),
          (0.75, 0.5, 0, 1, 0.5, 0.25),
          (0.5, 0.75, 0, 0.5, 1, 0.25),
          (0.25, 0, 0.5, 0, 0.25, 0.5),
          (0.75, 0, 0.5, 1, 0.25, 0.5),
          (0.75, 1, 0.5, 1, 0.75, 0.5),
          (0.25, 1, 0.5, 0, 0.75, 0.5),
          (0.5, 0, 0.75, 0.5, 0.25, 1),
          (0, 0.5, 0.75, 0.25, 0.5, 1),
          (0.5, 1, 0.75, 0.5, 0.75, 1),
          (1, 0.5, 0.75, 0.75, 0.5, 1)]
CubicV2 = [(0.5, 0.0, 0.5, 0.5, 0.5, 0.5),
           (0.0, 0.5, 0.5, 0.5, 0.5, 0.5),
           (0.5, 1.0, 0.5, 0.5, 0.5, 0.5),
           (1.0, 0.5, 0.5, 0.5, 0.5, 0.5),
           (0.5, 0.5, 0.0, 0.5, 0.5, 0.5),
           (0.5, 0.5, 1.0, 0.5, 0.5, 0.5)]
CubicV3 = [(0.0, 0.0, 0.0, 0.5, 0.0, 0.0),
           (0.5, 0.0, 0.0, 1.0, 0.0, 0.0),
           (0.0, 1.0, 0.0, 0.5, 1.0, 0.0),
           (0.5, 1.0, 0.0, 1.0, 1.0, 0.0),
           (0.5, 0.0, 0.0, 0.5, 1.0, 0.0),
           (0.0, 0.0, 1.0, 0.5, 0.0, 1.0),
           (0.5, 0.0, 1.0, 1.0, 0.0, 1.0),
           (0.0, 1.0, 1.0, 0.5, 1.0, 1.0),
           (0.5, 1.0, 1.0, 1.0, 1.0, 1.0),
           (0.5, 0.0, 1.0, 0.5, 1.0, 1.0),
           (0.5, 0.0, 0.0, 0.5, 0.0, 1.0),
           (0.5, 1.0, 0.0, 0.5, 1.0, 1.0)]
CubicV4 = [(0.5, 0.0, 0.0, 0.5, 0.5, 0.0),
           (0.0, 0.5, 0.0, 0.5, 0.5, 0.0),
           (0.5, 1.0, 0.0, 0.5, 0.5, 0.0),
           (1.0, 0.5, 0.0, 0.5, 0.5, 0.0),
           (0.5, 0.0, 1.0, 0.5, 0.5, 1.0),
           (0.0, 0.5, 1.0, 0.5, 0.5, 1.0),
           (0.5, 1.0, 1.0, 0.5, 0.5, 1.0),
           (1.0, 0.5, 1.0, 0.5, 0.5, 1.0),
           (0.5, 0.5, 0.0, 0.5, 0.5, 1.0)]
Newlattice = [
    (0.0, 0.0, 0.0, 0.25, 0.25, 0.25),
    (0.25, 0.25, 0.25, 0.5, 0.0, 0.0),
    (0.25, 0.25, 0.25, 0.0, 0.0, 0.5),
    (0.25, 0.25, 0.25, 0.0, 0.5, 0.0),
    (1.0, 0.0, 0.0, 0.75, 0.25, 0.25),
    (0.75, 0.25, 0.25, 0.5, 0.0, 0.0),
    (0.75, 0.25, 0.25, 1.0, 0.5, 0.0),
    (0.75, 0.25, 0.25, 1.0, 0.0, 0.5),
    (0.0, 1.0, 0.0, 0.25, 0.75, 0.25),
    (0.25, 0.75, 0.25, 0.0, 0.5, 0.0),
    (0.25, 0.75, 0.25, 0.5, 1.0, 0.0),
    (0.25, 0.75, 0.25, 0.0, 1.0, 0.5),
    (1.0, 1.0, 0.0, 0.75, 0.75, 0.25),
    (0.75, 0.75, 0.25, 1.0, 0.5, 0.0),
    (0.75, 0.75, 0.25, 0.5, 1.0, 0.0),
    (0.75, 0.75, 0.25, 1.0, 1.0, 0.5),
    (0.0, 0.0, 1.0, 0.25, 0.25, 0.75),
    (0.25, 0.25, 0.75, 0.0, 0.5, 1.0),
    (0.25, 0.25, 0.75, 0.5, 0.0, 1.0),
    (0.25, 0.25, 0.75, 0.0, 0.0, 0.5),
    (1.0, 0.0, 1.0, 0.75, 0.25, 0.75),
    (0.75, 0.25, 0.75, 1.0, 0.0, 0.5),
    (0.75, 0.25, 0.75, 0.5, 0.0, 1.0),
    (0.75, 0.25, 0.75, 1.0, 0.5, 1.0),
    (0.0, 1.0, 1.0, 0.25, 0.75, 0.75),
    (0.25, 0.75, 0.75, 0.0, 1.0, 0.5),
    (0.25, 0.75, 0.75, 0.5, 1.0, 1.0),
    (0.25, 0.75, 0.75, 0.0, 0.5, 1.0),
    (1.0, 1.0, 1.0, 0.75, 0.75, 0.75),
    (0.75, 0.75, 0.75, 1.0, 1.0, 0.5),
    (0.75, 0.75, 0.75, 0.5, 1.0, 1.0),
    (0.75, 0.75, 0.75, 1.0, 0.5, 1.0)
]
Diamond = [
    (0.0, 0.0, 0.0, 0.25, 0.25, 0.25),
    (0.25, 0.25, 0.25, 0.5, 0.5, 0.0),
    (0.25, 0.25, 0.25, 0.0, 0.5, 0.5),
    (0.25, 0.25, 0.25, 0.5, 0.0, 0.5),
    (1.0, 0.0, 0.0, 0.75, 0.25, 0.25),
    (0.75, 0.25, 0.25, 0.5, 0.5, 0.0),
    (0.75, 0.25, 0.25, 1.0, 0.5, 0.5),
    (0.75, 0.25, 0.25, 0.5, 0.0, 0.5),
    (1.0, 1.0, 0.0, 0.75, 0.75, 0.25),
    (0.75, 0.75, 0.25, 0.5, 0.5, 0.0),
    (0.75, 0.75, 0.25, 1.0, 0.5, 0.5),
    (0.75, 0.75, 0.25, 0.5, 1.0, 0.5),
    (0.0, 1.0, 0.0, 0.25, 0.75, 0.25),
    (0.25, 0.75, 0.25, 0.5, 0.5, 0.0),
    (0.25, 0.75, 0.25, 0.0, 0.5, 0.5),
    (0.25, 0.75, 0.25, 0.5, 1.0, 0.5),
    (0.0, 0.0, 1.0, 0.25, 0.25, 0.75),
    (0.25, 0.25, 0.75, 0.5, 0.5, 1.0),
    (0.25, 0.25, 0.75, 0.0, 0.5, 0.5),
    (0.25, 0.25, 0.75, 0.5, 0.0, 0.5),
    (1.0, 0.0, 1.0, 0.75, 0.25, 0.75),
    (0.75, 0.25, 0.75, 0.5, 0.5, 1.0),
    (0.75, 0.25, 0.75, 1.0, 0.5, 0.5),
    (0.75, 0.25, 0.75, 0.5, 0.0, 0.5),
    (1.0, 1.0, 1.0, 0.75, 0.75, 0.75),
    (0.75, 0.75, 0.75, 0.5, 0.5, 1.0),
    (0.75, 0.75, 0.75, 1.0, 0.5, 0.5),
    (0.75, 0.75, 0.75, 0.5, 1.0, 0.5),
    (0.0, 1.0, 1.0, 0.25, 0.75, 0.75),
    (0.25, 0.75, 0.75, 0.5, 0.5, 1.0),
    (0.25, 0.75, 0.75, 0.0, 0.5, 0.5),
    (0.25, 0.75, 0.75, 0.5, 1.0, 0.5)
]
Auxetic = [(0.5, 0.0, 0.0, 0.5, 0.0, hGeom),
           (0.5, 0.0, 1.0, 0.5, 0.0, 1 - hGeom),
           (0.0, 0.0, valGeom, 0.0, 0.0, 1 - valGeom),
           (1.0, 0.0, valGeom, 1.0, 0.0, 1 - valGeom),
           (0.0, 0.0, valGeom, 0.5, 0.0, hGeom),
           (0.0, 0.0, 1 - valGeom, 0.5, 0.0, 1 - hGeom),
           (1.0, 0.0, 1 - valGeom, 0.5, 0.0, 1 - hGeom),
           (1.0, 0.0, valGeom, 0.5, 0.0, hGeom),
           (0.5, 1.0, 0.0, 0.5, 1.0, hGeom),
           (0.5, 1.0, 1.0, 0.5, 1.0, 1 - hGeom),
           (0.0, 1.0, valGeom, 0.0, 1.0, 1 - valGeom),
           (1.0, 1.0, valGeom, 1.0, 1.0, 1 - valGeom),
           (0.0, 1.0, valGeom, 0.5, 1.0, hGeom),
           (0.0, 1.0, 1 - valGeom, 0.5, 1.0, 1 - hGeom),
           (1.0, 1.0, 1 - valGeom, 0.5, 1.0, 1 - hGeom),
           (1.0, 1.0, valGeom, 0.5, 1.0, hGeom),
           (1.0, 0.0, valGeom, 1.0, 0.5, hGeom),
           (1.0, 1.0, valGeom, 1.0, 0.5, hGeom),
           (1.0, 0.5, 0.0, 1.0, 0.5, hGeom),
           (1.0, 0.5, 1 - hGeom, 1.0, 1.0, 1 - valGeom),
           (1.0, 0.5, 1 - hGeom, 1.0, 0.0, 1 - valGeom),
           (1.0, 0.5, 1 - hGeom, 1.0, 0.5, 1.0),
           (0.0, 0.0, valGeom, 0.0, 0.5, hGeom),
           (0.0, 1.0, valGeom, 0.0, 0.5, hGeom),
           (0.0, 0.5, 0.0, 0.0, 0.5, hGeom),
           (0.0, 0.5, 1 - hGeom, 0.0, 1.0, 1 - valGeom),
           (0.0, 0.5, 1 - hGeom, 0.0, 0.0, 1 - valGeom),
           (0.0, 0.5, 1 - hGeom, 0.0, 0.5, 1.0)]
HLattice = [(0.0, 0.0, 0.0, 0.5, 0.5, 0.5),
          (0.5, 0.5, 0.5, 1.0, 1.0, 1.0),
          (0.5, 0.5, 0.5, 1.0, 1.0, 0.0),
          (0.5, 0.5, 0.5, 0.0, 0.0, 1.0),
          (0.5, 0.5, 0.5, 0.0, 1.0, 0.0),
          (0.5, 0.5, 0.5, 0.0, 1.0, 1.0),
          (1.0, 0.0, 1.0, 0.5, 0.5, 0.5),
          (0.5, 0.5, 0.5, 1.0, 0.0, 0.0),
          (0.0, 0.0, 0.0, 0.5, 0.0, 0.5),
          (0.5, 0.0, 0.0, 0.5, 0.0, 0.5),
          (1.0, 0.0, 0.0, 0.5, 0.0, 0.5),
          (1.0, 0.0, 0.5, 0.5, 0.0, 0.5),
          (1.0, 0.0, 1.0, 0.5, 0.0, 0.5),
          (0.5, 0.0, 1.0, 0.5, 0.0, 0.5),
          (0.0, 0.0, 1.0, 0.5, 0.0, 0.5),
          (0.0, 0.0, 0.5, 0.5, 0.0, 0.5),
          (0.0, 1.0, 0.0, 0.5, 1.0, 0.5),
          (0.5, 1.0, 0.0, 0.5, 1.0, 0.5),
          (1.0, 1.0, 0.0, 0.5, 1.0, 0.5),
          (1.0, 1.0, 0.5, 0.5, 1.0, 0.5),
          (1.0, 1.0, 1.0, 0.5, 1.0, 0.5),
          (0.5, 1.0, 1.0, 0.5, 1.0, 0.5),
          (0.0, 1.0, 1.0, 0.5, 1.0, 0.5),
          (0.0, 1.0, 0.5, 0.5, 1.0, 0.5),
          (1.0, 0.0, 0.0, 1.0, 0.5, 0.5),
          (1.0, 0.5, 0.0, 1.0, 0.5, 0.5),
          (1.0, 1.0, 0.0, 1.0, 0.5, 0.5),
          (1.0, 1.0, 0.5, 1.0, 0.5, 0.5),
          (1.0, 1.0, 1.0, 1.0, 0.5, 0.5),
          (1.0, 0.5, 1.0, 1.0, 0.5, 0.5),
          (1.0, 0.0, 1.0, 1.0, 0.5, 0.5),
          (1.0, 0.0, 0.5, 1.0, 0.5, 0.5),
          (0.0, 0.0, 0.0, 0.0, 0.5, 0.5),
          (0.0, 0.5, 0.0, 0.0, 0.5, 0.5),
          (0.0, 1.0, 0.0, 0.0, 0.5, 0.5),
          (0.0, 1.0, 0.5, 0.0, 0.5, 0.5),
          (0.0, 1.0, 1.0, 0.0, 0.5, 0.5),
          (0.0, 0.5, 1.0, 0.0, 0.5, 0.5),
          (0.0, 0.0, 1.0, 0.0, 0.5, 0.5),
          (0.0, 0.0, 0.5, 0.0, 0.5, 0.5),
          (0.0, 0.0, 0.0, 0.5, 0.5, 0.0),
          (0.5, 0.0, 0.0, 0.5, 0.5, 0.0),
          (1.0, 0.0, 0.0, 0.5, 0.5, 0.0),
          (1.0, 0.5, 0.0, 0.5, 0.5, 0.0),
          (1.0, 1.0, 0.0, 0.5, 0.5, 0.0),
          (0.5, 1.0, 0.0, 0.5, 0.5, 0.0),
          (0.0, 1.0, 0.0, 0.5, 0.5, 0.0),
          (0.0, 0.5, 0.0, 0.5, 0.5, 0.0),
          (0.0, 0.0, 1.0, 0.5, 0.5, 1.0),
          (0.5, 0.0, 1.0, 0.5, 0.5, 1.0),
          (1.0, 0.0, 1.0, 0.5, 0.5, 1.0),
          (1.0, 0.5, 1.0, 0.5, 0.5, 1.0),
          (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
          (0.5, 1.0, 1.0, 0.5, 0.5, 1.0),
          (0.0, 1.0, 1.0, 0.5, 0.5, 1.0),
          (0.0, 0.5, 1.0, 0.5, 0.5, 1.0)
          ]
Hybrid1 = [
    (0.25, 0.25, 0.25, 0.5, 0.0, 0.0),
    (0.25, 0.25, 0.25, 0.0, 0.0, 0.5),
    (0.25, 0.25, 0.25, 0.0, 0.5, 0.0),
    (0.75, 0.25, 0.25, 0.5, 0.0, 0.0),
    (0.75, 0.25, 0.25, 1.0, 0.5, 0.0),
    (0.75, 0.25, 0.25, 1.0, 0.0, 0.5),
    (0.25, 0.75, 0.25, 0.0, 0.5, 0.0),
    (0.25, 0.75, 0.25, 0.5, 1.0, 0.0),
    (0.25, 0.75, 0.25, 0.0, 1.0, 0.5),
    (0.75, 0.75, 0.25, 1.0, 0.5, 0.0),
    (0.75, 0.75, 0.25, 0.5, 1.0, 0.0),
    (0.75, 0.75, 0.25, 1.0, 1.0, 0.5),
    (0.25, 0.25, 0.75, 0.0, 0.5, 1.0),
    (0.25, 0.25, 0.75, 0.5, 0.0, 1.0),
    (0.25, 0.25, 0.75, 0.0, 0.0, 0.5),
    (0.75, 0.25, 0.75, 1.0, 0.0, 0.5),
    (0.75, 0.25, 0.75, 0.5, 0.0, 1.0),
    (0.75, 0.25, 0.75, 1.0, 0.5, 1.0),
    (0.25, 0.75, 0.75, 0.0, 1.0, 0.5),
    (0.25, 0.75, 0.75, 0.5, 1.0, 1.0),
    (0.25, 0.75, 0.75, 0.0, 0.5, 1.0),
    (0.75, 0.75, 0.75, 1.0, 1.0, 0.5),
    (0.75, 0.75, 0.75, 0.5, 1.0, 1.0),
    (0.75, 0.75, 0.75, 1.0, 0.5, 1.0)
]
Hybrid2 = [
    (0.5, 0.0, 0.0, 0.5, 0.5, 0.5),
    (1.0, 0.0, 0.5, 0.5, 0.5, 0.5),
    (0.5, 0.0, 1.0, 0.5, 0.5, 0.5),
    (0.0, 0.0, 0.5, 0.5, 0.5, 0.5),
    (0.5, 1.0, 0.0, 0.5, 0.5, 0.5),
    (1.0, 1.0, 0.5, 0.5, 0.5, 0.5),
    (0.5, 1.0, 1.0, 0.5, 0.5, 0.5),
    (0.0, 1.0, 0.5, 0.5, 0.5, 0.5),
    (0.0, 0.5, 0.0, 0.5, 0.5, 0.5),
    (0.0, 0.5, 1.0, 0.5, 0.5, 0.5),
    (1.0, 0.5, 0.0, 0.5, 0.5, 0.5),
    (1.0, 0.5, 1.0, 0.5, 0.5, 0.5)
]
Hybrid3 = [
    (0.25, 0.25, 0.25, 0.5, 0.0, 0.5),
    (0.75, 0.25, 0.25, 0.5, 0.0, 0.5),
    (0.25, 0.25, 0.75, 0.5, 0.0, 0.5),
    (0.75, 0.25, 0.75, 0.5, 0.0, 0.5),
    (0.25, 0.75, 0.25, 0.5, 1.0, 0.5),
    (0.75, 0.75, 0.25, 0.5, 1.0, 0.5),
    (0.25, 0.75, 0.75, 0.5, 1.0, 0.5),
    (0.75, 0.75, 0.75, 0.5, 1.0, 0.5),
    (0.25, 0.25, 0.25, 0.0, 0.5, 0.5),
    (0.25, 0.75, 0.25, 0.0, 0.5, 0.5),
    (0.25, 0.75, 0.75, 0.0, 0.5, 0.5),
    (0.25, 0.25, 0.75, 0.0, 0.5, 0.5),
    (0.75, 0.25, 0.25, 1.0, 0.5, 0.5),
    (0.75, 0.75, 0.25, 1.0, 0.5, 0.5),
    (0.75, 0.75, 0.75, 1.0, 0.5, 0.5),
    (0.75, 0.25, 0.75, 1.0, 0.5, 0.5),
    (0.25, 0.25, 0.75, 0.5, 0.5, 1.0),
    (0.75, 0.75, 0.75, 0.5, 0.5, 1.0),
    (0.25, 0.75, 0.75, 0.5, 0.5, 1.0),
    (0.75, 0.25, 0.75, 0.5, 0.5, 1.0),
    (0.25, 0.25, 0.25, 0.5, 0.5, 0.0),
    (0.75, 0.75, 0.25, 0.5, 0.5, 0.0),
    (0.25, 0.75, 0.25, 0.5, 0.5, 0.0),
    (0.75, 0.25, 0.25, 0.5, 0.5, 0.0),
]
Hybrid3_plus_bar = [
    (0.25, 0.25, 0.25, 0.5, 0.0, 0.5),
    (0.75, 0.25, 0.25, 0.5, 0.0, 0.5),
    (0.25, 0.25, 0.75, 0.5, 0.0, 0.5),
    (0.75, 0.25, 0.75, 0.5, 0.0, 0.5),
    (0.25, 0.75, 0.25, 0.5, 1.0, 0.5),
    (0.75, 0.75, 0.25, 0.5, 1.0, 0.5),
    (0.25, 0.75, 0.75, 0.5, 1.0, 0.5),
    (0.75, 0.75, 0.75, 0.5, 1.0, 0.5),
    (0.25, 0.25, 0.25, 0.0, 0.5, 0.5),
    (0.25, 0.75, 0.25, 0.0, 0.5, 0.5),
    (0.25, 0.75, 0.75, 0.0, 0.5, 0.5),
    (0.25, 0.25, 0.75, 0.0, 0.5, 0.5),
    (0.75, 0.25, 0.25, 1.0, 0.5, 0.5),
    (0.75, 0.75, 0.25, 1.0, 0.5, 0.5),
    (0.75, 0.75, 0.75, 1.0, 0.5, 0.5),
    (0.75, 0.25, 0.75, 1.0, 0.5, 0.5),
    (0.25, 0.25, 0.75, 0.5, 0.5, 1.0),
    (0.75, 0.75, 0.75, 0.5, 0.5, 1.0),
    (0.25, 0.75, 0.75, 0.5, 0.5, 1.0),
    (0.75, 0.25, 0.75, 0.5, 0.5, 1.0),
    (0.25, 0.25, 0.25, 0.5, 0.5, 0.0),
    (0.75, 0.75, 0.25, 0.5, 0.5, 0.0),
    (0.25, 0.75, 0.25, 0.5, 0.5, 0.0),
    (0.75, 0.25, 0.25, 0.5, 0.5, 0.0),

    (0.5, 0.0, 0.5, 0.5, 0.5, 0.5),
    (0.5, 1.0, 0.5, 0.5, 0.5, 0.5),
    (0.0, 0.5, 0.5, 0.5, 0.5, 0.5),
    (1.0, 0.5, 0.5, 0.5, 0.5, 0.5),
    (0.5, 0.5, 1.0, 0.5, 0.5, 0.5),
    (0.5, 0.5, 0.0, 0.5, 0.5, 0.5),
]

# Map names to actual geometry data
GEOMETRY_DATA = {
    "BCC": BCC,
    "Octet": Octet,
    "OctetExt": OctetExt,
    "OctetInt": OctetInt,
    "BCCZ": BCCZ,
    "Cubic": Cubic,
    "OctahedronZ": OctahedronZ,
    "OctahedronZcross": OctahedronZcross,
    "Kelvin": Kelvin,
    "CubicV2": CubicV2,
    "CubicV3": CubicV3,
    "CubicV4": CubicV4,
    "Newlattice": Newlattice,
    "Diamond": Diamond,
    "Auxetic": Auxetic,
    "HLattice": HLattice,
    "Hybrid1": Hybrid1,
    "Hybrid2": Hybrid2,
    "Hybrid3": Hybrid3,
    "Hybrid3_plus_bar": Hybrid3_plus_bar
}



def Lattice_geometry(LatticeGeometry):
    """
    Get data of points and beams for lattice geometry.

    Parameters:
    -----------
    LatticeGeometry: int
        Type number of lattice geometry
    """
    if LatticeGeometry == -1:
        LatticeGeometry = random.choice(list(LATTICE_GEOMETRIES.keys()))
    geometry_name = LATTICE_GEOMETRIES.get(LatticeGeometry, "BCC")
    return GEOMETRY_DATA[geometry_name]

