import pygame
import sys

class cBTextInput:

    def InputText(self):
        pass

    def InputTextFlip(self):
        pass


class cTextInput(cBTextInput):
    def __init__(self, _tRectValue, _defColor, _pgScreen, _Font):

        self.tRectValue = _tRectValue
        self.sDefColor = _defColor
        self.pgScreen = _pgScreen
        self.Font = _Font

        self.Clock = pygame.time.Clock()
        self.InputRectangle = pygame.Rect(*self.tRectValue)
        self.sUserName = ''

        self.Color = pygame.Color(self.sDefColor)

    def InputText(self):

        pygame.draw.rect(self.pgScreen, self.Color, self.InputRectangle)

        textPrint = self.Font.render(self.sUserName, True, (255, 255, 255))

        self.pgScreen.blit(textPrint, (self.InputRectangle.x + 10, self.InputRectangle.y + 10))

        self.InputRectangle.w = max(150, textPrint.get_width() + 10)

        self.InputTextFlip()

        self.Clock.tick(60)

    def InputTextFlip(self):
        pygame.display.flip()




