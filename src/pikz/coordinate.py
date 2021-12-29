from typing import Union
import math

COORD_ARG = Union['Coordinate', tuple, complex]


def Polar(angle: float, radius: float, rad: bool = False):
    return Coordinate.from_polar(angle, radius, rad)


class Coordinate:

    __slots__ = ['_x', '_y']

    def __init__(self,
                 x: float,
                 y: float):

        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @classmethod
    def from_tuple(cls, xy: tuple):
        return cls(*xy)

    @classmethod
    def from_complex(cls, z: complex):
        return cls(z.real, z.imag)

    @classmethod
    def from_polar(cls, angle: float, radius: float, rad: bool = False):
        if not rad:
            angle = angle * (2 * math.pi) / 360
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return cls(x, y)

    @classmethod
    def from_args(cls, *args):
        if len(args) == 1:
            argument = args[0]
            if isinstance(argument, tuple):
                return cls.from_tuple(argument)
            if isinstance(argument, cls):
                return argument
            if isinstance(argument, complex):
                return cls.from_complex(argument)
        if len(args) == 2:
            return cls(*args)
        raise ValueError(f"Can not transform input {args} to a Pikz Coordinate")

    def to_str(self, precision: int = 3) -> str:
        return "({x:.{precision}f}, {y:.{precision}f})".format(x=self._x,
                                                               y=self._y,
                                                               precision=precision)

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"<Coordinate ({self._x:.3f}, {self._y:.3f})>"