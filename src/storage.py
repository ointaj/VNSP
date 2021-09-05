import os.path


class cFileMethods:
    def __init__(self):
        self.Append = "a"
        self.Write = "w"
        self.Read = "r"


class cFileExtension:
    def __init__(self):
        self.TxtExt = ".txt"
        self.CsvExt = ".csv"


class cBStorage:

    def FileNameCheck(self):
        pass

    def CreateFolder(self):
        pass

    def CreateFile(self, _sScore, _sPlayerName):
        pass


class cStorage(cBStorage):
    def __init__(self, _sFileName, _sDelimeter):
        self.sFileName = _sFileName
        self.sDelimeter = _sDelimeter

        self.CurrentDirectory = os.getcwd()
        self.sDirName = 'Storage/'
        self.NewDir = os.path.join(self.CurrentDirectory, r'Storage')

        self.bAppendFlag = True

        self.oFileMethods = cFileMethods()
        self.oFileExtension = cFileExtension()

    def FileNameCheck(self):
        PosOfExt = self.sFileName.find(".")
        if PosOfExt != -1:
            if self.sFileName[PosOfExt:len(self.sFileName)] == self.oFileExtension.TxtExt:
                return True
            else:
                return False
        else:
            return False

    def CreateFolder(self):
        if not os.path.exists(self.NewDir):
            try:
                os.makedirs(self.NewDir)
            except:
                print("Error of creating storage for game !")
                exit()

    def CreateFile(self, _sScore, _sPlayerName):
        if self.FileNameCheck():
            try:
                file = open(self.sDirName + self.sFileName, self.oFileMethods.Append)
                try:
                    file.write(_sScore + self.sDelimeter + _sPlayerName + '\n')
                except:
                    print("Can't write to file")
                finally:
                    file.close()
            except:
                print("File can't be open")
        self.bAppendFlag = False
