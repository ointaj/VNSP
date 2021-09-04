from entity import *
from values import *
import pygame
pygame.init()


class cBMain:

    def GUI(self):
        pass

    def FillScreen(self):
        pass

    def Init(self):
        pass

    def InitEndEntity(self):
        pass

    def Event(self):
        pass

    def MainFunction(self):
        pass

    def StartKeyboardInput(self, allEvents):
        pass

    def KeyboardInput(self, _allEvents):
        pass

    def EndKeyboardInput(self, _allEvents):
        pass

    def UpdateScreen(self):
        pass

    def Entity(self, lValues):
        pass

    def SetFlag(self):
        pass

    def ShowScore(self):
        pass

    def EndTextPos(self, lLoopValue):
        pass

    def PrintEndInfo(self, EndValue):
        pass

    def StartThread(self):
        pass

    def EndThread(self):
        pass

    def DeallocatedVaccinePos(self):
        pass


class cMain(cBMain):
    def __init__(self, iHeightScreenV, iWidthScreenV, sPlayerImage, sEnemyImage, sVaccineImage, sCovidImage):

        self.iHeiVal = iHeightScreenV
        self.iWidVal = iWidthScreenV

        self.bStartRunning = False # Will be true, now its only because of not using it
        self.bRunning = True
        self.bEndRunning = False
        self.bPause = False  # pause break

        self.PlayerImage = pygame.image.load(sPlayerImage)
        self.EnemyImage = pygame.image.load(sEnemyImage)
        self.VaccineImage = pygame.image.load(sVaccineImage)
        self.CovidImage = pygame.image.load(sCovidImage)

        self.ScoreFont = pygame.font.SysFont(None, 32)

        self.lImage = (self.PlayerImage, self.EnemyImage)

        self.pgScreen = pygame.display.set_mode((iHeightScreenV, iWidthScreenV))

        self.RenderValue = (0, 0, 0)
        self.lPrintValues = ()

        self.oEntity = cEntity(self.pgScreen)
        self.oInitPos = ValuesForInit([(0, 1000), (50, 250)], [(430, 460), (490, 510)],
                                      [(0, 1000), (50, 250)])
        self.oTextOutput = TextOutput("Dumb nazi infected you ! Your score is: ",
                                      "Press Enter to start again ! ",
                                      "Press Esc to end game ! ")

    def ShowScore(self):
        scorePrint = self.ScoreFont.render("You vaccinated : " + str(self.oEntity.ScoreValue) + " Nazis !",
                                           True, (0, 0, 0))
        self.pgScreen.blit(scorePrint, ((self.iWidVal / 2) + 40, 10))

    def GUI(self):
        pygame.display.set_caption("VNSP")
        icon = pygame.image.load('Images/antifa.png')
        pygame.display.set_icon(icon)

    def FillScreen(self):
        self.pgScreen.fill((255, 255, 255))

    def Init(self):
        self.oEntity.PosInit(self.oEntity.lEnemyPos, self.oInitPos.tInitEnemyPos, self.oEntity.EnemyPosDiff)
        self.oEntity.PosInit(self.oEntity.lPlayerPos, self.oInitPos.tInitPlayerPos, self.oEntity.PlayerPosDiff)
        self.oEntity.FlagInit()

    def InitEndEntity(self):
        self.oEntity.PosInit(self.oEntity.tCovidePos, self.oInitPos.tInitCovidPos, self.oEntity.CoronaPosDiff)
        self.lPrintValues = (self.CovidImage, self.oEntity.tCovidePos)

    def Event(self):
        for event in pygame.event.get():
            if self.bStartRunning:
                self.StartKeyboardInput(event)
            if not self.oEntity.bGetInfection and not self.bEndRunning:
                self.KeyboardInput(event)
            else:
                self.EndKeyboardInput(event)

    def UpdateScreen(self):
        pygame.display.update()

    def Entity(self, lValues):
        for it in lValues:
            self.oEntity.PrintEntity(it[1], it[0])

    def StartKeyboardInput(self, _allEvents):
        if _allEvents.type == pygame.QUIT:
            self.bStartRunning = False
            self.bRunning = False
        if _allEvents.type == pygame.KEYDOWN:
            if _allEvents.key == pygame.K_ESCAPE:
                self.bStartRunning = False
                self.bRunning = False

    def KeyboardInput(self, _allEvents):
        if _allEvents.type == pygame.QUIT:
            self.bRunning = False
        if _allEvents.type == pygame.KEYDOWN:
            if _allEvents.key == pygame.K_ESCAPE:
                self.bEndRunning = True
                return
            if _allEvents.key == pygame.K_LEFT:
                self.oEntity.PositionChange = -1
                return
            if _allEvents.key == pygame.K_RIGHT:
                self.oEntity.PositionChange = 1
                return
            if _allEvents.key == pygame.K_SPACE:
                if not self.oEntity.tVaccinePos:
                    self.oEntity.tVaccinePos.append([self.oEntity.lPlayerPos[0][0], self.oEntity.lPlayerPos[0][1]])
                    return
                for it, index in zip(self.oEntity.tVaccinePos, range(len(self.oEntity.tVaccinePos))):
                    if len(it) == 0:
                        self.oEntity.tVaccinePos[index] = ([self.oEntity.lPlayerPos[0][0], self.oEntity.lPlayerPos[0][1]])
                        return
                self.oEntity.tVaccinePos.append([self.oEntity.lPlayerPos[0][0], self.oEntity.lPlayerPos[0][1]])
                return
            # Test #
            if _allEvents.key == pygame.K_1:
                self.oEntity.bGetInfection = True
                return
            # ---- #
        self.oEntity.PositionChange = 0

    def EndKeyboardInput(self, _allEvents):
        if _allEvents.type == pygame.QUIT:
            self.bRunning = False
            self.oEntity.bGetInfection = False
            self.bEndRunning = False
        if _allEvents.type == pygame.KEYDOWN:
            if _allEvents.key == pygame.K_ESCAPE:
                self.oEntity.bGetInfection = False
                self.bEndRunning = False
                self.bRunning = False
            elif _allEvents.key == pygame.K_RETURN:
                self.oEntity.ScoreValue = 0
                self.oEntity.bGetInfection = False
                self.bEndRunning = False

    def EndTextPos(self, lLoopValue):
        heightValue = (self.iHeiVal / 2) - 40
        posChange = 0
        for _lLoopValue, _range in zip(lLoopValue, range(len(lLoopValue))):
            widthValue = (self.iWidVal / 2) - 10
            if _range > 0:
                widthValue += len(self.oTextOutput.tGameOverTextOutput[0]) + posChange
                posChange += 20
            self.pgScreen.blit(_lLoopValue, (widthValue, heightValue))
            heightValue += 40

    def PrintEndInfo(self, EndValue):
        lLoopValue = []
        for textValue, _range in zip(EndValue, range(len(self.oTextOutput.tGameOverTextOutput))):
            if _range == 0:
                lLoopValue.append(self.ScoreFont.render(textValue
                                                        +
                                                        str(self.oEntity.ScoreValue),
                                                        True, self.RenderValue))
            else:
                lLoopValue.append(self.ScoreFont.render(textValue,
                                                        True, self.RenderValue))

        self.EndTextPos(lLoopValue)

    def StartThread(self):
        if self.bStartRunning:
            while self.bStartRunning:
                self.Event()
                self.pgScreen.fill((255, 255, 255))
            self.bStartRunning = False

    def EndThread(self):
        if self.oEntity.bGetInfection or self.bEndRunning:
            self.InitEndEntity()
            while self.oEntity.bGetInfection or self.bEndRunning:
                self.Event()
                self.pgScreen.fill((255, 255, 255))
                if self.oEntity.bGetInfection:
                    self.oEntity.PrintEntity(self.lPrintValues[1], self.lPrintValues[0])
                    self.PrintEndInfo(self.oTextOutput.tGameOverTextOutput)
                    self.bStartRunning = True
                elif self.bEndRunning:
                    self.oEntity.PrintEntity(self.lPrintValues[1], self.lPrintValues[0])
                    self.PrintEndInfo(self.oTextOutput.tEndGameTextOutput)
                self.UpdateScreen()
            self.oEntity.SetNewEnemyInit()
            self.oEntity.newEnemyPosInit()
            self.oEntity.tCovidePos = []
            self.lPrintValues = ()

    def DeallocatedVaccinePos(self):
        count = 0
        for VaccinePos in self.oEntity.tVaccinePos:
            if len(VaccinePos) == 0:
                count += 1
        if count == len(self.oEntity.tVaccinePos):
            self.oEntity.tVaccinePos = []
        for VaccinePos, index in zip(self.oEntity.tVaccinePos, range(len(self.oEntity.tVaccinePos))):
            if len(VaccinePos) == 0:
                continue
            elif VaccinePos[1] <= 0:
                self.oEntity.tVaccinePos[index] = []

    def MainFunction(self):
        self.Init()
        self.GUI()
        while self.bRunning:
            self.Event()
            self.FillScreen()
            self.oEntity.PlayerPos()
            self.oEntity.EnemyPos()
            self.oEntity.EnemyDestroyed()
            lPrintValues = (self.PlayerImage, self.oEntity.lPlayerPos), (self.EnemyImage, self.oEntity.lEnemyPos)
            self.oEntity.FireVaccine(self.VaccineImage)
            self.DeallocatedVaccinePos()
            self.Entity(lPrintValues)
            self.oEntity.newEnemyPosInit()
            self.ShowScore()
            self.UpdateScreen()
            self.oEntity.GetInfected()
            self.EndThread()
            self.UpdateScreen()
