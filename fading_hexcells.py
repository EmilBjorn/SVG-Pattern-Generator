"""
Module to draw a SVG of hexagonal cells that are complete in the bottom, 
but gradually becomes less complete in the top of the drawing
"""
#%%#
import math
import random
import svg

# import fpdf


#%%#
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
        sidelength=60,
        completion: float = 1,
        start_coord: tuple[int, int] = (0, 0)
    ) -> svg.Element:
        # elements: list[svg.Element] = []
        # elements.append(
        #         svg.Line(x1=)
        # )

        hexrelativecoordinates2 = [(0, 1), (math.cos(deg30), math.sin(deg30)),
                                   (math.cos(deg30), -math.sin(deg30)),
                                   (0, -1),
                                   (-math.cos(deg30), -math.sin(deg30)),
                                   (-math.cos(deg30), math.sin(deg30))]

        linesegments: list[svg.Element] = [
            svg.M(*start_coord),
            svg.m(*hexrelativecoordinates2[5])
        ]

        for i in range(0, 6):

            drawline = True if random.random() < completion else False
            coords = [x * sidelength for x in hexrelativecoordinates2[i]]

            linesegment = svg.l(*coords)  #if drawline else svg.m(*coords)

            linesegments.append(linesegment)

        hexagon = svg.Path(d=linesegments, stroke="red", fill="none")

        return hexagon if drawline else None

    for i in range(10):
        for j in range(10):
            pos = hexstartpos((i, j), 11.5)
            pct = math.sqrt((1 / (j + 1)))
            print(pct)
            elements.append(hexagon(10, pct, pos))

    # elements.append(hexagon(40, 0.5, (50, 100)))

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

# %%
