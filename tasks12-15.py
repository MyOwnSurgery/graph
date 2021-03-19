import numpy as np
from numpy import linalg as LA
from PIL import Image, ImageDraw
import math
from task4and6 import Parser

class Z_buf:
    def __init__(self):
        self.buffer = [[10000 for i in range(size)] for j in range(size)]

def bar_coord(x0, y0, x1, y1, x2, y2, x, y):
        lambda0 = ((x1-x2)*(y-y2) - (y1-y2)*(x-x2))/((x1-x2)*(y0-y2)-(y1-y2)*(x0-x2))
        lambda1 = ((x2-x0)*(y-y0) - (y2-y0)*(x-x0))/((x2-x0)*(y1-y0)-(y2-y0)*(x1-x0))
        lambda2 = ((x0-x1)*(y-y1) - (y0-y1)*(x-x1))/((x0-x1)*(y2-y1)-(y0-y1)*(x2-x1))

        #print(lambda0+lambda1+lambda2)
        return lambda0, lambda1, lambda2

def draw_triangles(x0,y0,z0,x1,y1,z1,x2,y2,z2, image, color, size, z_buf):
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
                    z_tilda = lambda0*z0 + lambda1*z1 + lambda2*z2
                    if z_tilda < z_buf.buffer[x][y]:
                        draw.point((x, size - y), color)
                        z_buf.buffer[x][y] = z_tilda



def draw_polygons(image):
    parser = Parser()
    parser.load_vertex("Test_rabbit.txt", True)
    parser.load_polygons("Test_rabbit.txt")
    z_buf = Z_buf()
    for polygon in parser.polygon_list:
        triangle = []
        for point in polygon:
            x, y, z = parser.vertex_list[point - 1]
            triangle.append((20000 * x + 2000, 20000 * y + 2000, 20000 * z + 2000))
        n = count_norm(triangle)
        cos = get_cos(n)
        if cos < 0:
         draw_triangles(triangle[0][0], triangle[0][1], triangle[0][2], triangle[1][0], triangle[1][1], triangle[1][2], triangle[2][0], triangle[2][1], triangle[2][2], image, (-int(255 * cos),-int(255 * cos),-int(255 * cos)), size, z_buf)
        else:
            continue
    image.save("images/PozhiloyRabbitPolygonsTrianglesLight.jpg", "JPEG")

def count_norm(triangle):
    return np.cross([triangle[1][0] - triangle[0][0], triangle[1][1] - triangle[0][1], triangle[1][2] - triangle[0][2]], [triangle[1][0] - triangle[2][0], triangle[1][1] - triangle[2][1], triangle[1][2] - triangle[2][2]])

def get_cos(n):
    return np.dot(n,[0, 0, 1])/(LA.norm(n)*LA.norm([0, 0, 1]))



size = 5000
image = Image.new('RGB', (size, size))
draw_polygons(image)





