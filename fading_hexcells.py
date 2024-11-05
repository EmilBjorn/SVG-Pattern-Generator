"""
Module to draw a SVG of hexagonal cells that are complete in the bottom, 
but gradually becomes less complete in the top of the drawing
"""

import math
import random
import svg

# import fpdf


def draw(width, height, stroke=0.02, *args, **kwargs) -> svg.SVG:

    elements: list[svg.Element] = []
    deg30 = 30 / 360 * 2 * math.pi

    if len(args) + len(kwargs) != 0:
        pass

    # Draw bounding box

    elements.append(
        svg.Rect(
            x=0,
            y=0,
            #  rx=8,
            #  ry=8,
            width=width,
            height=height,
            stroke_width=stroke,
            fill="pink",
            stroke="black"))

    # Eksempel på at bruge polygon - det er dog ikke viable til endelig løsning, da jeg ikke kan fjerne siderne.
    # Der skal i stedet bruges Line elementer
    sidelength = 60
    # elements.append(
    #     svg.Polygon(points=[
    #         0,
    #         math.sin(deg30) * sidelength, 0,
    #         (math.sin(deg30) + 1) * sidelength,
    #         math.cos(deg30) * sidelength,
    #         (2 * math.sin(deg30) + 1) * sidelength,
    #         2 * math.cos(deg30) * sidelength,
    #         (math.sin(deg30) + 1) * sidelength,
    #         2 * math.cos(deg30) * sidelength,
    #         math.sin(deg30) * sidelength,
    #         math.cos(deg30) * sidelength, 0
    #     ],
    #                 stroke="black",
    #                 fill="white"))

    elements.append(
        svg.Path(d=[
            svg.M(50 + 0, 50 + math.sin(deg30) * sidelength),
            svg.L(50 + 0, 50 + (math.sin(deg30) + 1) * sidelength),
            svg.L(50 + math.cos(deg30) * sidelength,
                  50 + (2 * math.sin(deg30) + 1) * sidelength),
            svg.M(50 + 2 * math.cos(deg30) * sidelength,
                  50 + (math.sin(deg30) + 1) * sidelength),
            svg.L(50 + 2 * math.cos(deg30) * sidelength,
                  50 + math.sin(deg30) * sidelength),
            svg.L(50 + math.cos(deg30) * sidelength, 50 + 0)
        ],
                 stroke="black",
                 fill="None"))

    def hexstartpos(index: tuple, sidelength: int = 1) -> tuple:
        # function to generate starting positions for hexagons in grid

        x_index, y_index = index

        x_coord = x_index + (y_index % 2) / 2
        y_coord = y_index

        x_normalizer = 2 * math.cos(deg30) * sidelength
        y_normalizer = (1 + math.sin(deg30)) * sidelength

        coords = (x_coord * x_normalizer, y_coord * y_normalizer)

        return coords

    group = svg.G(elements=elements)

    def hexagon(
        unit_sidelength: float = 1,
        sides: int = 6,
        start_coord: tuple[int, int] = (0, 0)) -> svg.Element:
        # elements: list[svg.Element] = []
        # elements.append(
        #         svg.Line(x1=)
        # )

        def hexcoordinates(index, sidelength=1) -> dict:
            coordinates = {
                "0": {
                    "x": 0,
                    "y": math.sin(deg30) * sidelength
                },
                "1": {
                    "x": 0,
                    "y": (math.sin(deg30) + 1) * sidelength
                },
                "2": {
                    "x": math.cos(deg30) * sidelength,
                    "y": (2 * math.sin(deg30) + 1) * sidelength
                },
                "3": {
                    "x": 2 * math.cos(deg30) * sidelength,
                    "y": (math.sin(deg30) + 1) * sidelength
                },
                "4": {
                    "x": 2 * math.cos(deg30) * sidelength,
                    "y": math.sin(deg30) * sidelength
                },
                "5": {
                    "x": math.cos(deg30) * sidelength,
                    "y": 0
                }
            }

            return coordinates[str(index)]

        return

    return svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, width, height),
        width=str(width) + "mm",
        height=str(height) + "mm",
        elements=[group],
    )


if __name__ == '__main__':

    WIDTH = 300
    HEIGHT = 200
    LANDSCAPE = False

    canvas = draw(WIDTH, HEIGHT)
    with open('output.svg', 'w', encoding='UTF-8') as file:
        file.write(str(canvas))
