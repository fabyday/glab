import numpy as np
import filesyshelper as fs
import re 



class ObjReader():
    #TODO make regualr exp finding " (v or f) 1 2 3 " style pattern
    __sObjFileVertexPattern = re.compile("")
    __sObjFileFacePattern = re.compile("")

    def __init__(self, name_pattern : str):
        """
        input arguments
        (str :) name_pattern : 
        """
        

        self.name_pattern = name_pattern
        self.previous_name = None
        

    def writeFile(self, fileName, vertices, faces):
        """
        input arguments
        vertices : ndArray (Number of vertices x 3)
        faces : ndArray (Number of faces x 3)
        return 
        None
        """
        #test file name. make that name by filesystemhelper
        with open(fileName, "w", encoding='utf-8') as fp:
            for v in vertices : 
                fp.writeline( "v "+" ".join(v.astype(str)) )

            for f in faces :
                fp.writeline( "f " + " ".join(f.astype(str)) )

    def readFile(self, fileName):
        """
            input arguments
                - None
            return : tuple of ndArray
                - (
                    vertex : ndArray Number of vertices x 3 
                  , faces  : ndArray Number of faces x 3
                  )
        """

        vertices = []
        faces = []
        #TODO make numpy array vertices & faces.
        with open(fileName, 'r', encoding='utf-8') as fp:
            while(1):
                lines = fp.readline()
                vertices.append(lines)


        
        return ( np.array(vertices), np.array(faces) )


    