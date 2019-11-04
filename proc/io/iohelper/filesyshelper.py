#################################################################################################
#                                   filesyshelper.py
#
#
#
#################################################################################################


import os



class FileSystemHelper():
    """
        Class FileSystemHelper


    """

    def __init__(self):
        self.root_path = self.curdir = os.path.abspath(os.path.curdir)
        #self.file_name_pattern = None


    def setWorkingDir(self, path):
        """
            input args
                -path

            return values
                - None
        """
        self.root_path = self.curdir = os.path.abspath(path)


    def getPwd(self, is_abs: bool = True ):
        """
        input args
            - None

        return value
            - return current directory as a absolute path
        """
        self.curdir = (os.path.abspath(os.path.curdir))
        return  (os.path.abspath(os.path.curdir)) if is_abs == True else os.path.curdir

    def getDirList(self, path = None):
        """
            if path is None. considering current dir path.
            input args
                -path ( type : string ) : default is None. 

            return value
                - return current directory filename list. not that absolute path. it includes child directory and files.
        """
        if path == None : 
            path = self.curdir
        os.listdir(path)
        return 
    

    def nextFile(self, path=None, isRecursive = False):
        """
            using when iterate working. 
            input args
                path ( type : string ) : default value is curdir
            return value
                filename(type : string) : diretory's child files that owns path
        """
        if path == None : 
            pass
        
        
        if not os.path.exists(path):
           return Exception("path doesn't exists.")
        
        

    #TODO
    def make_filename(self, pattern):
        return "for the nothing"





