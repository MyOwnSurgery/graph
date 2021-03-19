import math

import numpy as np
from numpy import linalg as LA
from PIL import Image, ImageDraw
from task4and6 import Parser

def bar_coord(x0, y0, x1, y1, x2, y2, x, y):
        lambda0 = ((x1-x2)*(y-y2) - (y1-y2)*(x-x2))/((x1-x2)*(y0-y2)-(y1-y2)*(x0-x2))
        lambda1 = ((x2-x0)*(y-y0) - (y2-y0)*(x-x0))/((x2-x0)*(y1-y0)-(y2-y0)*(x1-x0))
        lambda2 = ((x0-x1)*(y-y1) - (y0-y1)*(x-x1))/((x0-x1)*(y2-y1)-(y0-y1)*(x2-x1))

        print(lambda0+lambda1+lambda2)
        return lambda0, lambda1, lambda2

def draw_triangles(x0,y0,x1,y1,x2,y2, image, color, size):
        draw = ImageDraw.Draw(image)
        xmin = math.floor(np.min([x0,x1,x2]))
        ymin = math.floor(np.min([y0,y1,y2]))
        xmax= math.ceil(np.max([x0,x1,x2]))
        ymax= math.ceil(np.max([y0,y1,y2]))
        if(xmin < 0):
            xmin = 0
        if(ymin < 0):
            ymin = 0
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                lambda0, lambda1, lambda2 = bar_coord(x0, y0, x1, y1, x2, y2, x, y)
                if lambda0 > 0 and lambda1 > 0 and lambda2 > 0:
                    draw.point((x, size - y), color)


def draw_polygons(image):
    parser = Parser()
    parser.load_vertex("Test_rabbit.txt", False)
    parser.load_polygons("Test_rabbit.txt")
    for polygon in parser.polygon_list:
        triangle = []
        for point in polygon:
            x, y = parser.vertex_list[point - 1]
            triangle.append((20000 * x + 2000, 20000 * y + 2000))
        print(triangle)
        draw_triangles(triangle[0][0], triangle[0][1], triangle[1][0], triangle[1][1], triangle[2][0], triangle[2][1], image, (np.random.randint(256),np.random.randint(256),np.random.randint(256)), size)
    image.save("images/PozhiloyRabbitPolygonsTriangles.jpg", "JPEG")

size = 5000
image = Image.new('RGB', (size, size))
draw_polygons(image)



