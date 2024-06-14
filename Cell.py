"""
Class Cell
"""
from array import array
from typing import List

from Point import *
from Beam import *
import math
import random


def Lattice_geometry(LatticeGeometry: int):
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
    if LatticeGeometry == 1000:
        return np.concatenate((BCC, Hybrid1, Hybrid2))


class Cell:
    """
    Define Cell data for lattice structure
    """

    def __init__(self, posCell: list, initialCellSize: list, startCellPos: list, latticeType: int,
                 Radius: float, gradRadius, gradDim, gradMat):
        """
        Initialize a Cell with its dimensions and position

        Parameters:
        -----------
        cell_size_x: x-dimension of the cell
        cell_size_y: y-dimension of the cell
        cell_size_z: z-dimension of the cell
        x: x-coordinate of the cell center
        y: y-coordinate of the cell center
        z: z-coordinate of the cell center
        """
        self.centerPoint = None
        self._beamMaterial = None
        self._beamRadius = None
        self.cellSize = None
        self.posCell = posCell
        self.beams = []
        self.index = None

        self.getBeamMaterial(gradMat)
        self.getBeamRadius(gradRadius, Radius)
        self.getCellSize(initialCellSize, gradDim)
        self.generateBeamsInCell(latticeType, startCellPos)
        self.getCellCenter(initialCellSize)

    def generateBeamsInCell(self, latticeType: int, startCellPos: list, beamType: int = 0):
        """
        Generate beams and nodes using a given lattice type and parameters.

        :param latticeType: Type of lattice geometry
        :param startCellPos: array of position of the start of the cell
        :param beamType: optional type of the beam to create
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
        gradMat:
        posCell:

        Returns:
        ---------
        materialType: int
            Material index of the beam
        """
        self._beamMaterial = gradMat[self.posCell[2]][self.posCell[1]][self.posCell[0]]

    def getBeamRadius(self, gradRadius, BaseRadius: float):
        """
        Calculate and return the beam radius

        Parameters:
        -----------
        gradRadius:
        posCell:
        BaseRadius: float

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

    def getCellCenter(self, initialCellSize):
        """
        Calculate the center point of the cell
        """
        self.centerPoint = [initialCellSize[i] + self.cellSize[i] / 2 for i in range(3)]

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
        try:
            self.beams.remove(beamToDelete)
        except ValueError:
            print("Beam not found in the list")

    def addBeam(self, beamToAdd):
        """
        Adding beam to cell
        """
        self.beams.append(beamToAdd)

    def random_coordinate(self, coord, mu, sigma):
        """
        Randomize coordinate of a node with a gaussian noise of parameter mu and sigma
        """
        mod_coord = []
        for pos in coord:
            # mod_coord.append(pos + random.uniform(0, 0.5) - 0.25)
            mod_coord.append(pos + random.gauss(mu, sigma))
        return mod_coord

    def add_point(self, point):
        x, y, z = map(float, point)
        point_obj = Point((x) * self.cellSizeX + self.x, (y) * self.cellSizeY + self.y,
                          (z) * self.cellSizeZ + self.z)
        self.nodes.append(point_obj)

    def generate_beams_random(self, Radius, gradRadius, gradDim, gradMat, posCell):
        self.beams = []
        self.nodes = []
        # Corner node
        corner_node = random.randint(0, 1)
        if corner_node == 1:  # Corner nodes
            map_corner = [(0.0, 0.0, 0.0),
                          (1.0, 1.0, 1.0),
                          (1.0, 1.0, 0.0),
                          (0.0, 0.0, 1.0),
                          (0.0, 1.0, 0.0),
                          (0.0, 1.0, 1.0),
                          (1.0, 0.0, 1.0),
                          (1.0, 0.0, 0.0)]
            for idx, point_corner in enumerate(map_corner):
                self.add_point(point_corner)
        # Edge
        map_edge = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
        for i in range(3):  # 3 direction of edge node
            Edge_node = random.randint(0, 1)
            if Edge_node == 1:
                point_mod = 0.5 + random.uniform(0, 0.5) - 0.25
                for idx, point_edge in enumerate(map_edge):
                    point = list(point_edge)
                    point.insert(i, point_mod)
                    self.add_point(point)
        # Face
        map_face = [(0.25, 0.25), (0.75, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.75)]
        for i in range(3):  # 3 direction of face node
            Face_node = [random.randint(0, 1) for _ in range(5)]
            for idx, point_face in enumerate(map_face):
                if Face_node[idx] == 1:
                    point = list(self.random_coordinate(map_face[idx], 0, 0.25))
                    point_sym = list(point)
                    point.insert(i, 0.0)
                    point_sym.insert(i, 1.0)
                    self.add_point(point)
                    self.add_point(point_sym)
        # Interior
        map_interior = [(0.25, 0.25, 0.25), (0.5, 0.25, 0.25), (0.75, 0.25, 0.25),
                        (0.25, 0.5, 0.25), (0.5, 0.5, 0.25), (0.75, 0.5, 0.25),
                        (0.25, 0.75, 0.25), (0.5, 0.75, 0.25), (0.75, 0.75, 0.25),

                        (0.25, 0.25, 0.5), (0.5, 0.25, 0.5), (0.75, 0.25, 0.5),
                        (0.25, 0.5, 0.5), (0.5, 0.5, 0.5), (0.75, 0.5, 0.5),
                        (0.25, 0.75, 0.5), (0.5, 0.75, 0.5), (0.75, 0.75, 0.5),

                        (0.25, 0.25, 0.75), (0.5, 0.25, 0.75), (0.75, 0.25, 0.75),
                        (0.25, 0.5, 0.75), (0.5, 0.5, 0.75), (0.75, 0.5, 0.75),
                        (0.25, 0.75, 0.75), (0.5, 0.75, 0.75), (0.75, 0.75, 0.75)]
        interior_node = [random.randint(0, 1) for _ in range(len(map_interior))]
        for idx, point_interior in enumerate(map_interior):
            if interior_node[idx] == 1:
                point = list(self.random_coordinate(map_interior[idx], 0, 0.1))
                self.add_point(point)

        self.remove_nodes_outside_unit_cube()
        print(len(self.nodes))

        self.remove_nodes_too_close_advanced()
        print(len(self.nodes))

        # Generate beam at least 2 beams per node
        for beam in range(1):
            beam = Beam(self.nodes[random.randint(0, len(self.nodes) - 1)],
                        self.nodes[random.randint(0, len(self.nodes) - 1)], beamRadius,
                        beamMaterial, 0)
            if self.beam_already_exist(beam):
                self.beams.append(beam)
        return self.nodes, self.beams

    def beam_already_exist(self, beam_test):
        # print(beam_test.point1, beam_test.point2)
        for beam in self.beams:
            if beam.point1 == beam_test.point1:
                if beam.point2 == beam_test.point2:
                    # print(beam.point1,beam.point2)
                    # print(False)
                    return False
            if beam.point1 == beam_test.point2:
                if beam.point2 == beam_test.point1:
                    # print(beam.point1,beam.point2)
                    # print(False)
                    return False
        # print(True)
        return True

    def remove_nodes_outside_unit_cube(self):
        """
        Remove nodes that are outside of the unit cube defined by the cell dimensions.
        """
        inside_nodes = []
        for point in self.nodes:
            if 0 <= point.x <= self.cellSizeX and 0 <= point.y <= self.cellSizeY and 0 <= point.z <= self.cellSizeZ:
                inside_nodes.append(point)
        self.nodes = inside_nodes

    def is_node_in_corner(self, node):
        """
        Check if a node is in a corner of the unit cube.

        :param node: The node to check.
        :return: True if the node is in a corner, False otherwise.
        """
        return ((node.x in [0, self.cellSizeX]) and
                (node.y in [0, self.cellSizeY]) and
                (node.z in [0, self.cellSizeZ]))

    def remove_nodes_too_close_advanced(self, min_distance=0.1):
        """
        Remove nodes that are too close together with a refined decision process.
        """
        to_remove = set()

        def is_surface_not_corner(node):
            return self.is_node_on_surface(node) and not self.is_node_in_corner(node)

        for i, node_i in enumerate(self.nodes):
            if i in to_remove:
                continue

            for j, node_j in enumerate(self.nodes[i + 1:], start=i + 1):
                if j in to_remove:
                    continue

                # Calculate Euclidean distance
                distance = math.sqrt((node_i.x - node_j.x) ** 2 +
                                     (node_i.y - node_j.y) ** 2 +
                                     (node_i.z - node_j.z) ** 2)

                if distance < min_distance:

                    if self.is_node_in_corner(node_i):
                        to_remove.add(j)
                        continue
                    elif self.is_node_in_corner(node_j):
                        to_remove.add(i)
                        continue

                    if self.is_node_on_surface(node_i) and not self.is_node_on_surface(node_j):
                        to_remove.add(i)
                    elif not self.is_node_on_surface(node_i) and self.is_node_on_surface(node_j):
                        to_remove.add(j)
                    else:

                        to_remove.add(j)  # Choix arbitraire pour supprimer
                        if is_surface_not_corner(node_j):
                            symmetric_node = self.find_symmetric_node(node_j)
                            if symmetric_node and not self.is_node_in_corner(symmetric_node):
                                symmetric_index = self.nodes.index(symmetric_node)
                                to_remove.add(symmetric_index)

        self.nodes = [node for index, node in enumerate(self.nodes) if index not in to_remove]

    def is_node_on_surface(self, node):
        """
        Check if a node is on the surface of the unit cube.

        :param node: The node to check.
        :return: True if the node is on the surface, False otherwise.
        """
        return (node.x in [0, self.cellSizeX] or
                node.y in [0, self.cellSizeY] or
                node.z in [0, self.cellSizeZ])

    def find_symmetric_node(self, node):
        """
        Find a symmetric node to a given node, based on the cube's faces. If a node is on the face X=0,
        its symmetric is on the face X=cellSizeX, and analogously for Y and Z axes.

        :param node: The node for which to find a symmetric counterpart.
        :return: The symmetric node, if found.
        """

        symmetric_x = self.cellSizeX - node.x if node.x in [0, self.cellSizeX] else node.x
        symmetric_y = self.cellSizeY - node.y if node.y in [0, self.cellSizeY] else node.y
        symmetric_z = self.cellSizeZ - node.z if node.z in [0, self.cellSizeZ] else node.z

        for n in self.nodes:
            if n.x == symmetric_x and n.y == symmetric_y and n.z == symmetric_z:
                return n
        return None

    def calculate_connections(self):
        """
        Calculate the number of connections for each node.

        :return: Dictionary containing the number of connections for each node index
        """
        connections = {}
        for i, point in enumerate(self.nodes):
            connections[i] = 0
        for beam in self.beams:
            start_point_index = self.nodes.index(beam.point1)
            end_point_index = self.nodes.index(beam.point2)
            connections[start_point_index] += 1
            connections[end_point_index] += 1
        return connections

    def remove_isolated_beams(self):
        """
        Remove isolated beams (beams connected to only one node).
        """
        point_counts = {}

        for beam in self.beams:
            point1 = beam.point1
            point2 = beam.point2

            if point1 not in point_counts:
                point_counts[point1] = 0
            if point2 not in point_counts:
                point_counts[point2] = 0

            point_counts[point1] += 1
            point_counts[point2] += 1

        self.beams = [beam for beam in self.beams if point_counts[beam.point1] > 1 and point_counts[beam.point2] > 1]

    def num_connections(self):
        """
        Calculate the total number of connections in the cell.

        :return: Total number of connections
        """
        total_connections = 0
        for beam in self.beams:
            total_connections += beam.num_connections()
        return total_connections

    def display_point(self, ax, color1=None, color2=None, color3=None):
        """
        Display nodes in the 3D plot.

        :param ax: Matplotlib 3D axis object
        :param color1: Color for corner points
        :param color2: Color for corner-edge points
        :param color3: Color for edge points
        """
        for point in self.nodes:
            x, y, z = point.x, point.y, point.z
            color = color1
            if z == 0 or z == self.cellSizeZ:
                if (x == 0 or x == self.cellSizeX) and (y == 0 or y == self.cellSizeY):
                    color = color2
                else:
                    color = 'y'
            elif (x == 0 or x == self.cellSizeX) or (y == 0 or y == self.cellSizeY):
                color = color3
            ax.scatter(x, y, z, c=color)

    def display_point_simple(self, ax, color):
        """
        Display nodes in the 3D plot using a simple color.

        :param ax: Matplotlib 3D axis object
        :param color: Color for points
        """
        for point in self.nodes:
            x, y, z = point.x, point.y, point.z
            ax.scatter(x, y, z, c=color)

    def display_beams(self, ax):
        """
        Display beams in the 3D plot.

        :param ax: Matplotlib 3D axis object
        """
        color = ['blue', 'green', 'black', 'yellow', 'orange']
        for index, beam in enumerate(self.beams):
            point1 = beam.point1
            point2 = beam.point2
            ax.plot([point1.x, point2.x], [point1.y, point2.y], [point1.z, point2.z], color=color[beam.material])

    def visualize_3d(self, ax):
        """
        Visualize the cell in a 3D plot.

        :param ax: Matplotlib 3D axis object
        """
        self.display_point(ax, 'r', 'pink', 'black')
        self.display_beams(ax, 'b', 'r')
