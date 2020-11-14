import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode([800, 800])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((150, 150, 150))
        pygame.draw.circle(window, (255, 0, 0), (400, 400), 100)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()