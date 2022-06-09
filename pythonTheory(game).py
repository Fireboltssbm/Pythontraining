import pygame

pygame.init()

width = 800
height = 800
white_color = (255, 255, 255)

game_window = pygame.display.set_mode((width,height))

clock.pygame.time.Clock()

background_image = pygame.image.load('assets/background.png')


def run_game_loop():
    while True:
    # handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
    # execute logic
    # update display
        game_window.fill(white_color)
        game_window.blit(background_image, (0,0))
        pygame.display.update()
    
        clock.tick(600)
        
run_game_loop()

pygame.quit()

quit()