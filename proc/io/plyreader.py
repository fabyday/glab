import numpy as np 

#format name
__gFileInfoStr = "ply"
__gPlyCommentStr = "comment"
__gFormatStr = "format" 
__gElementStr = "element"
__gPropertyStr = "property"
__gEndHeaderStr = "end_header"


__gPlyComment = "made by glab library"
__gFormatArgs = "ascii 1.0"
__gElementvertexPostfix = "vertex"
__gElementFacePostfix = "face"


__gPreCheckTable = [__gFileInfoStr, __gFormatStr]
__gPostCheckTable = [__gElementFacePostfix, __gElementvertexPostfix]

class PlyReader():
    """
        Class PlyReader
            .ply reader

    """

    def __init__(self):
        pass
    
    def writeFile(self, fileName, vertices, faces):
        """
        input arguments
        vertices : ndArray (Number of vertices x 3)
        faces : ndArray (Number of faces x 3)
        return 
        None
        """

        vertexShape = list(vertices.shape)
        faceShape = list(faces.shape)

        if len(vertexShape) > 2 :
            raise Exception("[ writeFile : vertex demension is too much. only 2-Demension is needed.]")
        if len(faceShape) > 2 : 
            raise Exception("[ writeFile : face demension is too much. only 2-Demension is needed.]") 
        
        #test file name. make that name by filesystemhelper
        with open(fileName, "w", encoding='utf-8') as fp:
            
            ###############################################################################################
            #           header make
            ###############################################################################################
            fp.writeline(__gFileInfoStr)                                # explicit ply file format
            fp.wrtieLine(__gFormatStr)                                  # explicit format ascii 1.0
            fp.writeline(" ".join([__gPlyCommentStr, __gPlyComment]))   # comment it is made by glab lib
            fp.writeline(" ".join([__gElementStr, __gElementvertexPostfix, str(vertexShape[0])])  # number of vertex info
            fp.writeline(" ".join( [ gElementStr, __gElementFacePostfix,  str( faceShape[0] ] ) ) )      # number of face info
            fp.writeline(__gEndHeaderStr)                               # header end
            ###############################################################################################
            for v in vertices :                                         # loop for writing vertex info
                fp.writeline( " ".join(v.astype(str)) )

            for f in faces :                                            # loop for writing face info
                fp.writeline( " ".join(f.astype(str)) )



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
            lines = fp.readline()
            if line == "ply" : 
                    pass
            else : 
                raise Exception("ply header error.")
            while(True):                # header read
                lines = fp.readline()
                lines = lines.split() # ['a', 'b']
                line = lines[0]

                if line == "ply" : 
                    continue
                elif line == "end_header" :
                    break
                elif line == "":
                    break
                elif line ==
            
            
            while(True):                # vertex information read
                lines = fp.readline()
                if not lines : 
                    break
                
                lines = lines.split()
                info = list(map(int, lines))
                vertices.append(info)

            while(True) :               # face information read
                pass


        return ( np.array(vertices), np.array(faces) )

