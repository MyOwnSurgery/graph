class Parser:
    def __init__(self):
        self.vertex_list = []
        self.polygon_list = []
        self.vertex_list_z = []

    def load_vertex(self, fileName,z):
        objFile = open(fileName)
        for line in objFile:
            split = line.split()
            # if blank line, skip
            if not len(split):
                continue
            if split[0] == "v":
                tmp = [float(i) for i in split[1:]]
                if z == True:
                 cord = (tmp[0],tmp[1],tmp[2])
                else:
                 cord = (tmp[0], tmp[1])
                self.vertex_list.append(cord)
        objFile.close()


    def load_polygons(self, fileName):
        objFile = open(fileName)
        for line in objFile:
            split = line.split()
            # if blank line, skip
            if not len(split):
                continue
            if split[0] == "f":
                polygons = (int(split[1:][0].partition('/')[0]),int(split[1:][1].partition('/')[0]),int(split[1:][2].partition('/')[0]))
                self.polygon_list.append(polygons)

        objFile.close()










