import pygame
import os
import time
import random

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Коридор')
    infoObject = pygame.display.Info()
    width, height = infoObject.current_w, infoObject.current_h - 10
    print(width, height)
    screen = pygame.display.set_mode((width, height))
    pygame.display.update()

    running = True
    name = load_image("name.png")
    name = pygame.transform.scale(name, (width - 10, height - 10))
    screen.blit(name, (10, 10))
    pygame.display.flip()
    time.sleep(1)
    f = pygame.font.Font(None, width // 7)
    text = f.render('PRESENTS', True,
                      (255, 255, 0))
    screen.blit(text, (width * 0.25, height * 0.67))
    pygame.display.flip()
    time.sleep(2)
    screen.fill((0, 0, 0))
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width * 0.33, height * 0.25, width * 0.34, height * 0.2))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(width * 0.33, height * 0.25, width * 0.34, height * 0.2), 7)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width * 0.33, height * 0.5, width * 0.34, height * 0.2))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(width * 0.33, height * 0.5, width * 0.34, height * 0.2), 7)
    f = pygame.font.Font(None, width // 13)
    text = f.render('Играть', True, (0, 0, 255))
    screen.blit(text, (width * 0.4, height * 0.3))
    f = pygame.font.Font(None, width // 20)
    text = f.render('Статистика', True, (0, 0, 255))
    screen.blit(text, (width * 0.4, height * 0.58))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                if 0.33 * width <= x <= 0.67 * width and 0.25 * height <= y <= 0.45:
                    print('play')
                elif 0.33 * width <= x <= 0.67 * width and 0.5 * height <= y <= 0.7 * height:
                    print('results')
    pygame.quit()