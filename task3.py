import numpy as np
from PIL import Image, ImageDraw


def line(start,finish,img):
    draw = ImageDraw.Draw(img)
    steep = False
    if abs(start[0] - finish[0]) < abs(start[1] - finish[1]):
        start = (start[1], start[0])
        finish = (finish[1], finish[0])
        steep = True
    if start[0] > finish[0]:
        start, finish = finish, start
    dx = -start[0] + finish[0]
    dy = -start[1] + finish[1]
    if dx == 0:
        derror = 0
    else:
        derror = abs(dy / dx)
    error = 0
    y = start[1]
    for x in range(start[0], finish[0]):
        if steep:
            draw.point((y,x))
        else:
            draw.point((x,y))
        error += derror
        if error > 0.5:
            if start[1] > finish[1]:
                y += -1
            else:
                y += 1
            error -= 1



img = Image.new("RGB", (200,200))

for i in range(13):
    line((100, 100), (int(100 + 95 * np.sin(2*np.pi*i/13)), int(100 + 95 * np.cos(2*np.pi*i/13))), img)

img.save("images/Star.jpg", "JPEG")










