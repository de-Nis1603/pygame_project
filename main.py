import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.vert = []
        self.hor = []
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.hor.append(self.top)
        for i in range(1, self.height + 1):
            self.hor.append(self.top + i * self.cell_size)
        self.vert.append(self.left)
        for j in range(1, self.width + 1):
            self.vert.append(self.left + j * self.cell_size)

    def render(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self.left + j * self.cell_size,
                                                                       self.top + i * self.cell_size, self.cell_size,
                                                                       self.cell_size), 1)

    def shower(self, pos):
        x_pos, y_pos = int(pos[0]), int(pos[1])
        hor_ans, vert_ans = None, None
        for i in range(self.width):
            if self.vert[i] <= x_pos and x_pos <= self.vert[i + 1]:
                hor_ans = i
        for j in range(self.height):
            if self.hor[j] <= y_pos and y_pos <= self.hor[j + 1]:
                vert_ans = j
        if hor_ans is None or vert_ans is None:
            return
        else:
            return hor_ans, vert_ans


if __name__ == '__main__':
    N = 7
    coords1, coords2 = None, None

    pygame.init()
    pygame.display.set_caption('Коридор')
    infoObject = pygame.display.Info()
    width, height = infoObject.current_w, infoObject.current_h - 10
    screen = pygame.display.set_mode((width, height))
    pygame.display.update()

    board = Board(N, N)
    cell_size = int(0.9 * height / N)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not coords1:
                    coords1 = board.shower(event.pos)
                else:
                    coords2 = board.shower(event.pos)
                    if abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1]) == 1:
                        pass
                        # put fence
                    else:
                        coords1 = coords2
                        coords2 = None
                board.shower(event.pos)
        screen.fill((0, 0, 0))
        board.set_view(0.5 * (width - 0.9 * height), 0.05 * height, cell_size)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()