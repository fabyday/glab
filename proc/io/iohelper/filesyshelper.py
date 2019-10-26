import os


class FileSystemHelper():
    def __init__(self):
        self.root_path = self.curdir = os.path.abspath(os.path.curdir)
        #self.file_name_pattern = None

    def pwd(self, is_abs: bool = True ):
        self.curdir = (os.path.abspath(os.path.curdir))
        return  (os.path.abspath(os.path.curdir)) if is_abs == True else os.path.curdir

    
    def recursive_iterator(self, path):
        if not os.path.exists(path):
           return Exception("path doesn't exists.") 
    
    def make_filename(self, pattern):
        return "for the nothing"





