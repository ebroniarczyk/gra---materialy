import pygame

pygame.init()

surface = pygame.display.set_mode((640, 480))

walk = (pygame.image.load('game\\Images\\Lemming\\walk1.png'),
                pygame.image.load('game\\Images\\Lemming\\walk2.png'),
                pygame.image.load('game\\Images\\Lemming\\walk3.png'),
                pygame.image.load('game\\Images\\Lemming\\walk4.png'))


frame = 1 # klatka
clock = pygame.time.Clock() 

running = True
while running:
    clock.tick(10) # ogranicza szybkosc petli do 10 klatek na sekunde; mierzy czas od ostatniego tika (i go zwraca)

    surface.fill(0) # wypelnienie czarnym tlem przed narysowaniem postaci (przed kazda klatka)

    image = pygame.transform.scale(walk[frame], (30,50)) # powiekszenie obrazka (w oryginale bardzo maly)
    surface.blit(image, (100,100)) # narysowanie obrazka na powierzchni
    frame = (frame + 1) % len(walk) # aktualizacja klatki

    pygame.display.update() # aktualizacja widoku w aplikacji

    events = pygame.event.get() # wylaczanie aplikacji
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False