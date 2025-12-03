import pygame

#Set up pygame
pygame.init()
screen =  pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load('mapConcept.png')

font = pygame.font.Font('smallCake.otf', 20)

text = font.render('Coins: ', True, 'yellow', 'black')
textRect = text.get_rect()

textRect.center = (1600, 150)

#sets player position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill("black")

        player = pygame.image.load("tempCharU.png").convert_alpha() #temp for player sprite
        screen.blit(background, (0, 0))
        screen.blit(player, (player_pos))
        screen.blit(text, textRect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 10
        if keys[pygame.K_s]:
            player_pos.y += 10
        if keys[pygame.K_a]:
            player_pos.x -= 10
        if keys[pygame.K_d]:
            player_pos.x += 10
        if keys[pygame.K_ESCAPE]:   #Close game when ESC is pressed
            running = False

        pygame.display.flip()

        #limits FPS to 60
        #dt is delta time in seconds since last frame, used for framerate independent physics
        dt = clock.tick(60)

pygame.quit()