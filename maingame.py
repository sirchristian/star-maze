import sys
import random
import pygame
from pygame.locals import *

import StarMazeSprites
from StarMazeSprites import *

def main():
    
    def move(direction):
        boy.rect.move_ip(direction)
        collisions = pygame.sprite.spritecollide(boy, starGroup, False)
        if len(collisions) > 0:
            star.rect.move_ip(direction)
        
    # setup the game
    pygame.init()
    gameSurface = pygame.display.set_mode((1024,786))
    gameRect = gameSurface.get_rect()
    pygame.display.set_caption('Fun game')
    pygame.key.set_repeat(1, 1)

    # create the backgound
    background = pygame.Surface(gameSurface.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # blit the background to the display
    gameSurface.blit(background, (0, 0))
    pygame.display.flip()

    # setup the boy
    boy = BoySprite(gameSurface)
    boy.rect = boy.rect.move(0, gameSurface.get_height()-boy.rect.height)
    boyGroup = pygame.sprite.GroupSingle(boy)

    # setup the star
    star = StarSprite(gameSurface)
    star.rect = star.rect.move(
        random.randint(0, gameSurface.get_width()),
        random.randint(0, gameSurface.get_height()))
    starGroup = pygame.sprite.GroupSingle(star)

    # game loop
    gameOver = False
    while not gameOver:
        
        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                gameOver = True
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and boy.rect.left > gameRect.left:
                    move((-1,0))
                elif event.key == K_RIGHT and boy.rect.right < gameRect.right:
                    move((1, 0))
                elif event.key == K_UP and boy.rect.top > gameRect.top:
                    move((0, -1))
                elif event.key == K_DOWN and boy.rect.bottom < gameRect.bottom:
                    move((0, 1))
                elif event.key == K_r:
                    # restart the game
                    return True

        # update UI
        gameSurface.blit(background, (0, 0))
        boyGroup.draw(gameSurface)
        starGroup.draw(gameSurface)
        pygame.display.flip()

    # return that we do not want to continue
    return False

if __name__ == "__main__":
    while main():
        pass
    pygame.quit()
    sys.exit()
