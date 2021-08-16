
class ValuesForInit:
    def __init__(self, _tEnemyPos, _tPlayerPos, _tCoronaPos):
        self.tInitEnemyPos = _tEnemyPos
        self.tInitPlayerPos = _tPlayerPos
        self.tInitCovidPos = _tCoronaPos


class TextOutput:
    def __init__(self, _sGameOver, _sPlayAgain, _sEnd):
        self.tGameOverTextOutput = (_sGameOver, _sPlayAgain, _sEnd)
        self.tEndGameTextOutput = (_sGameOver[_sGameOver.find('!') + 2: len(_sGameOver)],
                                   _sPlayAgain, _sEnd)
