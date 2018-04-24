import os

class FileProvider:
    workingDir = os.getcwd()

    def getFontFile(fileName):
        return FileProvider.workingDir+"/Font/"+fileName
