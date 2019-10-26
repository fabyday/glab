import json


__gFileName = "progsetting"
class ArgumentFinder:

    """
    Class ArgumentFinder

    ArgumentFinder read JSON type Setting files.
    if you didn't give setting file name.
    ArgumentFinder finds default name("progsetting")

    """
    def __init__(self):
        pass


    
    def readSetting(self, fileName = __gFileName ):
        """
        read setting files that was wrote by "JSON" type.
        if file was carshed or wrong. it return empty dict.
        method finds setting file in current directory first.
        input args :
            fileName : setting file name. default is "progsetting".
        return valeus : 
            dict : parsed json files.
        """
        pass


    @DeprecationWarning
    def saveSetting(self, settings, fileName = __gFileName):
        pass


    


    
