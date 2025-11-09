import settings
from logic.rubiks_cube import RubiksCube
from ui import RubiksCubeDisplay

if __name__ == "__main__":
    rubiks_cube = RubiksCube(settings.RUBIKS_CUBE_SIZE)
    RubiksCubeDisplay(
        rubiks_cube, settings.CUBE_SIZE, settings.NUMBER_OF_FRAMES
    ).display()
