import pygame

#Set up pygame
pygame.init()
screen =  pygame.display.set_mode((0,0), pygame.FULLSCREEN|pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load('mapConcept.png').convert()
coinCount = 0
cropCount = 0
oxygen = 0
fuel = 0

font = pygame.font.Font('smallCake.otf', 20)

coinCountText = font.render(str(coinCount), 1, 'yellow', 'black')
cropCountText = font.render(str(cropCount), 1, 'green', 'black')
oxygenText = font.render(str(oxygen), 1, 'blue', 'black')
fuelCText = font.render(str(fuel), 1, 'orange', 'black')

textC = font.render('Coins: ', True, 'yellow', 'black')
textCrop = font.render('Crops: ', True, 'green', 'black')
textFuel = font.render('Fuel: ', True, 'orange', 'black')
textOx = font.render('Oxygen: ', True, 'blue', 'black')

coinsRect = textC.get_rect()
cropRect = textCrop.get_rect()
fuelCRect = textFuel.get_rect()
oxRect = textOx.get_rect()

coinsCountRect = coinCountText.get_rect()
cropCountRect = cropCountText.get_rect()
oxygenRect = oxygenText.get_rect()
fuelRect = fuelCText.get_rect()

coinsRect.center = (1450, 50)
cropRect.center = (1450, 75)
fuelRect.center = (1450, 100)
oxRect.center = (1450, 125)

coinsCountRect.center = (1530, 50)
cropCountRect.center = (1530, 75)
fuelCRect.center = (1550, 100)
oxygenRect.center = (1530, 125)

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
        screen.blit(textC, coinsRect)
        screen.blit(textCrop, cropRect)
        screen.blit(textFuel, fuelRect)
        screen.blit(textOx, oxRect)
        screen.blit(coinCountText, coinsCountRect)
        screen.blit(cropCountText, cropCountRect)
        screen.blit(fuelCText, fuelCRect)
        screen.blit(oxygenText, oxygenRect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 5
        if keys[pygame.K_s]:
            player_pos.y += 5
        if keys[pygame.K_a]:
            player_pos.x -= 5
        if keys[pygame.K_d]:
            player_pos.x += 5
        if keys[pygame.K_ESCAPE]:   #Close game when ESC is pressed
            running = False

        pygame.display.flip()

        #limits FPS to 60
        #dt is delta time in seconds since last frame, used for framerate independent physics
        dt = clock.tick(60)

pygame.quit()