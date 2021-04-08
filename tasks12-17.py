import numpy as np
from numpy import linalg as LA
from PIL import Image, ImageDraw
import math
from task4and6 import Parser


class Z_buf:
    def __init__(self):
        self.buffer = [[10000 for i in range(size)] for j in range(size)]


def bar_coord(x0, y0, x1, y1, x2, y2, x, y):
    lambda0 = ((x1 - x2) * (y - y2) - (y1 - y2) * (x - x2)) / ((x1 - x2) * (y0 - y2) - (y1 - y2) * (x0 - x2))
    lambda1 = ((x2 - x0) * (y - y0) - (y2 - y0) * (x - x0)) / ((x2 - x0) * (y1 - y0) - (y2 - y0) * (x1 - x0))
    lambda2 = ((x0 - x1) * (y - y1) - (y0 - y1) * (x - x1)) / ((x0 - x1) * (y2 - y1) - (y0 - y1) * (x2 - x1))

    return lambda0, lambda1, lambda2


def draw_triangles(x0, y0, z0, x1, y1, z1, x2, y2, z2, image, color, size, z_buf):
    draw = ImageDraw.Draw(image)
    xmin = math.floor(np.min([x0, x1, x2]))
    ymin = math.floor(np.min([y0, y1, y2]))
    xmax = math.ceil(np.max([x0, x1, x2]))
    ymax = math.ceil(np.max([y0, y1, y2]))
    if (xmin < 0):
        xmin = 0
    if (ymin < 0):
        ymin = 0
    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            lambda0, lambda1, lambda2 = bar_coord(x0, y0, x1, y1, x2, y2, x, y)
            if lambda0 > 0 and lambda1 > 0 and lambda2 > 0:
                z_tilda = lambda0 * z0 + lambda1 * z1 + lambda2 * z2
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
        triangle_proj = []
        for point in polygon:
            x, y, z = parser.vertex_list[point - 1]
            t_coord = turn_coord(x, y, z)
            x, y, z = t_coord[0], t_coord[1], t_coord[2]
            t_coord = move_coord(x, y, z)
            x, y, z = t_coord[0], t_coord[1], t_coord[2]

            coord = proj_coord(x, y, z)
            triangle.append((x, y, z))
            triangle_proj.append((coord[0], coord[1], 1.0))
        n = count_norm(triangle)
        cos = get_cos(n)
        if cos < 0:
            draw_triangles(triangle_proj[0][0], triangle_proj[0][1], triangle[0][2], triangle_proj[1][0],
                           triangle_proj[1][1], triangle[1][2], triangle_proj[2][0], triangle_proj[2][1],
                           triangle[2][2], image, (-int(255 * cos), -int(255 * cos), -int(255 * cos)), size, z_buf)
        else:
            continue
    image.save("images/PozhiloyRabbitPolygonsTrianglesLight.jpg", "JPEG")


def count_norm(triangle):
    return np.cross([triangle[1][0] - triangle[0][0], triangle[1][1] - triangle[0][1], triangle[1][2] - triangle[0][2]],
                    [triangle[1][0] - triangle[2][0], triangle[1][1] - triangle[2][1], triangle[1][2] - triangle[2][2]])


def get_cos(n):
    return np.dot(n, [0, 0, -1]) / (LA.norm(n) * LA.norm([0, 0, -1]))


def proj_coord(x, y, z):
    init_vec = np.array([[x], [y], [z]])
    ax = 20000
    ay = 20000
    u0 = 2500
    v0 = 2500
    matrix = np.array([[ax, 0, u0], [0, ay, v0], [0, 0, 1]])
    final_vec = matrix.dot(init_vec)
    return final_vec[0][0] / final_vec[2][0], final_vec[1][0] / final_vec[2][0]


def turn_coord(x, y, z):
    init_vec = np.array([[x], [y], [z]])
    alpha = 0
    beta = -1.57
    gamma = 0
    R_1 = np.array([[1, 0, 0], [0, np.cos(alpha), np.sin(alpha)], [0, -np.sin(alpha), np.cos(alpha)]])
    R_2 = np.array([[np.cos(beta), 0, np.sin(beta)], [0, 1, 0], [-np.sin(beta), 0, np.cos(beta)]])
    R_3 = np.array([[np.cos(gamma), np.sin(gamma), 0], [-np.sin(gamma), np.cos(gamma), 0], [0, 0, 1]])
    final_vec = ((R_1.dot(R_2)).dot(R_3)).dot(init_vec)
    return final_vec[0][0], final_vec[1][0], final_vec[2][0]


def move_coord(x, y, z):
    init_vec = np.array([[x], [y], [z]])
    t_vec = np.array([[0.005], [-0.045], [1.5]])
    final_vec = init_vec + t_vec
    return final_vec[0][0], final_vec[1][0], final_vec[2][0]


size = 5000
image = Image.new('RGB', (size, size))
draw_polygons(image)









