import os.path


class cFileMethods:
    def __init__(self):
        self.Append = "a"
        self.Write = "w"
        self.Read = "r"


class cBStroage:

    def CreateFolder(self):
        pass

    def CreateFile(self, _sScore, _sPlayerName):
        pass


class cStorage(cBStroage):
    def __init__(self, _sFileName, _sDelimeter):
        self.sFileName = _sFileName
        self.sDelimeter = _sDelimeter

        self.CurrentDirectory = os.getcwd()
        self.NewDir = os.path.join(self.CurrentDirectory, r'Storage')

        self.bAppendFlag = True

        self.oFileMethods = cFileMethods()

    def CreateFolder(self):
        if not os.path.exists(self.NewDir):
            os.makedirs(self.NewDir)

    def CreateFile(self, _sScore, _sPlayerName):
        file = open(self.sFileName, self.oFileMethods.Append)
        file.write(_sScore + self.sDelimeter + _sPlayerName + '\n')
        file.close()
        self.bAppendFlag = False

