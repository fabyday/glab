import json
import os

__gFileName = "progsetting"
class ArgumentFinder:

    """
    Class ArgumentFinder

    ArgumentFinder read JSON type Setting files.
    if you didn't give setting file name.
    ArgumentFinder finds default name("progsetting")

    """
    def __init__(self, env):
        self.env = env
        


    
    def readSetting(self, fileName = __gFileName ):
        """
        read setting files that was wrote by "JSON" type.
        if file was carshed or wrong. it return empty dict.
        method finds setting file in current directory first.
        input args :
            fileName : setting file name. default is "progsetting".
        return valeus : 
            data (type : dict) : parsed json files.
        """
        if os.path.exists(fileName) : 
            data = json.loads(fileName)
        else : 
            raise Exception("Files not found")
        return data


    @DeprecationWarning
    def writeSetting(self, settings = dict(), fileName = __gFileName, permitOverlap = False):
        tmp_number = 0
        if permitOverlap == True : 
            while os.path.exists(fileName):
                ''.join([fileName, tmp_number])
                tmp_number += 1
                
        print("save setting files in " + os.path.curdir+'/'+fileName)
        with open(fileName, 'w') as f : 
            json.dumps(settings, fp = f, indent = 4)
            print(settings)

    def writeTemplate(self, fineName= __gFileName):
        args = dict()
        args['epochs'] = 200
        args['testSize'] = 200
        with open(fineName, 'w') as f:
            json.dumps(args, fp = f, indent=4)

    def __writeSetting(self):
        pass




if __name__ == "__main__":
    af = ArgumentFinder("test")
    af.writeSetting()



    


    
