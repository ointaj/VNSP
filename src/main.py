import pygame
import random
import math

pygame.init()


class cBEntity:

    def FlagInit(self):
        pass

    def PrintEntity(self, tEnPos, entityImage):
        pass

    def PlayerPos(self):
        pass

    def EnemyPos(self):
        pass

    def PosInit(self, EntityPos, ValuesForInit, PosDiff):
        pass

    def newEnemyPosInit(self):
        pass

    def FireVaccine(self, Image):
        pass

    def EnemyDestroyed(self):
        pass

    def GetInfected(self):
        pass

    def ScoreCounter(self):
        pass


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

    def EndThread(self):
        pass


class ValuesForInit:
    def __init__(self, _tEnemyPos, _tPlayerPos, _tCoronaPos):
        self.tInitEnemyPos = _tEnemyPos
        self.tInitPlayerPos = _tPlayerPos
        self.tInitCovidPos = _tCoronaPos


class cEntity(cBEntity):
    def __init__(self, pyScreen):
        self.Screen = pyScreen
        self.FlagMovement = []

        self.EnemyPosDiff = 3
        self.PlayerPosDiff = 1
        self.CoronaPosDiff = 4

        self.PositionChange = 0
        self.ScoreValue = 0

        self.initNewEnemy = []

        self.lEnemyPos = []
        self.lPlayerPos = []
        self.tVaccinePos = []
        self.tCovidePos = []

        self.bFireVaccine = []
        self.Collision = 50

        self.bGetInfection = False

    def FlagInit(self):
        for it in range(self.EnemyPosDiff):
            self.FlagMovement.append(True)
            self.initNewEnemy.append(False)

    def PrintEntity(self, tEnPos, entityImage):
        for playPos in tEnPos:
            self.Screen.blit(entityImage, playPos)

    def FireVaccine(self, Image):
        count = 0
        if not self.bFireVaccine:
            return
        for it in self.tVaccinePos:
            count += 1
            if not self.bFireVaccine[count - 1]:
                continue
            else:
                it[1] -= 0.5
                self.Screen.blit(Image, it)

    def PlayerPos(self):
        for it in self.lPlayerPos:
            it[0] += self.PositionChange
            if it[0] <= 0:
                it[0] = 0
            elif it[0] >= 940:
                it[0] = 940

    def EnemyPos(self):
        for fIt, sIt in zip(self.lEnemyPos, range(len(self.FlagMovement))):
            if fIt[1] >= 500:
                self.initNewEnemy[sIt] = True
            if fIt[0] >= 940:
                self.FlagMovement[sIt] = False
                fIt[1] += 30
            elif fIt[0] <= 0:
                self.FlagMovement[sIt] = True
                fIt[1] += 30

            if self.FlagMovement[sIt]:
                fIt[0] += 0.3
            else:
                fIt[0] -= 0.3

    def EnemyDestroyed(self):
        count = 0
        if not self.tVaccinePos:
            return
        for enemyIt in self.lEnemyPos:
            count += 1
            for vacPos in self.tVaccinePos:
                collision = math.sqrt((math.pow(enemyIt[0] - vacPos[0], 2)) + (math.pow(enemyIt[1] - vacPos[1], 2)))
                if collision < self.Collision:
                    self.initNewEnemy[count - 1] = True
                    self.ScoreValue += 1

    def GetInfected(self):
        for playerIt in self.lPlayerPos:
            for enemyIt in self.lEnemyPos:
                infection = math.sqrt((math.pow(playerIt[0] - enemyIt[0], 2)) + (math.pow(playerIt[1] - enemyIt[1], 2)))
                if infection < self.Collision:
                    self.bGetInfection = True

    def newEnemyPosInit(self):
        for it in range(len(self.initNewEnemy)):
            if self.initNewEnemy[it]:
                self.lEnemyPos[it] = ([random.randint(0, 1000), random.randint(50, 250)])
                self.initNewEnemy[it] = False

    def PosInit(self, EntityPos, tValuesForInit, PosDiff):
        for it in range(PosDiff):
            EntityPos.append([random.randint(*tValuesForInit[0]), random.randint(*tValuesForInit[1])])


class cMain(cBMain):
    def __init__(self, iHeightScreenV, iWidthScreenV, sPlayerImage, sEnemyImage, sVaccineImage, sCovidImage):

        self.iHeiVal = iHeightScreenV
        self.iWidVal = iWidthScreenV

        self.bRunning = True

        self.PlayerImage = pygame.image.load(sPlayerImage)
        self.EnemyImage = pygame.image.load(sEnemyImage)
        self.VaccineImage = pygame.image.load(sVaccineImage)
        self.CovidImage = pygame.image.load(sCovidImage)

        self.ScoreFont = pygame.font.SysFont(None, 32)

        self.lImage = (self.PlayerImage, self.EnemyImage)

        self.pgScreen = pygame.display.set_mode((iHeightScreenV, iWidthScreenV))

        self.oEntity = cEntity(self.pgScreen)
        self.oInitPos = ValuesForInit([(0, 1000), (50, 250)], [(430, 460), (490, 510)], [(0, 1000), (50, 250)])

    def ShowScore(self):
        scorePrint = self.ScoreFont.render("You vaccinated : " + str(self.oEntity.ScoreValue) + " Nazis !",
                                           True, (0, 0, 0))
        self.pgScreen.blit(scorePrint, ((self.iWidVal / 2) + 40, 10))

    def GUI(self):
        pygame.display.set_caption("Kill nazi")
        icon = pygame.image.load('antifa.png')
        pygame.display.set_icon(icon)

    def FillScreen(self):
        self.pgScreen.fill((255, 255, 255))

    def Init(self):
        self.oEntity.PosInit(self.oEntity.lEnemyPos, self.oInitPos.tInitEnemyPos, self.oEntity.EnemyPosDiff)
        self.oEntity.PosInit(self.oEntity.lPlayerPos, self.oInitPos.tInitPlayerPos, self.oEntity.PlayerPosDiff)
        self.oEntity.FlagInit()

    def InitEndEntity(self):
        self.oEntity.PosInit(self.oEntity.tCovidePos, self.oInitPos.tInitCovidPos, self.oEntity.CoronaPosDiff)
        lPrintValue = (self.CovidImage, self.oEntity.tCovidePos)
        return lPrintValue

    def Event(self):
        for event in pygame.event.get():
            if not self.oEntity.bGetInfection:
                self.KeyboardInput(event)
            else:
                self.EndKeyboardInput(event)

    def UpdateScreen(self):
        pygame.display.update()

    def Entity(self, lValues):
        for it in lValues:
            self.oEntity.PrintEntity(it[1], it[0])

    def KeyboardInput(self, _allEvents):
        if _allEvents.type == pygame.QUIT:
            self.bRunning = False
        if _allEvents.type == pygame.KEYDOWN:
            if _allEvents.key == pygame.K_ESCAPE:
                self.bRunning = False
            if _allEvents.key == pygame.K_LEFT:
                self.oEntity.PositionChange = -1
                return
            if _allEvents.key == pygame.K_RIGHT:
                self.oEntity.PositionChange = 1
                return
            if _allEvents.key == pygame.K_SPACE:
                self.oEntity.bFireVaccine.append(True)
                self.oEntity.tVaccinePos.append([self.oEntity.lPlayerPos[0][0], self.oEntity.lPlayerPos[0][1]])
            # Test #
            if _allEvents.key == pygame.K_1:
                self.oEntity.bGetInfection = True
            # ---- #
        self.oEntity.PositionChange = 0

    def EndKeyboardInput(self, _allEvents):
        if _allEvents.type == pygame.QUIT:
            self.oEntity.bGetInfection = False
            self.bRunning = False

        if _allEvents.type == pygame.KEYDOWN:
            if _allEvents.key == pygame.K_ESCAPE:
                self.oEntity.bGetInfection = False
                self.bRunning = False
            elif _allEvents.key == pygame.K_RETURN:
                self.oEntity.ScoreValue = 0
                self.oEntity.bGetInfection = False

    def EndThread(self):
        if self.oEntity.bGetInfection:
            lPrintValues = self.InitEndEntity()
            while self.oEntity.bGetInfection:
                self.Event()
                self.pgScreen.fill((255, 255, 255))
                self.oEntity.PrintEntity(lPrintValues[1], lPrintValues[0])
                scorePrint = self.ScoreFont.render("Dumb nazi infected you ! Your score is: "
                                                   +
                                                   str(self.oEntity.ScoreValue),
                                                   True, (0, 0, 0))
                self.pgScreen.blit(scorePrint, ((self.iWidVal / 2) - 10, (self.iHeiVal / 2) - 40))
                self.UpdateScreen()

    def SetFlag(self):
        count = 0
        if not self.oEntity.bFireVaccine:
            return
        for it in self.oEntity.tVaccinePos:
            count += 1
            if it[1] <= 0:
                self.oEntity.bFireVaccine[count - 1] = False

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
            self.SetFlag()
            self.Entity(lPrintValues)
            self.oEntity.newEnemyPosInit()
            self.ShowScore()
            self.UpdateScreen()
            self.oEntity.GetInfected()
            self.EndThread()
            self.UpdateScreen()


if __name__ == "__main__":
    Main = cMain(1000, 600, 'antifa.png', 'naziscum.png', 'vac.png', 'covid.png')
    Main.MainFunction()
