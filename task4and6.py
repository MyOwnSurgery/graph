class Parser:
    def __init__(self):
        self.vertex_list = []
        self.polygon_list = []
        self.vertex_list_z = []
        self.norm_list = []
        self.index_list = []

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

    def load_norms(self, fileName):
        objFile = open(fileName)
        for line in objFile:
            split = line.split()
            if split[0] == "vn":
                norms = (float(split[1]), float(split[2]),
                            float(split[3]))
                self.norm_list.append(norms)

    def load_normal_indexes(self, fileName):
        objFile = open(fileName)
        for line in objFile:
            split = line.split()
            # if blank line, skip
            if not len(split):
                continue
            if split[0] == "f":
                first = (split[1:][0])[::-1]
                second = (split[1:][1])[::-1]
                third = (split[1:][2])[::-1]
                indexes = (int(first.partition('/')[0][::-1]), int(second.partition('/')[0][::-1]),
                            int(third.partition('/')[0][::-1]))
                self.index_list.append(indexes)

        objFile.close()





parser = Parser()
parser.load_norms("Test_rabbit.txt")
parser.load_polygons("Test_rabbit.txt")
parser.load_vertex("Test_rabbit.txt", True)
parser.load_normal_indexes("Test_rabbit.txt")





