from random import random, randint
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

H = 200
W = 200
matrix = np.zeros((H,W))
img = Image.fromarray(matrix)
img.convert('RGB').save("images/Black.jpg","JPEG")

matrix = np.empty((H,W))
matrix.fill(255)
img = Image.fromarray(matrix)
img.convert('RGB').save("images/White.jpg","JPEG")

matrix = np.zeros((H, W, 3), dtype=np.uint8)
matrix[0:H, 0:W] = [255,0,0]
img = Image.fromarray(matrix,'RGB')
img.save("images/Red.jpg","JPEG")

matrix = np.zeros((H, W, 3), dtype=np.uint8)
matrix = [[[randint(0,255),randint(0,255),randint(0,255)] for i in range(H)] for j in range(W)]
img = Image.fromarray(np.asarray(matrix),'RGB')
img.save("images/Random.jpg","JPEG")



