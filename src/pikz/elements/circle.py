from ..abc import Fillable
from ..coordinate import Coordinate, COORD_ARG


class Circle(Fillable):

    def __init__(self,
                 center: COORD_ARG = (0, 0),
                 radius: float = 0,
                 *args, **kwargs):

        self._center = Coordinate.from_args(center)
        self._radius = radius
        super().__init__(*args, **kwargs)

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    def tikz_draw(self,
                  style: str = None,
                  color: str = None,
                  thickness: str = None) -> str:
        return f"{self.draw_command(style, color, thickness)} {self._center} circle ({self._radius});"

    def tikz_fill(self, fill: str = None):
        return f"{self.fill_command(fill)} {self._center} circle ({self._radius});"

    def translate(self,
                  x: float = 0,
                  y: float = 0,
                  inplace: bool = False):

        center = self._center.translate(x, y)
        if inplace:
            self._center = center
            return

        return Circle(center=center,
                      radius=self.radius,
                      style=self.style,
                      thickness=self.thickness,
                      color=self.color,
                      fill=self.fill)

    def __repr__(self):
        return f"<Circle at {self._center} with radius {self._radius}>"