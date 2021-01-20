import networkx as nx
import itertools

class myGraph:
    def __init__(self):
        self.__filmsAndActors = {}
        self.__data = []
        self.__Graph = nx.Graph()
        self.__nodes = []
 
    def setData(self, data):
        self.__clearData()
        self.__data = data
        self.__setFilmsAndActors()
        self.__setNodes()
        self.__buildGraph()
    
    def __clearData(self):
        self.__filmsAndActors = {}
        self.__data = []
        self.__Graph = nx.Graph()
        self.__nodes = []
        
    def __setFilmsAndActors(self):
        for actor in self.__data:
            for film in actor['films']:
                nameAndYear = film['title'] + ' (' + str(film['year']) + ')'
                if nameAndYear in self.__filmsAndActors.keys():
                    self.__filmsAndActors[nameAndYear].append(actor['name'])
                else:
                    self.__filmsAndActors[nameAndYear] = []
                    self.__filmsAndActors[nameAndYear].append(actor['name'])

    def __setNodes(self):
        for actor in self.__data:
            self.__nodes.append(actor['name'])
    
    def getNodes(self):
        return self.__nodes
   
    def __buildGraph(self):
        self.__Graph.add_nodes_from( self.__nodes)

        for value in self.__filmsAndActors.values():
            pairsOfVertices = list(itertools.combinations(value,2))
            if(len(pairsOfVertices)>=1):
                self.__Graph.add_edges_from(pairsOfVertices)
    
    def getTheBaconNumber(self, actorName):
        pathFromNames = nx.shortest_path(self.__Graph, source = actorName, target = 'Kevin Bacon')
        text = ''
        baconNumber = len(pathFromNames)-1

        def getFilm(actor1, actor2):
            for film, names in self.__filmsAndActors.items():
                if actor1 and actor2 in names:
                    return film 

        for i in range(baconNumber):
            actor1 = pathFromNames[i]
            actor2 = pathFromNames[i+1]
            film = getFilm(actor1, actor2)
            text +=  actor1 + ' was in ' + film + ' with ' + actor2 + '\n'
        text +=  pathFromNames[0] + '\'s'+ ' Bacon number is ' + str(baconNumber) + '\n'
        
        return text
