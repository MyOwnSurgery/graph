import numpy as np

from task4and6 import Parser
from PIL import Image, ImageDraw
from task3 import line

img = Image.new("RGB", (1000,1000))
draw = ImageDraw.Draw(img)
parser = Parser()
parser.load_vertex("Test_rabbit.txt", False)
point_list = []

for pair in parser.vertex_list:

    x = int(-8000*pair[0] + 500)
    y = int(-8000*pair[1] + 1000)
    point_list.append((x,y))
    draw.point((x,y))

img.save("images/PozhiloyRabbit.jpg", "JPEG")

parser.load_polygons("Test_rabbit.txt")

for polygon in parser.polygon_list:
    line(point_list[polygon[0] - 1], point_list[polygon[1] - 1], img)
    line(point_list[polygon[1] - 1], point_list[polygon[2] - 1], img)
    line(point_list[polygon[2] - 1], point_list[polygon[0] - 1], img)


img.save("images/PozhiloyRabbitPolygons.jpg", "JPEG")
