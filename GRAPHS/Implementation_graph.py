class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo={}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys() #return all the keys of dict

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + "connected to" + str([x.id for x in self.connectedTo])





