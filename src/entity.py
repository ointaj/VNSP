import random
import math


class cBEntity:

    def FlagInit(self):
        pass

    def PrintEntity(self, tEnPos, entityImage):
        pass

    def PlayerPos(self):
        pass

    def EnemyPos(self):
        pass

    def PosInit(self, EntityPos, tValuesForInit, PosDiff):
        pass

    def SetNewEnemyInit(self):
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

    def SetNewEnemyInit(self):
        for it in range(len(self.initNewEnemy)):
            self.initNewEnemy[it] = True

    def newEnemyPosInit(self):
        for it in range(len(self.initNewEnemy)):
            if self.initNewEnemy[it]:
                self.lEnemyPos[it] = ([random.randint(0, 1000), random.randint(50, 250)])
                self.initNewEnemy[it] = False

    def PosInit(self, EntityPos, tValuesForInit, PosDiff):
        for it in range(PosDiff):
            EntityPos.append([random.randint(*tValuesForInit[0]), random.randint(*tValuesForInit[1])])

