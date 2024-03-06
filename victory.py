import  pygame
import os

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image
def give_victory(player):
    pygame.init()
    infoObject = pygame.display.Info()
    size = width, height = infoObject.current_w, infoObject.current_h - 10
    screen = pygame.display.set_mode(size)
    print("winner" + str(player))
    screen.fill((0, 0, 0))
    f = pygame.font.Font(None, width // 13)
    text = f.render(f'Победил игрок {player}!', True,
                    (255, 255, 255))
    screen.blit(text, (width * 0.25, height * 0.67))
    king = load_image(f"king_mouse{player}.png")
    king = pygame.transform.scale(king, (width // 3, height // 2))
    screen.blit(king, (width // 3, 10))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                running = False
                return 'ok'
    pygame.quit()