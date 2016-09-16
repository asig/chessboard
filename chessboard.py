#!/usr/bin/env python

import sys, pygame

WIDTH = 480
HEIGHT = 800

class Board:
    global screen

    def __init__(self):
        self.w = 40
        self.h = 40
        self.ofsX = (WIDTH - 8*self.w)/2
        self.ofsY = self.ofsX

    def render(self):
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(screen, (128,128,128), (self.ofsX + j*self.w, self.ofsY + i*self.h, self.w, self.h))


class Game:
    def __init__(self):
        self.board = Board()
        self.clock = pygame.time.Clock()

        # self.speed = [1, 1]
        # self.black = 0, 122, 0
        # self.ball = pygame.image.load("ball.png").convert_alpha()
        # self.background = pygame.image.load("low_poly-wallpaper-480x800.jpg")
        # self.ballrect = self.ball.get_rect()

    def gameLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.board.render()

            # self.ballrect = self.ballrect.move(self.speed)
            # if self.ballrect.left < 0 or self.ballrect.right > self.WIDTH:
            #     self.speed[0] = -self.speed[0]
            # if self.ballrect.top < 0 or self.ballrect.bottom > self.HEIGHT:
            #     self.speed[1] = -self.speed[1]

            # self.screen.blit(self.background, self.background.get_rect())
            # self.screen.blit(self.ball, self.ballrect)

            self.clock.tick_busy_loop(60)
            pygame.display.flip()

if __name__ == "__main__":
    global screen

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    game = Game()
    game.gameLoop()
