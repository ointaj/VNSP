import os
from messages import *
from stringhelper import *


class cFileMethods:
    def __init__(self):
        self.Append = "a"
        self.Write = "w"
        self.Read = "r"


class cFileExtension:
    def __init__(self):
        self.Ext = (".txt", ".csv")


class cBStorage:

    def FileNameCheck(self):
        pass

    def FileEmpty(self):
        pass

    def FileLines(self):
        pass

    def CheckFileForOverwrite(self, UserName, Score):
        pass

    def CreateFolder(self):
        pass

    def CreateFile(self, _sScore, _sPlayerName):
        pass

    def CreateSortedScore(self):
        pass


class cStorage(cBStorage):
    def __init__(self, _sFileName, _sDelimeter):
        self.sFileName = _sFileName
        self.sDelimeter = _sDelimeter

        self.CurrentDirectory = os.getcwd()
        self.sDirName = 'Storage/'
        self.NewDir = os.path.join(self.CurrentDirectory, r'Storage')
        self.LinesOfFileContent = []

        self.oFileMethods = cFileMethods()
        self.oFileExtension = cFileExtension()
        self.oStringHelper = cStringHelper()

    def CreateSortedScore(self):
        ScoreValues = []

        for fileContent in self.LinesOfFileContent:
            delimeterPos = fileContent.find(self.sDelimeter)
            Score = fileContent[0:delimeterPos]
            ScoreValues.append(Score)

        ScoreValues.sort()

        FileContent = []

        for Score in range(len(ScoreValues)):
            for LineInFile in self.LinesOfFileContent:
                delimeterPos = LineInFile.find(self.sDelimeter)
                if Score == LineInFile[0:delimeterPos]:
                    FileContent.append(LineInFile)
                    break

        return FileContent

    def FileNameCheck(self):
        PosOfExt = self.sFileName.find(".")
        if PosOfExt != -1:
            for Extension in self.oFileExtension.Ext:
                if self.sFileName[PosOfExt:len(self.sFileName)] == Extension:
                    return True
            return False
        else:
            return False

    def FileEmpty(self):
        if not os.path.exists(self.sDirName + self.sFileName):
            return True
        return os.stat(self.sDirName + self.sFileName).st_size == 0

    def FileLines(self):
        try:
            file = open(self.sDirName + self.sFileName, self.oFileMethods.Read)
            self.LinesOfFileContent = file.readlines()
            file.close()
        except:
            cErrorMessages.CantOpenFile()

    def CheckFileForOverwrite(self, UserName, Score):
        charValue = self.oStringHelper.IsRemovelNeeded(UserName)
        if charValue:
            UserName = self.oStringHelper.StringFormat(UserName, charValue)
        self.FileLines()
        for FileLine, it in zip(self.LinesOfFileContent, range(len(self.LinesOfFileContent))):
            DelPos = FileLine.find(self.sDelimeter)
            if UserName == str(FileLine[DelPos + 1:len(FileLine) - 1]):
                if Score == FileLine[0:DelPos]:
                    return True, False
                else:
                    self.LinesOfFileContent[it] = FileLine.replace(FileLine[0:DelPos], Score)
                    return True, True
        return False, False

    def CreateFolder(self):
        if not os.path.exists(self.NewDir):
            try:
                os.makedirs(self.NewDir)
            except:
                cErrorMessages.StorageError()
                exit()

    def CreateFile(self, _sScore, _sPlayerName):
        if not self.FileEmpty():
            Exists, ChangedContent = self.CheckFileForOverwrite(_sPlayerName, _sScore)
            if Exists and not ChangedContent:
                return
            elif ChangedContent:
                try:
                    file = open(self.sDirName + self.sFileName, self.oFileMethods.Write)
                    try:
                        for fileContent in self.LinesOfFileContent:
                            file.write(fileContent)
                    except:
                        cErrorMessages.CantWriteToFile()
                    finally:
                        file.close()
                except:
                    cErrorMessages.CantOpenFile()
                return
        if self.FileNameCheck():
            try:
                file = open(self.sDirName + self.sFileName, self.oFileMethods.Append)
                try:
                    file.write(_sScore + self.sDelimeter + _sPlayerName)
                except:
                    cErrorMessages.CantWriteToFile()
                finally:
                    file.close()
            except:
                cErrorMessages.CantOpenFile()
