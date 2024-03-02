import pygame
import sqlite3
import random

if __name__ == '__main__':
    pygame.init()
    infoObject = pygame.display.Info()
    size = width, height = infoObject.current_w, infoObject.current_h - 10
    screen = pygame.display.set_mode(size)

    connection = sqlite3.connect("random_stats.sqlite")
    cur = connection.cursor()
    games_played = cur.execute("""SELECT games_played FROM types""").fetchone()[0]
    fences_put = cur.execute('''SELECT fences_put FROM types''').fetchone()[0]
    turns_made = cur.execute('''SELECT turns_made FROM types''').fetchone()[0]
    average_turns = cur.execute('''SELECT average_turns FROM types''').fetchone()[0]
    one_wins = cur.execute('''SELECT one_wins FROM types''').fetchone()[0]
    two_wins = cur.execute('''SELECT two_wins FROM types''').fetchone()[0]

    params = {"Игр сыграно": games_played,
              "Заборов возведено": fences_put,
              "Ходов сделано": turns_made,
              "Среднее число ходов": average_turns,
              "Побед первого": one_wins,
              "Побед второго": two_wins}
    f = pygame.font.Font(None, width // 25)
    for index, key in enumerate(params):
        text = f'{key}: {params[key]}'
        text = f.render(text, True,
                        (255, 255, 0))
        screen.blit(text, (width * 0.25, height * 0.33 + 50 * index))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width * 0.75, height * 0.1, width * 0.2, height * 0.15))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width * 0.75, height * 0.1, width * 0.2, height * 0.15), 7)
    f = pygame.font.Font(None, width // 15)
    text = f.render("Меню", True, (255, 255, 255))
    screen.blit(text, (width * 0.78, height * 0.16))
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                if 0.75 * width <= x <= 0.95 * width and 0.1 * height <= y <= 0.25 * height:
                    print('menu')
                    # возвращаемся в меню
    pygame.quit()