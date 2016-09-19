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
        self.colors = [ (244,211,167), (165,71,20) ]
        self.sprites = {
           'p' : pygame.image.load("resources/png/pawn_black.png").convert_alpha(),
           'n' : pygame.image.load("resources/png/knight_black.png").convert_alpha(),
           'b' : pygame.image.load("resources/png/bishop_black.png").convert_alpha(),
           'r' : pygame.image.load("resources/png/rook_black.png").convert_alpha(),
           'q' : pygame.image.load("resources/png/queen_black.png").convert_alpha(),
           'k' : pygame.image.load("resources/png/king_black.png").convert_alpha(),
           'P' : pygame.image.load("resources/png/pawn_white.png").convert_alpha(),
           'N' : pygame.image.load("resources/png/knight_white.png").convert_alpha(),
           'B' : pygame.image.load("resources/png/bishop_white.png").convert_alpha(),
           'R' : pygame.image.load("resources/png/rook_white.png").convert_alpha(),
           'Q' : pygame.image.load("resources/png/queen_white.png").convert_alpha(),
           'K' : pygame.image.load("resources/png/king_white.png").convert_alpha()
        }

        self.reset()

    def reset(self):
        self.board = [
            'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
            'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
            'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 
            'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

    def render(self):
        for i in range(8):
            for j in range(8):
                r = (self.ofsX + j*self.w, self.ofsY + i*self.h, self.w, self.h)
                pygame.draw.rect(screen, self.colors[(i+j) % 2], r)
                piece = self.board[i*8+j]
                if piece != ' ':
                    screen.blit(self.sprites[piece], r)


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
