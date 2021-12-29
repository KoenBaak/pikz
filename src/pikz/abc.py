from abc import ABC, abstractmethod

from . import styles
from . import colors


class Drawable(ABC):

    def __init__(self,
                 style: str = styles.SOLID,
                 color: str = colors.BLACK,
                 thickness: str = None):

        self.style = style
        self.color = color
        self.thickness = thickness

    def draw_arguments(self,
                       style: str = None,
                       color: str = None,
                       thickness: str = None):

        given = (style, color, thickness)
        default = (self.style, self.color, self.thickness)
        valid = (x or y for x, y in zip(given, default))

        return [
            arg for arg in valid if arg is not None
        ]

    def draw_command(self,
                     style: str = None,
                     color: str = None,
                     thickness: str = None) -> str:

        props = ", ".join(self.draw_arguments(style, color, thickness))
        return f"\\draw[{props}]"

    @abstractmethod
    def tikz_draw(self,
                  style: str = None,
                  color: str = None,
                  thickness: str = None) -> str:
        pass


class Fillable(Drawable):

    def __init__(self,
                 style: str = styles.SOLID,
                 color: str = colors.BLACK,
                 thickness: str = None,
                 fill: str = None):

        self.fill = fill
        super().__init__(style, color, thickness)

    def fill_command(self, fill: str = None) -> str:

        fill = fill or self.fill

        if fill is None:
            raise ValueError("fill_command needs non None fill value")

        return f"\\fill[{fill}]"

    def tikz_drawfill(self,
                      style: str = None,
                      color: str = None,
                      thickness: str = None,
                      fill: str = None):

        if fill is not None or self.fill is not None:
            result = self.tikz_fill(fill) + "\n"
        else:
            result = ""

        return result + self.tikz_draw(style, color, thickness)

    @abstractmethod
    def tikz_fill(self, fill: str = None):
        pass
