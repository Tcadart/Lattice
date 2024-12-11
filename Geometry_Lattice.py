import math
import random

def Lattice_geometry(LatticeGeometry):
    """
    Get data of point and beam for lattice geometry

    Parameter:
    ------------
    LatticeGeometry: integer
        Type number of lattice geometry
    """
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
    angleGeom = 20  # Angle en degres
    hGeom = 0.35
    valGeom = hGeom - math.tan(angleGeom * math.pi / 180) / 2
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
    Hichem = [(0.0, 0.0, 0.0, 0.5, 0.5, 0.5),
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
    if LatticeGeometry == -1:
        LatticeGeometry = random.randint(0, 10)
    if LatticeGeometry == 0:
        return BCC
    if LatticeGeometry == 1:
        return Octet
    if LatticeGeometry == 2:
        return OctetExt
    if LatticeGeometry == 3:
        return OctetInt
    if LatticeGeometry == 4:
        return BCCZ
    if LatticeGeometry == 5:
        return Cubic
    if LatticeGeometry == 6:
        return OctahedronZ
    if LatticeGeometry == 7:
        return OctahedronZcross
    if LatticeGeometry == 8:
        return Kelvin
    if LatticeGeometry == 9:
        return CubicV2
    if LatticeGeometry == 10:
        return CubicV3
    if LatticeGeometry == 11:
        return CubicV4
    if LatticeGeometry == 12:
        return Newlattice
    if LatticeGeometry == 13:
        return Diamond
    if LatticeGeometry == 14:
        return Auxetic
    if LatticeGeometry == 15:
        return Hichem
    if LatticeGeometry == 16:
        return Hybrid1
    if LatticeGeometry == 17:
        return Hybrid2
    if LatticeGeometry == 18:
        return Hybrid3
    if LatticeGeometry == 19:
        return Hybrid3_plus_bar
    if LatticeGeometry == 1000:
        return BCC + Hybrid1 + Hybrid2

