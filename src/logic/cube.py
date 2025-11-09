from typing import Any

from .enums import Color, Face


class Cube:
    def __init__(self, facecolors: dict[Face, Color]) -> None:
        self.facecolors = facecolors

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Cube):
            return False
        return self.facecolors == other.facecolors

    def __hash__(self) -> int:
        return id(self)

    def rotate_xz(self) -> None:
        self.facecolors = {
            Face.FRONT: self.facecolors[Face.FRONT],
            Face.RIGHT: self.facecolors[Face.BOTTOM],
            Face.BACK: self.facecolors[Face.BACK],
            Face.LEFT: self.facecolors[Face.TOP],
            Face.BOTTOM: self.facecolors[Face.LEFT],
            Face.TOP: self.facecolors[Face.RIGHT],
        }

    def rotate_xy(self) -> None:
        self.facecolors = {
            Face.FRONT: self.facecolors[Face.RIGHT],
            Face.RIGHT: self.facecolors[Face.BACK],
            Face.BACK: self.facecolors[Face.LEFT],
            Face.LEFT: self.facecolors[Face.FRONT],
            Face.BOTTOM: self.facecolors[Face.BOTTOM],
            Face.TOP: self.facecolors[Face.TOP],
        }

    def rotate_yz(self) -> None:
        self.facecolors = {
            Face.FRONT: self.facecolors[Face.BOTTOM],
            Face.RIGHT: self.facecolors[Face.RIGHT],
            Face.BACK: self.facecolors[Face.TOP],
            Face.LEFT: self.facecolors[Face.LEFT],
            Face.BOTTOM: self.facecolors[Face.BACK],
            Face.TOP: self.facecolors[Face.FRONT],
        }
