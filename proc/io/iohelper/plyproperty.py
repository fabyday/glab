from sys import byteorder as _byteorder

class PlyProperty():

    def __init__(self):
        self._format = ["ascuu 1.0", "binary"]
        self._commnet = []
        self._headerKeyword = {"ply" : True,
                            "format" : True, 
                            "comment" : True, 
                            "element" : self.addElement, 
                            "property" : self.addProperty, 
                            "end_header" : True }


        self._latesetElementInfo = None
        self._elementsInfo = dict()
        self._propertyInfo = dict()

        self._xInfo = 0
        self._yInfo = 1
        self._zInfo = 2


        self._valueType = {"char" : lambda x:int(x), 
                        "uchar" : lambda x:int(x), 
                        "short" : lambda x:int(x),
                        "ushort" : lambda x:int(x),
                        "int" : lambda x:int(x),
                        "uint" : lambda x:int(x),
                        "float" : lambda x:float(x), 
                        "double" : lambda x:float(x),
                        "list" : "list"
                        }
                
    def setNeedElement(self, findList = ["vertex", "face"]):
        pass

    def addElement(self, key : str, value :str):
        try:
            self._elementsInfo[key] = int(value)
            self._latesetElementInfo = key
        except ValueError:
            raise Exception(__file__+"addElement function: can't transform to integer")

    def addProperty(self, propertyInfo : list):
        """
            input args
                -propertyInfo (type : string) : example like [float x] or [list uchar int vertex_index]
            return 
                None
        """
        try:
            self._propertyInfo[self._latesetElementInfo][propertyInfo[-1]]
            self._propertyInfo[self._latesetElementInfo][propertyInfo[-1]] = [self._valueType[x] for x in propertyInfo[:-1]]
        except KeyError:    
            self._propertyInfo[self._latesetElementInfo] = {propertyInfo[-1] : [self._valueType[x] for x in propertyInfo[:-1]]}


    def setEnvironment(self):
        self._xInfo = self._propertyInfo['x']
        self._yInfo = self._propertyInfo['y']
        self._zInfo = self._propertyInfo['z']



    def consume(self, rawLine=None) : 
        """
            rawLine (type str) : consuming string data. it is consider header line or rawdata lines.
        """
        if not rawLine:
            raise Exception("keyword was not find")

        rawdata = rawLine.split()
        if rawdata[0] not in self._headerKeyword :
            raise Exception("not allowed headerInfo keyword")
        else : 
            




if __name__ == "__main__":
    a = PlyProperty()
