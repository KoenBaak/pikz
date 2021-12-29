from abc import ABC, abstractmethod


class Drawable(ABC):

    @abstractmethod
    def tikz_draw(self) -> str:
        pass


class Fillable(Drawable):

    @abstractmethod
    def tikz_fill(self) -> str:
        pass
