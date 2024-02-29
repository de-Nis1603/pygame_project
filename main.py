import pygame
import os
import copy
import time


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
        self.colors = []
        self.mouse2_pos = (self.width // 2, 0)
        self.mouse1_pos = (self.width // 2, self.height - 1)
        self.fence_count_1 = self.height + 1
        self.fence_count_2 = self.height + 1
        self.turn = 1
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append((0, 0, 0))
            self.colors.append(row)
        self.hor_fence = []
        for i in range(self.height - 1):
            row = []
            for j in range(self.width):
                row.append(0)
            self.hor_fence.append(row)
        self.vert_fence = []
        for i in range(self.height):
            row = []
            for j in range(self.width - 1):
                row.append(0)
            self.vert_fence.append(row)
        print(self.hor_fence)
        print(self.vert_fence)

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
                pygame.draw.rect(surface, self.colors[i][j], pygame.Rect(self.left + j * self.cell_size,
                                                                 self.top + i * self.cell_size, self.cell_size,
                                                                 self.cell_size))
                pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self.left + j * self.cell_size,
                                                                       self.top + i * self.cell_size, self.cell_size,
                                                                       self.cell_size), 1)
        for i in range(len(self.hor_fence)):
            for j in range(len(self.hor_fence[i])):
                if self.hor_fence[i][j]:
                    pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.vert[j], self.hor[i + 1] - 1,
                                                                       self.cell_size, 2))
        for i in range(len(self.vert_fence)):
            for j in range(len(self.vert_fence[i])):
                if self.vert_fence[i][j]:
                    pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.vert[j + 1] - 1, self.hor[i],
                                                                       2, self.cell_size))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width - 0.5 * (width - 0.9 * height), 0.45 * height,
                                                              0.35 * (width - 0.9 * height), 0.1 * height), 7)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width - 0.5 * (width - 0.9 * height), 0.15 * height,
                                                              0.1 * (width - 0.9 * height), 0.1 * height), 2)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width - 0.5 * (width - 0.9 * height), 0.75 * height,
                                                              0.1 * (width - 0.9 * height), 0.1 * height), 2)
        f1 = pygame.font.Font(None, 40)
        text1 = f1.render(str(self.fence_count_1), True,
                          (0, 255, 0))
        f2 = pygame.font.Font(None, 40)
        text2 = f2.render(str(self.fence_count_2), True,
                          (0, 255, 0))
        f3 = pygame.font.Font(None, 36)
        text3 = f3.render('Сдаться', True,
                          (255, 255, 0))
        screen.blit(text2, (width - 0.5 * (width - 0.9 * height) + 0.1 * 0.35 * (width - 0.9 * height), 0.19 * height))
        screen.blit(text1, (width - 0.5 * (width - 0.9 * height) + 0.1 * 0.35 * (width - 0.9 * height), 0.79 * height))
        screen.blit(text3, (width - 0.5 * (width - 0.9 * height) + 0.1 * 0.35 * (width - 0.9 * height), 0.5 * height))

        mouse1 = load_image("trans_mouse1.png")
        mouse1 = pygame.transform.scale(mouse1, (cell_size, cell_size))
        screen.blit(mouse1, (self.vert[self.mouse1_pos[0]], self.hor[self.mouse1_pos[1]]))

        mouse2 = load_image("trans_mouse2.png")
        mouse2 = pygame.transform.scale(mouse2, (cell_size, cell_size))
        screen.blit(mouse2, (self.vert[self.mouse2_pos[0]], self.hor[self.mouse2_pos[1]]))

    def get_cell(self, pos):
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

    def get_click(self, pos):
        cell = self.get_cell(pos)
        self.on_click(cell)

    def on_click(self, cell):
        if not cell:
            return
        hor_ans, vert_ans = cell
        self.colors[vert_ans][hor_ans] = (203, 212, 172)

    def back_to_black(self):
        self.colors = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append((0, 0, 0))
            self.colors.append(row)


def put_fence(board, coords1, coords2, count):
    if count < 1:
        return
    if not we_can_put_fence(board, coords1, coords2):
        return "cancelled"
    print("allowed")
    if abs(coords1[0] - coords2[0]) == 1:
        a = max(coords1[0], coords2[0])
        if board.vert_fence[coords1[1]][a - 1] == 1:
            return "cancelled"
        board.vert_fence[coords1[1]][a - 1] = 1
    elif abs(coords1[1] - coords2[1]) == 1:
        b = min(coords1[1], coords2[1])
        if board.hor_fence[b][coords1[0]] == 1:
            return "cancelled"
        board.hor_fence[b][coords1[0]] = 1
    return "ok"

def we_can_put_fence(board, coords1, coords2):
    shadow_vert = copy.deepcopy(board.vert_fence)
    shadow_hor = copy.deepcopy(board.hor_fence)
    if abs(coords1[0] - coords2[0]) == 1:
        a = max(coords1[0], coords2[0])
        shadow_vert[coords1[1]][a - 1] = 1
    elif abs(coords1[1] - coords2[1]) == 1:
        b = min(coords1[1], coords2[1])
        shadow_hor[b][coords1[0]] = 1
    can_go_to_1 = []
    can_go_to_1.append(board.mouse1_pos)
    added_in_cycle = 1
    accessible_1 = False
    while added_in_cycle > 0:
        to_add = set()
        for i in range(len(can_go_to_1) - added_in_cycle, len(can_go_to_1)):
            cell = can_go_to_1[i]
            if cell[1] > 0 and shadow_hor[cell[1] - 1][cell[0]] == 0:
                to_add.add((cell[0], cell[1] - 1))
            if cell[1] < N - 1 and shadow_hor[cell[1]][cell[0]] == 0:
                to_add.add((cell[0], cell[1] + 1))
            if cell[0] > 0 and shadow_vert[cell[1]][cell[0] - 1] == 0:
                to_add.add((cell[0] - 1, cell[1]))
            if cell[0] < N - 1 and shadow_vert[cell[1]][cell[0]] == 0:
                to_add.add((cell[0] + 1, cell[1]))
        added_in_cycle = 0
        for elem in to_add:
            if elem[1] == 0:
                accessible_1 = True
                added_in_cycle = 0
                break
            if elem not in can_go_to_1:
                can_go_to_1.append(elem)
                added_in_cycle += 1

    can_go_to_2 = []
    can_go_to_2.append(board.mouse2_pos)
    added_in_cycle = 1
    accessible_2 = False
    while added_in_cycle > 0:
        to_add = set()
        for i in range(len(can_go_to_2) - added_in_cycle, len(can_go_to_2)):
            cell = can_go_to_2[i]
            if cell[1] > 0 and shadow_hor[cell[1] - 1][cell[0]] == 0:
                to_add.add((cell[0], cell[1] - 1))
            if cell[1] < N - 1 and shadow_hor[cell[1]][cell[0]] == 0:
                to_add.add((cell[0], cell[1] + 1))
            if cell[0] > 0 and shadow_vert[cell[1]][cell[0] - 1] == 0:
                to_add.add((cell[0] - 1, cell[1]))
            if cell[0] < N - 1 and shadow_vert[cell[1]][cell[0]] == 0:
                to_add.add((cell[0] + 1, cell[1]))
        added_in_cycle = 0
        for elem in to_add:
            if elem[1] == N - 1:
                accessible_2 = True
                added_in_cycle = 0
                break
            if elem not in can_go_to_2:
                can_go_to_2.append(elem)
                added_in_cycle += 1
    if accessible_1 and accessible_2:
        return True
    return False

def check_move(board, coords1, coords2):
    if coords1[0] == coords2[0]:
        if board.hor_fence[min(coords1[1], coords2[1])][coords1[0]]:
            return "cancelled"
    elif coords1[1] == coords2[1]:
        if board.vert_fence[coords1[1]][min(coords1[0], coords2[0])]:
            return "cancelled"
    return "ok"

def move(board, coords1, coords2):
    if board.mouse1_pos == coords1:
        if coords2 == board.mouse2_pos:
            return "cancelled"
        if check_move(board, coords1, coords2) == "cancelled":
            return "cancelled"
        board.mouse1_pos = coords2
    elif board.mouse2_pos == coords1:
        if coords2 == board.mouse1_pos:
            return "cancelled"
        if check_move(board, coords1, coords2) == "cancelled":
            return "cancelled"
        board.mouse2_pos = coords2
    return "ok"

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image

def change_turn(turn):
    if turn == 1:
        return 2
    return 1


if __name__ == '__main__':
    N = 3
    fence_count_1 = N + 1
    fence_count_2 = N + 1
    coords1 = None
    it_is_turn_for_player = 1

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Коридор')
    infoObject = pygame.display.Info()
    width, height = infoObject.current_w, infoObject.current_h - 10
    print(width, height)
    screen = pygame.display.set_mode((width, height))
    pygame.display.update()

    board = Board(N, N)
    cell_size = int(0.9 * height / N)
    board.set_view(0.35 * (width - 0.9 * height), 0.05 * height, cell_size)

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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords1_clicked = board.get_cell(event.pos)
                c1 = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                coords2_clicked = board.get_cell(event.pos)
                c2 = event.pos
                if width - 0.5 * (width - 0.9 * height) <= c2[0] <= width - 0.15 * (width - 0.9 * height) and width - 0.5 * (width - 0.9 * height) <= c1[0] <= width - 0.15 * (width - 0.9 * height) and 0.45 * height <= c1[1] <= 0.55 * height and 0.45 * height <= c2[1] <= 0.55 * height:
                    print("giving up")
                if coords1_clicked == coords2_clicked and coords1_clicked:
                    # скорее всего двигаем мышь,
                    # но это неточно, поэтому перепроверим
                    if coords1:
                         if coords1 == coords1_clicked:
                            coords1 = None
                            # точно ходим мышкой
                            if abs(board.mouse1_pos[0] - coords1_clicked[0]) + abs(board.mouse1_pos[1] - coords1_clicked[1]) == 1 and it_is_turn_for_player == 1:
                                verdict = move(board, board.mouse1_pos, coords1_clicked)
                                if verdict == "ok":
                                    it_is_turn_for_player = change_turn(it_is_turn_for_player)
                                    print(it_is_turn_for_player)
                            elif abs(board.mouse2_pos[0] - coords1_clicked[0]) + abs(board.mouse2_pos[1] - coords1_clicked[1]) == 1 and it_is_turn_for_player == 2:
                                verdict = move(board, board.mouse2_pos, coords1_clicked)
                                if verdict == "ok":
                                    it_is_turn_for_player = change_turn(it_is_turn_for_player)
                                    print(it_is_turn_for_player)
                            elif abs(board.mouse2_pos[0] - coords1_clicked[0]) + abs(board.mouse2_pos[1] - coords1_clicked[1]) == 1 and abs(board.mouse2_pos[0] - board.mouse1_pos[0]) + abs(board.mouse2_pos[1] - board.mouse1_pos[1]) == 1 and board.mouse1_pos != coords1_clicked and it_is_turn_for_player == 1 and check_move(board, board.mouse1_pos, board.mouse2_pos) == "ok" and check_move(board, board.mouse2_pos, coords1_clicked) == "ok":
                                verdict = move(board, board.mouse1_pos, coords1_clicked)
                                if verdict == "ok":
                                    it_is_turn_for_player = change_turn(it_is_turn_for_player)
                                    print(it_is_turn_for_player)
                            elif abs(board.mouse1_pos[0] - coords1_clicked[0]) + abs(board.mouse1_pos[1] - coords1_clicked[1]) == 1 and abs(board.mouse1_pos[0] - board.mouse2_pos[0]) + abs(board.mouse1_pos[1] - board.mouse2_pos[1]) == 1 and board.mouse2_pos != coords1_clicked and it_is_turn_for_player == 2 and check_move(board, board.mouse2_pos, board.mouse1_pos) == "ok" and check_move(board, board.mouse1_pos, coords1_clicked) == "ok":
                                verdict = move(board, board.mouse2_pos, coords1_clicked)
                                if verdict == "ok":
                                    it_is_turn_for_player = change_turn(it_is_turn_for_player)
                                    print(it_is_turn_for_player)
                            else:
                                coords1 = None
                                coords1_clicked = None
                                coords2_clicked = None
                         else:
                             coords1 = coords1_clicked
                             coords1_clicked = None
                             coords2_clicked = None
                    else:
                        coords1 = coords1_clicked
                elif coords1_clicked and abs(coords1_clicked[0] - coords2_clicked[0]) + abs(coords1_clicked[1] - coords2_clicked[1]) == 1:
                    # точно ставим забор
                    if it_is_turn_for_player == 1:
                        verdict = put_fence(board, coords1_clicked, coords2_clicked, fence_count_1)
                    elif it_is_turn_for_player == 2:
                        verdict = put_fence(board, coords1_clicked, coords2_clicked, fence_count_2)
                    if verdict == "ok":
                        if it_is_turn_for_player == 1:
                            board.fence_count_1 -= 1
                            fence_count_1 -= 1
                        elif it_is_turn_for_player == 2:
                            board.fence_count_2 -= 1
                            fence_count_2 -= 1
                        it_is_turn_for_player = change_turn(it_is_turn_for_player)
                        print(it_is_turn_for_player)
                    else:
                        coords1 = None
                        coords1_clicked = None
                        coords2_clicked = None
                else:
                    coords1 = None
                    coords1_clicked = None
                    coords2_clicked = None
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()