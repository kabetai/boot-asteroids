import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x,y)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    # you have to put comma after single item in tuple, 
    # otherwise Python won't recognize it as a tuple
    AsteroidField.containers = (updatable,) 
    field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            collision = player.check_collision(asteroid)
            if(collision):
                print(f"Game over!")
                sys.exit()
            for bullet in shots:
                collision = bullet.check_collision(asteroid)
                if(collision):
                    asteroid.kill()
                    bullet.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
