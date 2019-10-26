import numpy as np
import filesyshelper as fs
import re 



class ObjReader():
    #TODO make regualr exp finding " (v or f) 1 2 3 " style pattern
    _obj_file_vertex_pattern = re.compile("")
    _obj_file_face_pattern = re.compile("")

    def __init__(self, name_pattern : str):
        """
        input arguments
        (str :) name_pattern : 
        """
        

        self.name_pattern = name_pattern
        self.previous_name = None
        

    def set_working_dir(self, path):
        pass

    def __save_to_file(self,vertices, faces):
        """
        input arguments
        vertices : ndArray (Number of vertices x 3)
        faces : ndArray (Number of faces x 3)
        return 
        None
        """
        #test file name. make that name by filesystemhelper
        filename = "test"
        with open(filename, "w", encoding='utf-8') as fp:
            for v in vertices : 
                fp.writeline( "v "+" ".join(v.astype(str)) )

            for f in faces :
                fp.writeline( "f " + " ".join(f.astype(str)) )

    def __load_from_file(self):
        """
            input arguments
                - None
            return : tuple of ndArray
                - (
                    vertex : ndArray Number of vertices x 3 
                  , faces  : ndArray Number of faces x 3
                  )
        """

        filename = "test"
        vertices = []
        faces = []
        #TODO make numpy array vertices & faces.
        with open(filename, 'r', encoding='utf-8') as fp:
            while(1):
                lines = fp.readline()
                vertices.append(lines)



        return ( vertices, faces )


    