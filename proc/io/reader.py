##############################################################################################
#                                    reader.py PREVIEW                                       #
#    reader.py help for reading 3d mesh data. reader.py supports { .obj, .ply } extension.   #
# 
##############################################################################################



import os
import numpy as np 






"""
private variables.
"""
__reader_abs_cur_dir = os.path.abspath(os.path.curdir)
class FileManager():
    def __init__(self):
        pass

    def setPath(self, path="./"):
        pass

    def readFile(self, fileName):
        pass

    
    def writeFile(self, data, name='no_name', path):
        """
        =========input arguments=====================================================================
            -[type : numpy array {Number of vertices} x 3] data :  a 3d Mesh's vertices informations. 
            -[type : string                              ] name : name of save file.
            -[type : string                              ] path : default is current dir's absolute path.
        ---------------------------------------------------------------------------------------------
        =========return arguments====================================================================
            -None
        ---------------------------------------------------------------------------------------------
        """
        pass



    def writeFile(self, data, name='no_name', path):

        """
        =========input arguments=====================================================================
            -[type : numpy array {Number of vertices} x 3] data :  a 3d Mesh's vertices informations. 
            -[type : string                              ] name : name of save file.
            -[type : string                              ] path : default is current dir's absolute path.
        ---------------------------------------------------------------------------------------------
        =========return arguments====================================================================
            -None
        ---------------------------------------------------------------------------------------------
        """
        pass
